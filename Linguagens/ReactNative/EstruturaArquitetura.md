# Estrutura e Arquitetura

Enquanto o React renderiza componentes para o Document Object Model (DOM) em aplicações web, o React Native transpila esses componentes em elementos nativos de plataformas móveis. 

O núcleo do React Native é formado por três partes principais: **Bridge** (Ponte), **Componentes Nativos** e **APIs de Plataforma**.

## Bridge

Conceitos centrais do React Native e permite a **comunicação entre o código JavaScript e os componentes nativos** do sistema operacional (iOS ou Android). Ela serve como uma ponte bidirecional que permite que o JavaScript e os módulos nativos se comuniquem de forma assíncrona. Isso significa que os desenvolvedores podem escrever a lógica do aplicativo em JavaScript, mas o renderizador final dos elementos é nativo.

O código JavaScript é executado em uma thread separada, chamada de JavaScript thread, enquanto os componentes e APIs nativos são executados na Native thread.

> ### Thread
> É a menor unidade de processamento que pode ser executada de forma independente por um sistema operacional. Assim, uma thread é parte de um processo, que é o programa em execução, e cada processo pode ter uma ou várias threads, compartilhando os mesmos recursos e memória.

A Bridge faz a intermediação da comunicação entre essas threads, traduzindo comandos e dados do JavaScript para instruções nativas e vice-versa.

![BridgeFluxo](Imagens/BridgeFluxo.png)

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
