# Introdução ao React Native ⚛️📱

React Native é um framework de desenvolvimento de aplicativos móveis criado pelo Facebook, que permite construir aplicações para iOS e Android utilizando JavaScript e React. A principal proposta do React Native é permitir o desenvolvimento multiplataforma com uma única base de código, aproveitando o conhecimento prévio de desenvolvedores web em React.

> **Baseado em React**: React Native herda os princípios do React, como componentes reutilizáveis, estado e propriedades, e o ciclo de vida dos componentes.

> **Hot Reloading**: Uma funcionalidade que permite visualizar alterações no código em tempo real, sem precisar recompilar o aplicativo completamente, acelerando o processo de desenvolvimento.

*Link para documentação [reactnative.dev](https://reactnative.dev/docs/getting-started)*

## Index 📚
- [Estrutura e Arquitetura](EstruturaArquitetura.md)
- [Super App](SuperApp.md)
- [Configuração do Ambiente de Desenvolvimento](ConfiguracaoAmbiente.md)
- [Projetos em React Native](LinksProjetosExemplo.md)

## React Native vs Desenvolvimento Nativo 

- **Desempenho** 
    - Aplicativos desenvolvidos em Swift/Objective-C (para iOS) e Kotlin/Java (para Android) são compilados diretamente em código de máquina nativo, o que resulta em desempenho superior.  No React Nativo, a lógica da aplicação é executada em JavaScript, e a comunicação entre o JavaScript e o código nativo é feita através da Bridge. Essa comunicação pode introduzir latências em operações intensas, como cálculos complexos ou interações em tempo real.
- **Reutilização de código**
    - O desenvolvimento nativo exige que os aplicativos para iOS e Android sejam desenvolvidos separadamente. Já o React Native oferece uma única base de código em JavaScript que pode ser usada para desenvolver aplicativos para ambas as plataformas.
- **Acesso às funcionalidades nativas**
    - O desenvolvimento nativo permite acesso total às APIs do sistema, garantindo controle completo sobre recursos como câmera, sensores e notificações. Já o React Native oferece acesso parcial via bibliotecas, exigindo módulos nativos para funcionalidades específicas.

## React Native vs. Flutter
- **Linguagem de Programação**
    - O React Native utiliza JavaScript, uma linguagem amplamente conhecida, especialmente entre desenvolvedores web. Já o Flutter usa Dart, uma linguagem menos popular, o que pode representar uma curva de aprendizado adicional.
- **Arquitetura de Interface e Renderização**
    - O React Native usa uma ponte (Bridge) para comunicar o código JavaScript com os componentes nativos, o que pode gerar latência em operações complexas. O Flutter utiliza o mecanismo Skia para renderizar diretamente na tela, oferecendo desempenho mais consistente.
- **Acesso a Funcionalidades Nativas**
    - Ambos oferecem acesso a APIs nativas, mas o React Native pode exigir a criação de módulos nativos em Swift/Objective-C ou Kotlin/Java. O Flutter facilita a integração com plugins, mas também pode exigir código nativo em casos específicos.

## React Native vs. Soluções Baseadas em WebView (Cordova/Ionic)
- **Renderização da Interface**
    - O React Native renderiza componentes nativos, proporcionando uma experiência mais próxima de um app nativo. Cordova e Ionic usam WebView, renderizando a interface como uma página web dentro de um contêiner.
- **Performance**
    - O React Native oferece melhor desempenho, com interfaces mais responsivas. Já soluções baseadas em WebView podem apresentar lentidão, especialmente em dispositivos antigos ou com animações complexas.
- **Experiência do Usuário**
    - O React Native respeita as diretrizes de design nativas, garantindo uma aparência e comportamento mais naturais. Cordova/Ionic tentam imitar os componentes nativos, mas podem oferecer uma experiência menos autêntica.
