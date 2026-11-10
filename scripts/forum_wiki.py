#!/usr/bin/env python3
"""Public forum topic indexer. No login, no full-post scraping, no external deps."""
import datetime as dt
import html
import json
import os
import pathlib
import re
import time
import urllib.parse
import urllib.request
from html.parser import HTMLParser

ROOT = "https://www.projetoacbr.com.br"
FORUM = ROOT + "/forum/"
OUT = pathlib.Path("wiki-content")
STATE = pathlib.Path(".github/forum-wiki-state.json")
MAX_FORUMS = 160
MAX_TOPICS = 25
DELAY = 1.5

class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.href = None
        self.text = []
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self.href = dict(attrs).get("href", "")
            self.text = []
    def handle_data(self, data):
        if self.href is not None:
            self.text.append(data)
    def handle_endtag(self, tag):
        if tag == "a" and self.href is not None:
            self.links.append((self.href, " ".join(" ".join(self.text).split())))
            self.href = None

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "ACBr-SVN-Mirror-Wiki/1.0 (public link index; https://github.com/fraurino/ACBr-SVN-Mirror)", "Accept": "text/html"})
    with urllib.request.urlopen(req, timeout=35) as response:
        if response.status != 200:
            raise RuntimeError(f"HTTP {response.status}")
        data = response.read(2_000_000)
        return data.decode("utf-8", errors="replace")

def canonical(url, kind):
    u = urllib.parse.urljoin(FORUM, html.unescape(url))
    p = urllib.parse.urlsplit(u)
    if p.scheme != "https" or p.netloc != "www.projetoacbr.com.br":
        return None
    m = re.match(r"^/forum/" + kind + r"/(\d+)-[^/?#]+/?$", p.path)
    if not m:
        return None
    return urllib.parse.urlunsplit(("https", p.netloc, p.path.rstrip("/") + "/", "", ""))

def discover(page, kind):
    parser = Links()
    parser.feed(page)
    found = {}
    for url, title in parser.links:
        normalized = canonical(url, kind)
        if normalized and title and len(title) >= 4:
            found.setdefault(normalized, title[:180])
    return found

def md(s):
    return re.sub(r"([\\\[\]_*|])", r"\\\1", s).replace("\n", " ").strip()

def main():
    OUT.mkdir(exist_ok=True)
    old = json.loads(STATE.read_text(encoding="utf-8")) if STATE.exists() else {}
    categories = dict(old.get("categories", {}))
    topics = dict(old.get("topics", {}))
    errors = []
    now = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    home = fetch(FORUM)
    categories.update(discover(home, "forum"))
    # Traverse public subforums by following only discovered forum links.
    visited = set()
    queue = list(categories)
    while queue and len(visited) < MAX_FORUMS:
        url = queue.pop(0)
        if url in visited:
            continue
        visited.add(url)
        try:
            time.sleep(DELAY)
            page = fetch(url)
            new = discover(page, "forum")
            for child, title in new.items():
                if child not in categories:
                    categories[child] = title
                    queue.append(child)
            found = discover(page, "topic")
            for link, title in list(found.items())[:MAX_TOPICS]:
                topics[link] = {"title": title, "forum": url, "last_seen": now}
        except Exception as exc:
            errors.append(f"{url}: {type(exc).__name__}")
    # Keep a bounded rolling index, without copying post bodies or private content.
    if len(topics) > 3000:
        topics = dict(sorted(topics.items(), key=lambda kv: kv[1].get("last_seen", ""), reverse=True)[:3000])
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps({"categories": categories, "topics": topics}, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = ["# ACBr — Índice do Fórum Público", "", "> **Espelho comunitário não oficial.** Este índice contém somente títulos e links públicos. Não reproduz mensagens nem representa orientação oficial do Projeto ACBr.", "", f"Última consulta: **{now}** · Categorias descobertas: **{len(categories)}** · Tópicos indexados: **{len(topics)}**.", "", "## Categorias públicas", ""]
    for link, title in sorted(categories.items(), key=lambda kv: kv[1].casefold()):
        lines.append(f"- [{md(title)}]({link})")
    lines += ["", "## Tópicos encontrados", "", "A lista registra tópicos visíveis nas primeiras páginas das categorias consultadas, incluindo dúvidas gerais. **Não representa todo o histórico do fórum**.", ""]
    for link, info in sorted(topics.items(), key=lambda kv: kv[1].get("last_seen", ""), reverse=True):
        lines.append(f"- [{md(info['title'])}]({link}) — [categoria]({info['forum']})")
    lines += ["", "## Limitações e direitos", "", "- Apenas páginas públicas, sem login, sem copiar mensagens, imagens ou anexos.", "- Títulos e links podem mudar; consulte sempre o tópico original.", "- Atualização programada a cada 6 horas; sujeita a indisponibilidade, bloqueios e atrasos.", "- Caso o fórum restrinja automação, interrompa a coleta e solicite autorização.", ""]
    (OUT / "Forum-ACBr.md").write_text("\n".join(lines), encoding="utf-8")
    (OUT / "Home.md").write_text("# ACBr-SVN-Mirror — Wiki\n\n> Wiki comunitária não oficial; consulte sempre o [Fórum ACBr](https://www.projetoacbr.com.br/forum/).\n\n- [Índice de tópicos e categorias públicas](Forum-ACBr)\n- [Repositório e sincronização SVN](https://github.com/fraurino/ACBr-SVN-Mirror)\n\nOs títulos e links são indexados automaticamente, sem reprodução integral de conteúdo.\n", encoding="utf-8")
    print(f"Categorias: {len(categories)}; tópicos: {len(topics)}; erros: {len(errors)}")
    if errors:
        print("Avisos:", "; ".join(errors[:8]))
    if not categories:
        raise RuntimeError("Nenhuma categoria pública encontrada; verifique acesso e estrutura HTML")

if __name__ == "__main__":
    main()
