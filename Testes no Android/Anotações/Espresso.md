# Espresso
**Definição oficial:** O Espresso cria testes concisos, bonitos e confiáveis para a IU do Android. - [Documentação Espresso][1]

## Sintaxe

Código         | Definição
-------------  | ----------------------------------------------------------------
onView()       | Pega um view
withId()       | Acha um id
perform()      | Executa uma ação
typeText()     | Escreve um texto
check()        | Checa algo
matches()      | Corresponder a uma exibição usando diferentes atributos
hasErrorText() | Se há uma mensagem de erro igual
withText()     | Se o campo tem o texto igual


### Exemplos
~~~ktk
onView(withId(R.id.o_id)).perform(click()) → clica no elemento com o id “o_id”.
~~~
~~~ktk
onView(withId(R.id.o_id)).perform(typeText(“Um texto)) → Escreve no campo com o id “o_id”
~~~
~~~ktk
onView(withId(R.id.o_id)).check(matches(hasErrorText("Texto Erro"))) → Checa se a há mensagem de erro com esse texto
~~~
~~~ktk
onView(withId(R.id.o_id)).check(matches(withText("Texto"))) → Checa se o valor do campo é igual há esse texto
~~~

[1]: https://developer.android.com/training/testing/espresso
[2]: https://www.tutorialspoint.com/espresso_testing/index.htm
[3]: https://medium.com/@heitorcolangelo/testes-no-android-com-espresso-parte-1-8d739672a235
