# Estrutura e Arquitetura

Enquanto o React renderiza componentes para o Document Object Model (DOM) em aplicações web, o React Native transpila esses componentes em elementos nativos de plataformas móveis. 

O núcleo do React Native é formado por três partes principais: **Bridge** (Ponte), **Componentes Nativos** e **APIs de Plataforma**.

## Bridge

Conceitos centrais do React Native e permite a **comunicação entre o código JavaScript e os componentes nativos** do sistema operacional (iOS ou Android). Ela serve como uma ponte bidirecional que permite que o JavaScript e os módulos nativos se comuniquem de forma assíncrona. Isso significa que os desenvolvedores podem escrever a lógica do aplicativo em JavaScript, mas o renderizador final dos elementos é nativo.

O código JavaScript é executado em uma thread separada, chamada de JavaScript thread, enquanto os componentes e APIs nativos são executados na Native thread.

> ### Thread
> É a menor unidade de processamento que pode ser executada de forma independente por um sistema operacional. Assim, uma thread é parte de um processo, que é o programa em execução, e cada processo pode ter uma ou várias threads, compartilhando os mesmos recursos e memória.

A Bridge faz a intermediação da comunicação entre essas threads, traduzindo comandos e dados do JavaScript para instruções nativas e vice-versa.

> Explorar mais sobre o assunto: https://medium-com.translate.goog/@antoniogally/exploring-react-natives-architectures-bridge-and-beyond-76e414accf7d?_x_tr_sl=en&_x_tr_tl=pt&_x_tr_hl=pt&_x_tr_pto=tc

## Componentes Nativos

Fornece e que correspondem diretamente aos **widgets nativos de cada plataforma**. Por exemplo, um do React Native é renderizado como um UILabel em iOS e um TextView em Android. 

Ainda, se o desenvolvedor precisar de funcionalidades que não estão incluídas nos componentes padrão do React Native (realizar algum tipo de customização), ele pode criar componentes personalizados em código nativo (Swift/Objective-C para iOS e Java/Kotlin para Android) e conectá-los ao código JavaScript.

## APIs de Plataforma

São módulos que o React Native **disponibiliza para acessar funcionalidades específicas do dispositivo**, como geolocalização, câmera, armazenamento de dados e sensores. Isso significa que os aplicativos podem fazer uso de funcionalidades avançadas sem a necessidade de bibliotecas de terceiros.

Quando funcionalidades específicas não são fornecidas pelo núcleo do React Native, os **desenvolvedores podem usar módulos de código aberto ou criar seus próprios módulos nativos para integrar essas funcionalidades** ao aplicativo. Esses módulos são escritos nas linguagens nativas de cada plataforma (Objective-C/Swift para iOS e Java/Kotlin para Android) e são chamados de forma assíncrona pelo JavaScript através da Bridge.

## Integração

Essas três partes (Bridge, Componentes Nativos e APIs de Plataforma) trabalham em conjunto para formar a base de desenvolvimento do React Native. O JavaScript é usado para escrever a lógica de interface e comportamento da aplicação. A Bridge faz a comunicação entre essa lógica e os Componentes Nativos, que são renderizados na Native UI de cada plataforma. As APIs de Plataforma permitem que os desenvolvedores acessem funcionalidades específicas de dispositivos, ampliando as capacidades dos aplicativos.

Essa arquitetura híbrida é o que diferencia o React Native de frameworks que utilizam WebView, pois ela permite uma experiência de usuário mais fluida e a criação de aplicativos que realmente se comportam como aplicativos nativos, mantendo a produtividade e o uso de uma única base de código para múltiplas plataformas.

Algumas das APIs de plataforma mais usadas incluem a Geolocation API para localização, a CameraRoll para acessar fotos e vídeos, e a AsyncStorage para armazenamento local de dados.

## Arquitetura de arquivos

- **assets**: Armazena recursos estáticos como imagens, fontes, ícones e outros arquivos multimídia que a aplicação pode usar.
- **node_modules**: Pasta gerada automaticamente pelo npm ou yarn que contém todas as dependências e pacotes externos que o projeto utiliza.
- **App.js**: Arquivo principal da aplicação onde o componente raiz do aplicativo é definido. Este arquivo contém o código que inicia a aplicação e pode conter a lógica de renderização da interface.
- **app.json**: Arquivo de configuração da aplicação, usado principalmente em projetos React Native para definir parâmetros como nome do projeto, ícone, tela de carregamento (splash) e outras configurações de metadados.
- **index.js**: Ponto de entrada da aplicação. É o arquivo que inicializa a aplicação e renderiza o componente principal (geralmente App.js) na tela.
- **package-lock.json**: Arquivo que bloqueia as versões exatas das dependências instaladas, garantindo que a instalação das dependências seja consistente em todas as máquinas.
- **package.json**: Arquivo de configuração que contém informações sobre o projeto, como nome, versão, autor, scripts de comando, dependências e metadados. Ele é usado pelo npm ou yarn para gerenciar pacotes e scripts do projeto.

## Empacotamento (bundler) 

O empacotamento, em termos gerais, é a prática de combinar vários arquivos em um único pacote ou arquivo maior. No contexto do React Native, isso significa que o "bundle" resultante conterá todo o código necessário para executar o aplicativo, como: 

