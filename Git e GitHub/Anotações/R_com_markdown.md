# O que é R Markdown?

R Markdown é uma linguagem de marcação baseada em Markdown que é utilizada para criar documentos dinâmicos e reprodutíveis com R. Ele permite combinar texto descritivo e código R no mesmo documento, facilitando a produção de relatórios, apresentações, documentos científicos, e até livros. Alguns dos principais recursos e benefícios do R Markdown incluem:

1. **Integração com R**: Você pode incluir código R diretamente no documento e, quando ele é renderizado, os resultados da execução do código (gráficos, tabelas, etc.) são incorporados automaticamente no documento final.
2. **Flexibilidade de saída**: Documentos R Markdown podem ser convertidos em vários formatos de saída, incluindo HTML, PDF, Word, slides em HTML, e muito mais.
3. **Reprodutibilidade**: Como o código R é incluído no próprio documento, qualquer pessoa pode reexecutar o código e obter os mesmos resultados, o que é essencial para a ciência reprodutível.
4. **Fácil de usar**: Baseado em Markdown, uma linguagem de marcação leve e fácil de aprender, permitindo que você se concentre no conteúdo em vez de se preocupar com a formatação.

Exemplo simples de um documento R Markdown:

~~~markdown
---
title: "Meu Relatório R Markdown"
author: "Rafaela BF"
date: "24 de Julho de 2024"
output: html_document
---

## Introdução

Um exemplo de um documento R Markdown. Você pode incluir texto e código R.

```{r}
# Este é um bloco de código R
summary(cars)
```
~~~

> Arquivo em [testeDeArquivo.Rmd](https://github.com/RafaelaBF/Caderno/blob/main/Git%20e%20GitHub/Anota%C3%A7%C3%B5es/testeDeArquivo.Rmd)

## Conclusão

R Markdown facilita a criação de relatórios reprodutíveis com R.

> Quando você renderiza este documento (por exemplo, usando o RStudio), o código R é executado e o resultado é inserido no documento HTML gerado.

## Documentação para explorar 🔍:
[BookDown - R Markdown](https://bookdown.org/yihui/rmarkdown/html-document.html)
