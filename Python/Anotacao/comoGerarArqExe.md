<img src="https://cdn3.iconfinder.com/data/icons/logos-and-brands-adobe/512/267_Python-512.png" width="100" align="right" style="border-radius: 15px;">

# Arquivo Executável com Python

## 🗂️ O que é um arquivo executável

Um arquivo executável é um tipo de arquivo que contém um programa executável por um computador. Diferente dos scripts Python (.py), que precisam de um interpretador para rodar, os arquivos executáveis podem ser executados diretamente pelo sistema operacional.

## 🌐 Ambiente Virtual

Um ambiente virtual é uma ferramenta que ajuda a manter dependências e bibliotecas requeridas por diferentes projetos Python isoladas umas das outras. É recomendado criar arquivos executáveis dentro de um ambiente virtual para garantir que apenas as bibliotecas necessárias sejam incluídas, tornando o arquivo mais leve e o processo mais rápido.

Utilizar o PyCharm facilita a criação desse ambiente virtual, simplificando o procedimento.

**OU**

Para criar um ambiente virtual, use o comando:

```sh
python -m venv myenv
```

Depois, ative o ambiente virtual:

- No Windows:

  ```sh
  myenv\Scripts\activate
  ```

- No MacOS/Linux:

  ```sh
  source myenv/bin/activate
  ```

## 📥 Instalar o pyinstaller

Para instalar o `pyinstaller`, execute:

```sh
pip install pyinstaller
```

## ⚙️ Gerar o arquivo executável

Para gerar um arquivo executável, use:

```sh
pyinstaller --onefile nomeArquivo.py
```

- `pyinstaller`: comando para iniciar o processo de criação do executável.
- `--onefile`: indica que todos os arquivos necessários serão empacotados em um único executável.
- `nomeArquivo.py`: nome do arquivo Python que será transformado em executável.

> P.S: Coloque o parâmetro `-w` apenas se o programa tiver uma interface gráfica (GUI) e não precisar de uma janela de console.

Exemplo para gerar um executável com mais de um arquivo:

```sh
pyinstaller --onefile --add-data "arquivo1.py;." --add-data "arquivo2.py;." nomePrincipal.py
```

- `--add-data "arquivo1.py;."`: adiciona arquivos extras necessários para o executável.
- `nomePrincipal.py`: nome do arquivo principal Python.

> OBS: O processo para transformar em um arquivo executável pode ser demorado, dependendo do tamanho do código e das bibliotecas utilizadas. Utilizar o ambiente virtual ajuda a incluir apenas as bibliotecas necessárias, evitando adicionar bibliotecas extras sem necessidade.

## 🗃️ Onde encontrar o executável

O executável será criado na pasta `dist`. Basta pegar esse executável e colocá-lo onde quiser.

> ATENÇÃO! Se seu arquivo precisa de outros arquivos (como imagens, bases de dados, etc.), mantenha-os juntos com o executável (.exe).

# Fontes dos Estudos 📚🔍

- [Como Transformar Arquivo Python em Executável ][1]
- [Arquivo executável python hashtag][2]
- [Criando um executável a partir de um programa em Python][3]

[1]: https://www.youtube.com/watch?v=cGSerUmK0CE&t=0s
[2]: https://www.hashtagtreinamentos.com/arquivo-executavel-python#bibliotecas
[3]: https://www.alura.com.br/artigos/criando-um-executavel-a-partir-de-um-programa-python