- **Código JavaScript:** O código da aplicação React Native, incluindo componentes, lógica e funcionalidades.
- **Recursos:** Imagens, ícones, fontes e outros recursos usados no aplicativo.
- **Bibliotecas:** Pacotes de terceiros e dependências usadas no aplicativo.

### Por que o Empacotamento é Importante no React Native?

- **Otimização:** O processo de empacotamento otimiza o código e os recursos para reduzir o tamanho do arquivo e melhorar o tempo de carregamento. 
- **Desempenho:** Um bundle bem otimizado garante que o aplicativo seja executado mais rapidamente e com menos recursos no dispositivo móvel. 
- **Facilidade de Implantação:** O bundle facilita a distribuição e implantação do aplicativo, pois ele contém tudo o que é necessário para executar o app em diferentes plataformas (Android e iOS). 
- **Segurança:** Em alguns casos, o empacotamento pode ajudar a ofuscar o código, tornando-o mais difícil de ser inspecionado e copiado por terceiros

### Processo de Empacotamento:

1. **Iniciando o Servidor de Desenvolvimento:**
    - O servidor de desenvolvimento do React Native (geralmente executado com `react-native start`) é responsável por gerenciar o processo de empacotamento em tempo real durante o desenvolvimento.
2. **Gerando o Bundle:**
    - Quando você executa o comando para construir o aplicativo (por exemplo, `react-native run-android` ou `react-native run-ios`), o bundler cria o pacote otimizado com base no seu código e configurações.

## Exercícios de revisão

### Questão 01
O que o React Native utiliza para acessar funcionalidades de hardware?

<ol type="A">
  <li>Native Threads</li>
  <li>Modificadores CSS</li>
  <li>APIs de Plataforma</li>
  <li> WebView</li>
  <li>Virtual DOM</li>
</ol>
<details>
  <summary><b>Resposta</b></summary>

**c. APIs de Plataforma**

*Explicação:*

O React Native utiliza APIs de plataforma para acessar funcionalidades de hardware, como:
Câmera, GPS/localização, Acelerômetro, Bluetooth, Sensores de proximidade, Armazenamento local, Microfone, entre outros.

Essas APIs podem ser acessadas por meio de módulos nativos já disponíveis ou criados sob medida, e o React Native faz a ponte entre o código JavaScript e o código nativo (Java/Kotlin para Android, Objective-C/Swift para iOS).

As outras alternativas não se aplicam:

a. Native Threads – são usadas internamente, mas não diretamente para acessar hardware.</br>
b. Modificadores CSS – não existem em React Native; o estilo é feito com objetos JavaScript.</br>
d. WebView – serve para renderizar conteúdo web, não para acessar hardware.</br>
e. Virtual DOM – é usado no React (web), mas o React Native não usa Virtual DOM.

</details>

### Questão 02
A Bridge no React Native permite o quê?

<ol type="A">
  <li>Manipulação de WebView</li>
  <li>Criação de novos elementos HTML</li>
  <li>Renderização direta de interfaces no DOM</li>
  <li>Execução síncrona de threads nativas</li>
  <li>Comunicação entre código JavaScript e nativo</li>
</ol>
<details>
  <summary><b>Resposta</b></summary>

**e. Comunicação entre código JavaScript e nativo**

*Explicação:*

A Bridge (ou ponte) no React Native é o mecanismo que permite a comunicação entre o código JavaScript e o código nativo (Java/Kotlin para Android e Objective-C/Swift para iOS). Essa ponte é essencial para que o React Native possa acessar funcionalidades nativas da plataforma, como sensores, câmera, GPS, entre outros.

As outras alternativas não se aplicam:

a. Manipulação de WebView – é uma funcionalidade específica, não relacionada diretamente à Bridge.<br>
b. Criação de novos elementos HTML – React Native não usa HTML; ele utiliza componentes nativos.<br>
c. Renderização direta de interfaces no DOM – o DOM é exclusivo da web, não usado em React Native.<br>
d. Execução síncrona de threads nativas – a comunicação via Bridge é assíncrona por padrão.

</details>

### Questão 03
O React Native transpila componentes em quê?

<ol type="A">
  <li>Elementos nativos de plataformas móveis</li>
  <li>WebView</li>
  <li>HTML e CSS</li>
  <li>Renderizadores genéricos</li>
  <li>Document Object Model (DOM)</li>
</ol>
<details>
  <summary><b>Resposta</b></summary>

**a. Elementos nativos de plataformas móveis**

*Explicação:*

O React Native transpila os componentes escritos em JavaScript para elementos nativos das plataformas móveis (Android e iOS). Isso significa que, ao invés de renderizar uma interface web, ele utiliza os componentes nativos da plataforma, proporcionando melhor desempenho e experiência de usuário.

As outras alternativas não se aplicam:

b. WebView – é usada para exibir conteúdo web, não para renderizar componentes do React Native.<br>
c. HTML e CSS – não são utilizados diretamente no React Native; o estilo é feito com objetos JavaScript.<br>
d. Renderizadores genéricos – não é um termo aplicável ao funcionamento do React Native.<br>
e. Document Object Model (DOM) – o DOM é exclusivo da web, enquanto o React Native usa componentes nativos.

</details>
