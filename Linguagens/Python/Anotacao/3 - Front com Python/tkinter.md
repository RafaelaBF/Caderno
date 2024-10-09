<img src="https://storage.googleapis.com/replit/images/1619744706953_a11b5e0a6acf250ac95d9b46d5a2673f.jpeg" width="70" align="right" style="border-radius: 15px;">

# Introdução ao Tkinter !
 
## 📦 O que é o tkinter?

O `tkinter` é a biblioteca padrão do Python para a criação de interfaces gráficas (GUIs). Ela permite a criação de aplicativos com janelas, botões, textos, e outros elementos de forma fácil e rápida.

## 📥 Instalar o tkinter

Para instalar o tkinter, execute:

```sh
pip install tk
```

## 🛠️ Importar o tkinter

```python
from tkinter import *
```

## 🚀 Inicializar o TK no código

```python
janela = Tk()  # Inicializar o TK

# Código do programa

janela.mainloop()  # Manter a janela aberta mesmo após a execução
```

## 📝 Modificando o título da janela

```python
janela.title("Título")
```

## 🖊️ Adicionando um texto

```python
texto = Label(janela, text="O texto")
```

## 🎨 Ajustando estilo de elementos

```python
texto.grid(column=0, row=0, padx=10, pady=10)
```

`column` e `row` -> posição do elemento; `padx` e `pady` -> padding do elemento

## 🔘 Adicionando um botão

```python
botao = Button(janela, text="Clique aqui!", command=onClick)
```

`onClick` será uma função dentro do código que será chamada ao clicar no botão.

## 🖥️ Código de exemplo

Código que mostra a cotação do dólar, euro e bitcoin:

```python
import requests
from tkinter import *

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto_resposta['text'] = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

janela = Tk()
janela.title("Cotação Atual de Moedas")
texto = Label(janela, text="Clique no botão para ver as cotações de moedas")
texto.grid(column=0, row=0, padx=10, pady=10)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes)
botao.grid(column=0, row=1, padx=10, pady=10)

texto_resposta = Label(janela, text="")
texto_resposta.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()
```

# Fontes dos Estudos 📚🔍

- [Como Criar uma Tela em Python Para Seus Códigos][1]
- [Documentação tkinter][2]

[1]: https://www.youtube.com/watch?v=AiBC01p58oI
[2]: https://docs.python.org/pt-br/3/library/tkinter.html#a-hello-world-program