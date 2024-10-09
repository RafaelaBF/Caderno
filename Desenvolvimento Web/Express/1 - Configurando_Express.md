# Configurando um servidor Express

O **Express** é um framework para Node.js que permite criar servidores web de maneira rápida e simples. A configuração de um servidor Express envolve a instalação do pacote do NPM e a criação de um arquivo de configuração para definir as rotas e a lógica do servidor.

## Instalando o pacote do NPM

Para instalar o pacote do NPM do Express, basta executar o seguinte comando no terminal:

~~~bach
npm install express
~~~
Esse comando instala o pacote `express` e suas dependências no diretório `node_modules` do seu projeto.

## Criando um arquivo de configuração

Para criar um servidor Express, é necessário criar um arquivo de configuração que define as rotas e a lógica do servidor. Um exemplo de arquivo de configuração pode ser o seguinte:

~~~javaScript
const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Olá, mundo!');
});

app.listen(3000, () => {
  console.log('Servidor iniciado na porta 3000');
});
~~~

Nesse exemplo, o arquivo de configuração define um servidor que responde com a mensagem "Olá, mundo!" quando recebe uma solicitação HTTP GET na rota raiz (/). Ele também inicia o servidor na porta 3000.

Vamos analisar linha por linha do código:

- `const express = require('express');:` essa linha importa o pacote express.
- `const app = express();:` essa linha cria um objeto app que representa o servidor Express.
- `app.get('/', (req, res) => {...});:` essa linha define uma rota para solicitações HTTP GET na rota raiz (/). Quando essa rota é acessada, o servidor responde com a mensagem "Olá, mundo!".
- `app.listen(3000, () => {...});:` essa linha inicia o servidor na porta 3000 e exibe uma mensagem no console quando o servidor é iniciado.

## Conclusão

A configuração de um servidor Express envolve a instalação do pacote do NPM e a criação de um arquivo de configuração que define as rotas e a lógica do servidor. O exemplo apresentado neste texto mostra como criar um servidor Express simples que responde com a mensagem "Olá, mundo!" na rota raiz (/).
