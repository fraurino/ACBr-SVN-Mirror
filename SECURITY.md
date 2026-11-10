# 🔐 Política de Segurança — ACBr-SVN-Mirror

Obrigado por ajudar a manter este repositório e a comunidade mais seguros.

> [!IMPORTANT]
> **Este repositório é um espelho comunitário, não oficial, do Projeto ACBr.** Os componentes e fontes são provenientes do [SVN oficial do ACBr](https://svn.code.sf.net/p/acbr/code/trunk2). Este espelho **não é responsável pelo desenvolvimento nem pela correção de vulnerabilidades no código original**.

## 📦 Versões com suporte

| Conteúdo | Política |
| --- | --- |
| Arquivos espelhados do `trunk2` | Acompanham a revisão disponível no SVN oficial; correções devem ser tratadas pelos mantenedores do ACBr |
| Automação de sincronização (`.github/workflows/`) | Mantida neste repositório; relatos de segurança são bem-vindos |
| Documentação e configuração próprias deste espelho | Mantidas neste repositório |

Não há garantia de suporte individual a versões antigas, nem um prazo de correção ou divulgação estabelecido para este espelho.

## 🚨 Como relatar uma vulnerabilidade

### 1. Problemas nos componentes ou no código do Projeto ACBr

Caso a vulnerabilidade afete **NF-e, NFC-e, CT-e, MDF-e, NFS-e, ACBrLib, ACBrMonitorPLUS ou qualquer outro componente original do ACBr**, procure os canais oficiais:

- 🌐 [Portal do Projeto ACBr](https://projetoacbr.com.br/)
- 💬 [Fórum oficial ACBr](https://www.projetoacbr.com.br/forum/)

**Não publique detalhes exploráveis, credenciais ou informações sensíveis em tópicos públicos.** Solicite aos responsáveis pelo projeto um canal privado adequado antes de compartilhar uma prova de conceito.

### 2. Problemas específicos deste espelho GitHub

Se a falha envolver o **workflow de sincronização, permissões, configuração ou outros arquivos próprios deste repositório**, utilize preferencialmente o canal privado do GitHub:

- 🔒 [Report a vulnerability / Private vulnerability reporting](https://github.com/fraurino/ACBr-SVN-Mirror/security/advisories/new) — **quando o recurso estiver habilitado** pelo proprietário.

Se esse formulário não estiver disponível, entre em contato com o proprietário do repositório pelo [perfil GitHub @fraurino](https://github.com/fraurino) para combinar um canal privado. **Não abra uma Issue pública com informações que permitam explorar a falha.**

### O que incluir no relato

Para facilitar a análise, informe, quando possível:

1. **Descrição:** comportamento observado e impacto potencial.
2. **Local afetado:** arquivo, workflow, componente e/ou caminho.
3. **Reprodução:** passos mínimos, em ambiente autorizado, sem dados reais sensíveis.
4. **Evidências:** logs sanitizados, mensagens de erro ou demonstração controlada.
5. **Referências:** revisão SVN, commit Git e versões relevantes.
6. **Mitigação sugerida:** se houver.

Nunca inclua senhas, tokens, certificados digitais, chaves privadas, dados fiscais de terceiros ou informações pessoais em relatórios públicos.

## 🔄 Processo de tratamento

Para problemas específicos do espelho, o mantenedor poderá avaliar o relato, reproduzir o comportamento, aplicar uma correção e publicar orientações quando apropriado. **Não são prometidos prazos fixos de resposta ou resolução.**

Para falhas no código original, a correção depende dos responsáveis pelo **Projeto ACBr** e de sua distribuição oficial. A atualização deste espelho ocorrerá conforme as sincronizações programadas e a disponibilidade do SVN.

## 🛡️ Boas práticas para usuários

- Confira a origem dos arquivos e a revisão registrada em [`.svn-revision`](https://github.com/fraurino/ACBr-SVN-Mirror/blob/main/.svn-revision).
- Consulte os canais oficiais antes de aplicar correções fiscais ou de segurança em produção.
- Proteja certificados digitais, credenciais, tokens e arquivos de configuração.
- Valide alterações em ambiente de testes antes de atualizar sistemas de clientes.
- Considere que a sincronização automática pode ter atrasos e não substitui a verificação de comunicados oficiais.

## ⚖️ Escopo e responsabilidade

Este repositório tem finalidade de **espelhamento e consulta**. A publicação de uma cópia dos fontes não implica auditoria de segurança, certificação, garantia de ausência de vulnerabilidades ou vínculo oficial com o Projeto ACBr.

Agradecemos relatos responsáveis e o respeito ao trabalho dos autores, mantenedores e colaboradores do ACBr.
