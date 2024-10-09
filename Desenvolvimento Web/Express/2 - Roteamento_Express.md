# Roteamento no servidor Express

Um aspecto importante da configuração do servidor Express é definir as rotas que serão usadas na aplicação. O roteamento no Express é feito por meio dos métodos HTTP, que correspondem a ações que podem ser realizadas em uma determinada rota. Alguns dos métodos HTTP mais comuns são GET, POST e DELETE.

## Definindo uma rota

Para definir uma rota no servidor Express, utiliza-se o método correspondente ao método HTTP que será utilizado para acessar essa rota. Por exemplo, para definir uma rota que responda a solicitações HTTP GET na rota `/usuarios`, utilizamos o método `app.get()`:

```javascript
app.get('/usuarios', (req, res) => {
  // Lógica para buscar usuários no banco de dados
  // ...
  res.send('Lista de usuários');
});
```

Nesse exemplo, estamos definindo uma rota `/usuarios` que responde a solicitações HTTP GET. Quando essa rota é acessada, a lógica dentro da função de callback é executada. Nesse caso, estamos retornando a mensagem "Lista de usuários" como resposta para a solicitação.

## Recebendo parâmetros de rota

Além de definir rotas fixas, o Express também permite receber parâmetros nas rotas. Por exemplo, podemos definir uma rota que receba o ID de um usuário na URL e retorne informações específicas desse usuário. Para fazer isso, utilizamos o caractere `:` seguido do nome do parâmetro na definição da rota:

```javascript
app.get('/usuarios/:id', (req, res) => {
  const id = req.params.id;
  // Lógica para buscar informações do usuário com o ID informado
  // ...
  res.send(`Informações do usuário ${id}`);
});
```

Nesse exemplo, estamos definindo uma rota `/usuarios/:id` que recebe um parâmetro `id` na URL. Quando essa rota é acessada, a lógica dentro da função de callback é executada e o valor do parâmetro `id` é recuperado por meio da propriedade `params` do objeto `req`. Em seguida, a lógica busca as informações do usuário com o ID informado e retorna uma mensagem com essas informações.

## Conclusão

O roteamento no servidor Express é feito por meio dos métodos HTTP, que correspondem a ações que podem ser realizadas em uma determinada rota. Para definir uma rota, utiliza-se o método correspondente ao método HTTP que será utilizado para acessar essa rota. O Express também permite receber parâmetros nas rotas, o que permite criar rotas dinâmicas que respondem a solicitações com base nos valores informados na URL.
