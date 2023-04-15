# Comandos

## Manipulação de arquivos

- mkdir nome_do_diretório -> *make directory* -> cria um diretório.
- rmdir nome_do_diretório -> *remove directory* -> remove um diretório vazio.
- rm -rf dir nome_do_diretório -> *remove directory* -> remove um diretório forçadamente.
- cd nome_do_diretório -> ** -> entra no diretório.
- ls -> ** -> lista os diretório pertencentes ao diretório atual.

## Scripts
- nano nome_do_arquivo.sh -> usado para leitura de um arquivo .sh executavel.
- chmod +x nome_do_arquivo.sh -> é usado para conceder permissão de execução.
  - chmod -> é um comando utilizado para alterar as permissões de acesso de um arquivo ou diretório no sistema Linux;
  - +x -> opção que indica que a permissão de execução deve ser adicionada ao arquivo;

## Manipulação de volume lógico
- lvcreate -L 20G -n volume grupo -> é usado para criar um novo volume lógico:
  - lvcreate -> o comando utilizado para criar o volume lógico;
  - -L 20G ->  opção para especificar o tamanho do volume lógico, neste caso, 20 gigabytes;
  - -n volume -> opção para definir um nome para o novo volume lógico, neste caso, "volume";
  - grupo -> nome do grupo de volume onde o novo volume será criado. 

> Um grupo de volume é um conjunto de discos que são agrupados e gerenciados como uma unidade.

## Administrador
O adm do linux é o sudo, quando se quer ter poder de adm a algum comando basta iniciar-lo com **sudo**.

su - -> passa para o usuario root.
