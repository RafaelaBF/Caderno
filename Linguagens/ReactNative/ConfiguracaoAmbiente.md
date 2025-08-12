# Configuração do Ambiente de Desenvolvimento

Antes de iniciar o desenvolvimento com React Native, é essencial configurar corretamente o ambiente de trabalho. Essa configuração garante que todas as ferramentas necessárias estejam disponíveis e funcionando de forma integrada, permitindo que você crie, execute e teste seus aplicativos com eficiência.

Existem duas abordagens principais para iniciar um projeto com React Native:

- **React Native CLI:** Ideal para quem deseja maior controle sobre o projeto e acesso direto ao código nativo. Recomendado para desenvolvedores com experiência ou que pretendem integrar funcionalidades específicas do sistema operacional.
- **Expo:** Uma ferramenta que simplifica o processo de desenvolvimento, oferecendo uma camada de abstração sobre o React Native. É excelente para prototipagem rápida e projetos que não exigem funcionalidades nativas avançadas.

## Instalação do Node.js e npm

1. Acesse o site oficial: https://nodejs.org
2. Baixe a versão **LTS (Long Term Support)**.
3. Execute o instalador e siga os passos (pode deixar as opções padrão).
4. Verifique a instalação no terminal:
   ```bash
   node -v
   npm -v
   ```

## React Native CLI / Expo 

<details>
  <summary><b>React Native CLI</b></summary>

1. Instale o CLI do React Native:
   ```bash
   npm install -g react-native-cli
   ```
2. Crie um novo projeto:
    ```bash
    npx react-native init NomeDoProjeto
   ```
3. Execute no Android:
    ```bash
    npx react-native run-android
   ```
4. Execute no iOS (macOS apenas):
    ```bash
    npx react-native run-ios
   ```
5. Configuração do Android Studio (para desenvolvimento Android):
    - Baixe e instale o Android Studio.
    - Instale o SDK do Android, configure as variáveis de ambiente necessárias.
        - No Windows:
        ```bash
        set ANDROID_HOME=C:\Users\SeuUsuario\AppData\Local\Android\Sdk
        ```
        - No macOS/Linux:
        ```bash
        export ANDROID_HOME=$HOME/Library/Android/sdk
        ```
    - Configure um emulador Android no AVD Manager.
6. Configuração do Xcode (para desenvolvimento iOS):
    - Disponível apenas em macOS.
    - Instale o Xcode pela App Store.
    - Instale as Command Line Tools:
        ```bash
        xcode-select --install
        ```

</details>

</br>

<details>
  <summary><b>Expo</b></summary>
   
1. Instale o Expo CLI:
    ```bash
    npm install -g expo-cli
    ```
2. Crie um novo projeto:
    ```bash
    npx create-expo-app NomeDoProjeto
    ```
3. Acesse o diretório do projeto:
    ```bash
    cd NomeDoProjeto
    ```
4. Inicie o projeto:
    ```bash
    npx expo start
    ```
5. Abra no celular:
    - Instale o app Expo Go no Android/iOS.
    - Escaneie o QR code exibido no terminal ou navegador.
