 # Conceitos básicos de PHP
 
> " O que distingue o PHP de algo como o JavaScript no lado do cliente é que o código é executado no servidor, gerando o HTML que é então enviado para o    navegador. O navegador recebe os resultados da execução desse script, mas não sabe qual era o código-fonte (PHP)." - (PHP, s.d.)

Desse jeito o php levou dinamismo às páginas Web. Isso porque, com essa linguagem, é possível adicionar recursos como consulta a banco de dados, processamento e tratamento de dados e consumo de recursos externos, como APIS, entre tantas outras possibilidades.
 
Um script PHP deve ser desenvolvidos em arquivos com a extensão `.php` . Dentro desse arquivo podemos escrever os codigos dentro das tag:
 ~~~php
<?php
// Código
?>
~~~
Isso é necessário para que o servidor Web entenda qual código deve ser interpretado e qual deve ser apenas renderizado, uma vez que tags HTML podem ser inseridas dentro de um arquivo contendo código PHP. Junto do mesmo arquivo também podemos usar dessa forma a linguagem de marcação HTML:
 ~~~php
<?php
// Código
?>
<html>
<!--Código-->
</html>
~~~

> As instruções PHP devem ser, obrigatoriamente, terminadas com a utilização de ponto e vírgula. Logo, ao final de cada comando, devemos indicar que ele foi terminado.

## Variáveis

As variáveis em PHP são declaradas com um simbulo `$`. Também não é nescessario a declaração do tipo da variável.
> OBS: Os nomes de variável são case-sensitive. Logo, há diferença entre letras maiúsculas e minúsculas.
 ~~~php
<?php
$variavel1 = 10;
$Variavel1 = 3;
$_variavel1 = "texto";
?>
~~~
> Em PHP, as variáveis não inicializadas possuem um valor padrão. Nas do tipo booleano, por exemplo, o valor padrão é false. Logo, é recomendado – e também uma boa prática − inicializar as variáveis antes de utilizá-las, embora isso não seja obrigatório.

Como a linguagem php é utilizada principalmente para receber dados do HTML e processa-los, temos nela 3 variaveis globais que saõ responsaveis por receber os dados do HTTP vindo do HTML. São elas:
~~~php
<?php
$_GET["var"] // Recebe os dados transmitidos atraves do get
$_POST["var"] // Recebe os dados transmitidos atraves do post
$_REQUEST["var"] // Recebe os dados transmitidos atraves do get e dos post (coringa)
?>
~~~
Todas elas são do tipo ARRAY.

