# 🤝 Como contribuir com o ACBr-SVN-Mirror

Obrigado pelo interesse! Este é um **espelho não oficial** do [SVN do Projeto ACBr](https://svn.code.sf.net/p/acbr/code/trunk2).

## Onde contribuir?

- **Correções de componentes ACBr:** encaminhe propostas e dúvidas ao [Fórum oficial ACBr](https://www.projetoacbr.com.br/forum/). Alterações diretas nos arquivos espelhados serão substituídas pela sincronização.
- **Problemas no espelho:** abra uma Issue para falhas no workflow, na documentação ou na atualização automática.
- **Falhas de segurança:** siga o [SECURITY.md](SECURITY.md); não divulgue detalhes exploráveis em Issues públicas.

## Pull requests

1. Abra uma Issue descrevendo a melhoria, quando apropriado.
2. Faça alterações somente nos arquivos de manutenção deste espelho (por exemplo, `.github/`, `README.md`, `SECURITY.md` e documentos da comunidade).
3. Não inclua certificados, credenciais, tokens, dados pessoais ou dados fiscais de terceiros.
4. Explique o motivo da mudança e como testá-la.
5. Não altere as licenças e os avisos originais dos componentes ACBr.

O projeto é mantido por voluntariado, sem compromisso de prazo para análise ou aprovação.

## Sincronização

O workflow `.github/workflows/sync-acbr.yml` consulta periodicamente o SVN oficial. Consulte a [aba Actions](https://github.com/fraurino/ACBr-SVN-Mirror/actions) e a revisão em `.svn-revision`. O histórico original do SVN não é importado integralmente.
