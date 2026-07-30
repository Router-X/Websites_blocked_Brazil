# Websites_blocked_Brazil

> Lista consolidada e versionada de domínios com ordem de bloqueio no Brasil, extraídos de ofícios e decisões judiciais.
>
> *Consolidated, version-controlled list of domains under blocking orders in Brazil, extracted from official notices and court decisions.*

[![Update](https://img.shields.io/badge/atualiza%C3%A7%C3%A3o-autom%C3%A1tica-brightgreen)](#atualização--updates)
[![Fonte](https://img.shields.io/badge/fonte-ANATEL%20%2F%20ANCINE%20%2F%20Judici%C3%A1rio-blue)](#origem-dos-dados--data-sources)
[![Formato](https://img.shields.io/badge/formato-um%20dom%C3%ADnio%20por%20linha-lightgrey)](#formato-da-lista--list-format)

---

## Sobre / About

**PT** — Este repositório mantém uma lista pública de domínios que constam em ordens de bloqueio emitidas por órgãos brasileiros (ANATEL, ANCINE) e pelo Poder Judiciário. A lista é destinada ao consumo por provedores de acesso, operadores de rede e sistemas de DNS que precisam aplicar bloqueios de forma padronizada e reproduzível.

**EN** — This repository maintains a public list of domains named in blocking orders issued by Brazilian authorities (ANATEL, ANCINE) and the Judiciary. It is intended for consumption by ISPs, network operators, and DNS systems that need to apply blocks in a standardized, reproducible way.

> **Aviso Legal e Finalidade / Disclaimer & Purpose**
> 
> **PT** — Todo o conteúdo, dados e metodologias disponibilizados neste repositório têm caráter estritamente educativo, de teste e para fins de estudo. Esta lista reflete determinações de terceiros e é fornecida "como está", sem garantia de completude ou atualidade. A responsabilidade pela utilização, aplicação, revisão ou contestação de qualquer informação ou bloqueio é inteira e exclusiva do usuário que a executa. Este repositório não emite, endossa nem contesta as ordens que compila.
>
> **EN** — *All content, data, and methodologies provided in this repository are strictly for educational, testing, and research purposes. This list reflects third-party determinations and is provided "as is", without warranty of completeness or timeliness. The application, implementation, review, or challenge of any information or block is the sole responsibility of the individual user. This repository neither issues, endorses, nor challenges the orders it compiles.*


---

## Arquivos do repositório / Repository files

| Arquivo | Conteúdo | Editável manualmente |
|---|---|---|
| `Websites_for_block` | A lista de bloqueio. Um domínio por linha, ordenado. | Não — gerado |
| `version` | Versão da lista no formato `AAAAMMDDNN`. | Não — gerado |
| `desbloqueados.txt` | Domínios com ordem de **desbloqueio**. Removidos da lista e nunca readmitidos. | Sim |
| `ignore-institucionais.txt` | Órgãos e tribunais citados nos ofícios (descartados na extração). | Sim |
| `ignore-legitimos.txt` | Sites legítimos citados como prova ou referência (nunca alvo). | Sim |
| `ignore-ruido.txt` | Fragmentos e leituras de OCR corrompidas, confirmados manualmente. | Sim |
| `tlds.txt` | Cache da lista oficial de TLDs da IANA, usada na validação. | Não — gerado |
| `processados.json` | Manifesto de rastreabilidade: qual ofício originou cada domínio. | Não — gerado |

---

## Formato da lista / List format

`Websites_for_block` contém **um domínio por linha**, em minúsculas, sem esquema (`http://`), sem caminho e sem porta:

```
exemplo-bloqueado.com
outro-dominio.net
sub.terceiro-dominio.com.br
```

Notas de formato:

- Domínios e subdomínios são mantidos **exatamente como constam no ofício** — `www.exemplo.com` e `exemplo.com` são tratados como entradas distintas, pois representam hosts distintos.
- Domínios internacionalizados (IDN) aparecem em sua forma *punycode* (`xn--…`).
- A lista é ordenada alfabeticamente e livre de duplicatas.

**EN** — `Websites_for_block` holds **one domain per line**, lowercase, with no scheme, path, or port. Entries are kept exactly as they appear in the source notice; `www.host` and the apex are distinct. IDN domains appear in punycode. The list is sorted and deduplicated.

---

## Versionamento / Versioning

O arquivo `version` segue o formato `AAAAMMDDNN`:

| Campo | Significado |
|---|---|
| `AAAAMMDD` | Data da geração |
| `NN` | Sequência da geração naquele dia (`01`, `02`, …) |

Exemplo: `2026072403` = terceira atualização de 24/07/2026. A versão só muda quando a lista efetivamente muda.

---

## Origem dos dados / Data sources

Os domínios são extraídos de:

- **Ofícios da ANATEL e ANCINE** — listas operacionais de bloqueio, frequentemente em formato de tabela.
- **Decisões judiciais** — determinações do Poder Judiciário, em texto corrido ou anexo.

Cada domínio adicionado é registrado em `processados.json` com o ofício de origem e a data de processamento, permitindo rastrear a procedência de qualquer entrada da lista.

---

## Atualização / Updates

A lista é atualizada por um processo automatizado que:

1. Lê os ofícios recebidos (PDF), incluindo documentos escaneados via OCR.
2. Extrai os domínios, validando cada um contra a lista oficial de TLDs da IANA.
3. Descarta ruído — órgãos, sites legítimos e fragmentos — usando as listas `ignore-*`.
4. Remove os domínios que constam em `desbloqueados.txt`.
5. Consolida, deduplica, versiona e publica o resultado.

Cada publicação passa por um conjunto de verificações automáticas antes de ser liberada, incluindo controle de perdas, detecção de regressões e conferência de domínios lidos por OCR.

> O arquivo `main.py`, referenciado em versões anteriores deste README, é legado e não faz parte do fluxo atual.

---

## Como consumir a lista / How to consume the list

Clonar o repositório:

```bash
git clone https://github.com/Router-X/Websites_blocked_Brazil.git
```

Ou obter apenas o arquivo da lista, sempre na versão mais recente:

```bash
curl -sfL https://raw.githubusercontent.com/Router-X/Websites_blocked_Brazil/main/Websites_for_block -o Websites_for_block
```

Verificar a versão atual:

```bash
curl -sfL https://raw.githubusercontent.com/Router-X/Websites_blocked_Brazil/main/version
```

### Exemplo de aplicação em DNS

A lista é agnóstica quanto ao mecanismo de bloqueio. Um domínio na lista pode ser aplicado, por exemplo, como:

```
# Unbound — bloqueia a zona inteira (apex + subdomínios)
local-zone: "exemplo-bloqueado.com" always_nxdomain

# dnsmasq
address=/exemplo-bloqueado.com/0.0.0.0
```

> **Atenção ao escopo** — como a lista preserva `www.host` e o apex separadamente, mecanismos que tratam o apex como zona inteira (Unbound `always_nxdomain`, dnsmasq `address=/`, RPZ com wildcard) cobrem ambos automaticamente. Mecanismos de correspondência exata exigem que cada host esteja presente na lista.

---

## Contribuindo / Contributing

Este repositório é a saída de um processo interno de compilação. Correções pontuais são bem-vindas:

- **Domínio bloqueado indevidamente** (ex.: site legítimo capturado por engano) — abra uma [issue](https://github.com/Router-X/Websites_blocked_Brazil/issues) indicando o domínio e, se possível, a referência do ofício.
- **Domínio faltante** — abra uma issue com o domínio e o ofício de origem.

Como o arquivo `Websites_for_block` é gerado automaticamente, edições diretas nele são sobrescritas na próxima atualização. Ajustes duradouros são feitos nas listas `desbloqueados.txt` e `ignore-*`.

---

## Licença / License

Este repositório é licenciado sob **[Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)**.

Você pode copiar, redistribuir, adaptar e usar esta lista para qualquer finalidade, inclusive comercial, desde que atribua o crédito ao **Router-X**. Consulte o arquivo [`LICENSE`](LICENSE) para o texto completo.

*Licensed under CC BY 4.0. You may share and adapt this list for any purpose, including commercial, provided you give appropriate credit to Router-X. See [`LICENSE`](LICENSE) for the full text.*

---

## Contato / Contact

Para reportes fora das [issues](https://github.com/Router-X/Websites_blocked_Brazil/issues): **servidores@routerx.net.br**

---

<sub>Desenvolvido por **Router-X** · versão 6</sub>
