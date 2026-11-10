<div align="center">

# 🇧🇷 ACBr · SVN Mirror

### Automação Comercial Brasil — espelho automatizado no GitHub

[![Sincronizar ACBr SVN](https://github.com/fraurino/ACBr-SVN-Mirror/actions/workflows/sync-acbr.yml/badge.svg)](https://github.com/fraurino/ACBr-SVN-Mirror/actions/workflows/sync-acbr.yml)
[![GitHub](https://img.shields.io/badge/GitHub-Espelho%20não%20oficial-181717?logo=github)](https://github.com/fraurino/ACBr-SVN-Mirror)
[![Origem](https://img.shields.io/badge/Origem-SVN%20SourceForge-orange)](https://svn.code.sf.net/p/acbr/code/trunk2)
[![Comunidade](https://img.shields.io/badge/Comunidade-Fórum%20ACBr-blue)](https://www.projetoacbr.com.br/forum/)

**Componentes, bibliotecas e ferramentas para automação comercial e documentos fiscais no Brasil.**

[🌐 Portal oficial](https://projetoacbr.com.br/) · [💬 Fórum ACBr](https://www.projetoacbr.com.br/forum/) · [📦 SVN oficial](https://svn.code.sf.net/p/acbr/code/trunk2) · [⚙️ Sincronizações](https://github.com/fraurino/ACBr-SVN-Mirror/actions)

</div>

---

> [!IMPORTANT]
> **Este é um espelho comunitário e NÃO OFICIAL do Projeto ACBr.**
> O desenvolvimento, a manutenção e o suporte oficiais acontecem nos canais do **Projeto ACBr**. Este repositório não representa nem substitui a equipe oficial. Para relatar problemas dos componentes ou tirar dúvidas, procure o [Fórum ACBr](https://www.projetoacbr.com.br/forum/).

## 🚀 Sobre o Projeto ACBr

**ACBr** significa **Automação Comercial Brasil**. O projeto reúne componentes, fontes, bibliotecas e aplicações voltados ao desenvolvimento de sistemas de automação comercial, com forte presença no ecossistema **Delphi / Object Pascal / Lazarus**.

Entre as áreas atendidas estão:

| Área | Exemplos |
| --- | --- |
| 🧾 Documentos fiscais eletrônicos | NF-e, NFC-e, CT-e, MDF-e e NFS-e |
| 💳 Pagamentos | TEF, PIX e boletos |
| 🖨️ Automação comercial | Impressoras, etiquetas, dispositivos e periféricos |
| 📚 Obrigações e integrações | SPED, arquivos fiscais e outros recursos |
| 🧩 Bibliotecas e utilitários | ACBrLib, ACBrMonitorPLUS e componentes diversos |

Os recursos disponíveis variam conforme a versão e os componentes publicados pelo projeto oficial.

## 🔄 Como funciona este espelho?

Este repositório mantém uma **cópia dos arquivos da árvore `trunk2` do SVN oficial** por meio do GitHub Actions.

```text
  Projeto ACBr (SVN / SourceForge)
  https://svn.code.sf.net/p/acbr/code/trunk2
                    │
                    ▼
         GitHub Actions (agendado)
                    │
          Consulta revisão do SVN
                    │
           ┌────────┴────────┐
           │                 │
      Sem mudanças      Nova revisão
           │                 │
        Encerra        Exporta arquivos
                             │
                      Atualiza espelho
                             │
                     Commit automático
                             │
                             ▼
             github.com/fraurino/ACBr-SVN-Mirror
```

- ⏱️ **Verificação programada:** duas vezes por hora (minutos 07 e 37, UTC).
- 🔍 **Detecção de mudanças:** comparação da revisão SVN com o arquivo `.svn-revision`.
- 📂 **Atualização:** exportação dos arquivos do `trunk2`, incluindo remoções e alterações.
- 📝 **Rastreabilidade:** commits com mensagens no formato `sync: ACBr SVN r49080`.
- ▶️ **Execução manual:** disponível na aba [Actions](https://github.com/fraurino/ACBr-SVN-Mirror/actions).

> [!NOTE]
> O agendamento do GitHub Actions é **periódico**, não instantâneo. O GitHub pode atrasar execuções. Este espelho registra snapshots sincronizados em commits Git; **não importa todo o histórico original de commits do SVN**.

### 📊 Consultar a revisão sincronizada

Abra [`.svn-revision`](https://github.com/fraurino/ACBr-SVN-Mirror/blob/main/.svn-revision) para consultar o número da última revisão do SVN registrada no espelho.

Confira também o [histórico de commits](https://github.com/fraurino/ACBr-SVN-Mirror/commits/main/) e o [status do workflow](https://github.com/fraurino/ACBr-SVN-Mirror/actions/workflows/sync-acbr.yml).

## 📥 Como obter os fontes

Para clonar a cópia disponível neste GitHub:

```bash
git clone https://github.com/fraurino/ACBr-SVN-Mirror.git
```

Para utilizar diretamente o repositório **oficial** do ACBr via Subversion:

```bash
svn checkout https://svn.code.sf.net/p/acbr/code/trunk2 ACBr
```

**Recomendação:** para instalação, atualização, configuração de dependências e suporte aos componentes, consulte sempre as orientações oficiais do ACBr. Um clone Git deste espelho não substitui o procedimento oficial de instalação.

## 🔗 Links úteis e comunidade

| Recurso | Link |
| --- | --- |
| 🌐 **Portal do Projeto ACBr** | [projetoacbr.com.br](https://projetoacbr.com.br/) |
| 💬 **Fórum oficial** | [Comunidade ACBr](https://www.projetoacbr.com.br/forum/) |
| 🧠 **Base de conhecimento e categorias** | [Fórum Aberto ACBr](https://www.projetoacbr.com.br/forum/forum/37-f%C3%B3rum-aberto-acbr/) |
| 🛠️ **Dúvidas gerais e instalação** | [Dúvidas Gerais sobre o ACBr](https://www.projetoacbr.com.br/forum/forum/3-d%C3%BAvidas-gerais-sobre-o-acbr/) |
| 📰 **Notícias e atualizações** | [Notícias do ACBr](https://www.projetoacbr.com.br/forum/forum/35-not%C3%ADcias-do-acbr/) |
| 📖 **Sobre o ACBr e perguntas frequentes** | [Conheça o projeto](https://projetoacbr.com.br/sobre/) |
| 🗃️ **Código-fonte original** | [SVN trunk2 no SourceForge](https://svn.code.sf.net/p/acbr/code/trunk2) |
| ⚙️ **Automação deste espelho** | [GitHub Actions](https://github.com/fraurino/ACBr-SVN-Mirror/actions) |

## 🤝 Contribuições e suporte

Quer contribuir com o **Projeto ACBr** ou discutir problemas nos componentes? Utilize os canais oficiais e as orientações da comunidade no [Fórum ACBr](https://www.projetoacbr.com.br/forum/).

Este repositório tem finalidade de **espelhamento e consulta**. Alterações feitas diretamente nos arquivos espelhados podem ser substituídas na próxima sincronização. Para personalizações, mantenha seu próprio fork ou branch.

## ⚖️ Créditos e licenciamento

Todo o reconhecimento pelo desenvolvimento dos componentes e bibliotecas pertence aos **autores, mantenedores e colaboradores do Projeto ACBr**.

Os arquivos espelhados preservam seus avisos e termos de licença originais. **Consulte as licenças e os cabeçalhos de cada componente antes de redistribuir ou utilizar os fontes.** A existência deste espelho não altera os termos estabelecidos pelos titulares.

---

<div align="center">

**Feito para facilitar o acesso e o acompanhamento das atualizações do ACBr.** 🇧🇷

⭐ Se este espelho for útil, considere marcar o repositório com uma estrela.

**[Visite o Projeto ACBr](https://projetoacbr.com.br/) · [Participe do Fórum](https://www.projetoacbr.com.br/forum/)**

</div>
