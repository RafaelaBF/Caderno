# Um exemplo de como utilizar o async
Usando async para esperar a resposta dos dados do firebase.

```javascript
const get = async (token, resp) => {
  admin
    .auth()
    .verifyIdToken(token)
    .then(async (decodedToken) => {
      // ...
```

A função `get` é definida como uma função assíncrona usando a palavra-chave `async`. Isso permite que possamos utilizar o `await` dentro dela para aguardar a conclusão de operações assíncronas.

Em seguida, temos a chamada de função `admin.auth().verifyIdToken(token)`. Aqui, o objeto `admin` representa uma biblioteca ou um módulo que oferece recursos de autenticação. A função `verifyIdToken` é uma função assíncrona que verifica a validade de um token de autenticação.

Utilizamos a palavra-chave `async` antes do callback da função `then` para que possamos usar `await` dentro dele. Isso nos permite esperar a conclusão da verificação do token antes de prosseguir.

```javascript
      const uid = decodedToken.uid;
      var obj = [];
      const userRecord = await admin.auth().getUser(uid);
```

Aqui, estamos obtendo o UID (identificador único) do usuário a partir do `decodedToken`, que foi retornado pela função `verifyIdToken`. O UID é armazenado na variável `uid`.

Em seguida, criamos um array vazio chamado `obj` para armazenar os resultados da consulta ao banco de dados.

A chamada `await admin.auth().getUser(uid)` busca os detalhes do usuário com base no UID. O `await` aguarda a conclusão dessa operação assíncrona antes de prosseguir.

```javascript
      const cols = ['col1', 'col2', 'col3']; // Adicione aqui as coleções que você deseja percorrer

      const promises = cols.map(async (col) => {
        const collectionRef = admin
          .firestore()
          .collection(`${userRecord}/${col}`);

        const snapshot = await collectionRef.get();

        snapshot.forEach((o) => {
          if (o.data()['data'] != null) {
            var dadosList = [col, o.data()['data']];
            obj.push(dadosList);
          }
        });
      });

      await Promise.all(promises);
```

Nesta parte do código, definimos um array chamado `cols` que contém os nomes das coleções que desejamos percorrer.

Em seguida, usamos o método `map` para iterar sobre o array `cols`. Dentro da função de callback do `map`, definimos uma função assíncrona que será executada para cada elemento `col`.

Dentro dessa função assíncrona, criamos uma referência à coleção específica com base no `col` atual. Usamos a função `await` antes de `collectionRef.get()` para aguardar a conclusão da operação assíncrona de obtenção dos documentos da coleção.

Em seguida, percorremos os documentos retornados utilizando o método `forEach` no `snapshot`. Se o campo `data` do documento não for nulo, criamos um novo array `dadosList` contendo informações relevantes e o adicionamos ao array

 `obj`.

Após o `map` terminar de executar todas as funções assíncronas, usamos `Promise.all` para aguardar a conclusão de todas as promessas retornadas pelo `map`. Isso garante que todas as consultas ao banco de dados tenham sido concluídas antes de prosseguir.

```javascript
      return resp.status(200).json(obj);
    })
    .catch((error) => {
      return resp.status(405).json(error);
    });
};
```

Por fim, exibimos o conteúdo do array `obj` no console e retornamos uma resposta com o status 200 e o array `obj` como JSON usando `resp.status(200).json(obj)`.

Se ocorrer um erro em qualquer parte do código, a função `catch` será chamada, e uma resposta com status 405 será retornada, contendo o erro como JSON.

Essas são as principais partes do código que utilizam conceitos assíncronos, como funções assíncronas, `await`, `Promise.all` e manipulação de promessas, para garantir que as operações assíncronas sejam tratadas corretamente e que a resposta seja enviada somente quando todas as consultas ao banco de dados forem concluídas.