6. Para poder rodar na web, instale o [metro](#o-que-é-):
    ```bash
    npx expo install react-dom react-native-web @expo/metro-runtime
    npm run web
    ``` 
  
</details>

## Empacotamento (bundler) 

O que é Empacotamento em [Estrutura e Arquitetura](ReactNative/EstruturaArquitetura.md#empacotamento-bundler)

Possiveis Empacotamentos:

<details>
  <summary><b>Webpack</b></summary>

Uma das ferramentas mais populares para empacotamento de módulos JavaScript. Ele é amplamente utilizado em projetos web modernos para transformar, otimizar e agrupar arquivos como JavaScript, CSS, imagens e outros recursos em bundles que podem ser carregados eficientemente pelo navegador ou ambiente de execução.

### **Principais Características do Webpack 5**

### 🔧 Modularidade
Webpack trata cada arquivo como um **módulo**. Isso permite importar e exportar funcionalidades entre arquivos de forma organizada e reutilizável.

### ⚡ Performance
Webpack 5 introduziu melhorias significativas de desempenho, como:
- **Caching inteligente**
- **Tree Shaking** aprimorado (remoção de código não utilizado)
- **Code Splitting** nativo (divisão de bundles para carregamento sob demanda)

### 🧩 Plugins e Loaders
Permite transformar arquivos com **loaders** (ex: Babel, TypeScript, CSS) e estender funcionalidades com **plugins** (ex: otimização, geração de HTML, limpeza de diretórios).

### 🌐 Module Federation
Uma das maiores novidades do Webpack 5. Permite que diferentes aplicações compartilhem módulos em tempo de execução, viabilizando arquiteturas de **microfrontends** e **integração dinâmica** entre projetos.

### **Webpack 5 no React Native**

Por padrão, o React Native usa o **Metro Bundler**, mas com ferramentas como **Re.Pack**, é possível substituir o Metro por Webpack 5. Isso traz vantagens como:

- Suporte a **Module Federation**
- Maior controle sobre o processo de bundling
- Integração com o ecossistema web (plugins, loaders)
- Melhor desempenho com bundlers alternativos como **Rspack**

### **Quando Usar Webpack 5 com React Native**

- Projetos grandes e modulares
- Necessidade de compartilhamento de código entre apps
- Uso de microfrontends
- Customizações avançadas no processo de build

</details> 
</br>
<details>
  <summary><b>Re.Pack</b></summary>

### O que é Re.Pack?
Re.Pack é uma ferramenta moderna de empacotamento (bundler) para aplicações React Native, desenvolvida pela Callstack. Ele substitui o bundler padrão do React Native, o Metro, e traz o poder do Webpack e Rspack para o ambiente mobile.

Seu principal objetivo é oferecer uma solução mais flexível e escalável para projetos React Native, especialmente aqueles de grande porte ou que utilizam arquiteturas avançadas como microfrontends e Module Federation.

### Principais Vantagens
- **Substituição direta do Metro:** Pode ser integrado com um único comando, sem necessidade de grandes mudanças estruturais .
- **Suporte a Webpack e Rspack:** Permite usar todo o ecossistema de plugins e loaders do Webpack, além de aproveitar o desempenho superior do Rspack (baseado em Rust).
Code Splitting: Permite dividir o bundle em partes menores, carregadas sob demanda, reduzindo o tempo de inicialização e consumo de memória.
- **Module Federation:** Suporte completo à arquitetura de microfrontends, permitindo que diferentes partes do app sejam desenvolvidas e atualizadas de forma independente.
- **DevTools avançado:** Inclui suporte a Hot Module Replacement, Fast Refresh, debugging com breakpoints, profiling de memória e CPU.
- **Redução no tamanho do app:** Utiliza técnicas como Tree Shaking para gerar bundles menores e mais eficientes.

### Como Integrar ao Projeto
1. Instalação das dependências:
    ```bash
    npm install -D @callstack/repack babel-loader swc-loader terser-webpack-plugin webpack @types/react
    ```
2. Configuração do React Native CLI: No arquivo react-native.config.js:
    ```js
    module.exports = {
      commands: require('@callstack/repack/commands'),
    };
    ```
3. Atualização dos scripts no package.json:
    ```json
    {
      "scripts": {
        "start": "react-native webpack-start"
      }
    }
    ```
4. Criação do arquivo de configuração do Webpack: `
    - Crie `webpack.config.mjs` na raiz do projeto com as configurações desejadas.
5. Configuração para Android e iOS:
    - Android: Atualize app/build.gradle com:
      ```groovy
      project.ext.react = [
        enableHermes: true,
        bundleCommand: "webpack-bundle"
      ]
      ```
    - iOS: No Xcode, adicione:
      ```bash
      export BUNDLE_COMMAND=webpack-bundle
      ```
6. Gerenciamento de módulos dinâmicos: 
    - Use `ScriptManager` para carregar chunks locais e remotos com suporte a cache e carregamento sob demanda.

### Quando Usar
Re.Pack é recomendado para desenvolvedores experientes que desejam maior controle sobre o processo de bundling e precisam de funcionalidades avançadas como:

- Aplicações grandes e modulares
- Microfrontends
- Otimizações de desempenho
- Integração com ferramentas do ecossistema Webpack

Para projetos simples ou iniciantes, o Metro ainda é a melhor escolha por sua simplicidade e menor curva de aprendizado.

### Documentação 

[re-pack](https://re-pack.dev/)

</details>
</br>
<details>
  <summary><b>Webpack 5 + Re.Pack</b></summary>

### 🧠 Webpack 5: O motor de empacotamento
O **Webpack 5** é um bundler altamente configurável que transforma e agrupa os arquivos do projeto (JavaScript, CSS, imagens, etc.) em bundles otimizados para execução. Ele oferece recursos avançados como:

- **Module Federation** (compartilhamento de módulos entre apps)
- **Code Splitting** (divisão de código para carregamento sob demanda)
- **Tree Shaking** (remoção de código não utilizado)
- **Caching inteligente** e otimizações de performance

### 🚀 Re.Pack: A ponte para React Native
O **Re.Pack** é uma ferramenta que **integra o Webpack 5 ao React Native**, substituindo o bundler padrão (Metro). Ele adapta o Webpack para funcionar com o ambiente mobile, permitindo que você aproveite todos os recursos avançados do Webpack **dentro de um app React Native**.

### 🧩 O que eles fazem juntos?

Quando usados em conjunto:

| Componente | Função |
|------------|--------|
| **Webpack 5** | Realiza o empacotamento do código com recursos avançados |
| **Re.Pack** | Adapta o Webpack para funcionar com React Native, gerando bundles compatíveis com Android/iOS |
| **Resultado** | Um app React Native com arquitetura modular, carregamento dinâmico, melhor performance e escalabilidade |

### 🏗️ Impacto na Arquitetura

Usar Webpack 5 com Re.Pack permite:

- **Arquitetura de Microfrontends**: Com Module Federation, diferentes partes do app podem ser desenvolvidas e implantadas separadamente.
- **Carregamento sob demanda**: Componentes são carregados apenas quando necessários, reduzindo o tempo de inicialização.
- **Atualizações independentes**: Você pode atualizar partes do app sem recompilar tudo.
- **Compartilhamento de código entre apps**: Ideal para apps que compartilham funcionalidades (ex: apps bancários com módulos de cartão, crédito, investimentos).

### 🆚 Comparação com Metro

| Recurso | Metro | Webpack 5 + Re.Pack |
|--------|-------|----------------------|
| Configuração | Simples | Avançada |
| Performance | Boa | Excelente (com Rspack) |
| Modularidade | Limitada | Alta (Module Federation) |
| Code Splitting | Não nativo | Nativo |
| Plugins | Limitado | Ecossistema Webpack completo |

</details>
</br>
<details>
  <summary><b>Metro Bundler</b></summary>

### O que é Metro?
É o empacotador (bundler) padrão utilizado pelo React Native. Ele é responsável por transformar o código JavaScript e os assets da aplicação em um formato que pode ser interpretado pelo ambiente nativo do app. O Metro foi desenvolvido especificamente para atender às necessidades do React Native, com foco em desempenho, simplicidade e integração direta com o ecossistema mobile.

### Como Funciona

- **Transformação de código**: Metro lê os arquivos JavaScript, aplica transformações (como Babel), e gera um bundle que será carregado pelo app.
- **Hot Reload e Fast Refresh**: Permite que alterações no código sejam refletidas instantaneamente no app durante o desenvolvimento.
- **Watch Mode**: Monitora alterações nos arquivos e recompila automaticamente.
- **Asset bundling**: Também empacota imagens, fontes e outros recursos estáticos.

### Integração com React Native
O Metro já vem integrado por padrão quando você cria um projeto com o React Native CLI:

```bash
npx react-native init MeuProjeto
npx react-native start
```

O comando `start` inicia o servidor do Metro, que escuta as mudanças no código e serve o bundle para o app em execução (emulador ou dispositivo físico).

### Vantagens do Metro

- **Simplicidade**: Não requer configuração adicional para começar a usar.
- **Desempenho otimizado para React Native**: Focado em empacotar rapidamente projetos mobile.
- **Integração nativa**: Funciona perfeitamente com Android Studio, Xcode e ferramentas do React Native.
- **Suporte oficial**: Mantido pela equipe do React Native, garantindo compatibilidade com novas versões.

### Limitações

- **Pouca flexibilidade**: Não permite customizações avançadas como Webpack ou Rspack.
- **Sem suporte nativo a Module Federation ou Code Splitting**: Funcionalidades avançadas de arquitetura não são suportadas diretamente.
- **Menor controle sobre o processo de bundling**: Ideal para projetos simples, mas pode ser limitante em aplicações complexas.

### Documentação 

- [metro](https://metrobundler.dev/)
- [metro no react native](https://reactnative.dev/docs/metro)

</details>
