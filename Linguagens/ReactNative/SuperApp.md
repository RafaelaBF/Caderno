# Super app
Um **Super App** é uma aplicação móvel que oferece múltiplos serviços e funcionalidades integradas em uma única interface. Em vez de ser apenas um app com uma função específica, ele atua como uma **plataforma central** que pode incluir:

- Pagamentos
- Compras
- Transporte
- Comunicação
- Serviços bancários
- Entretenimento

Exemplos famosos incluem **WeChat**, **Grab**, **Paytm** e **Rappi**.

## Como funciona o conceito de Super App no React Native?

No contexto do **React Native**, o conceito de Super App pode ser implementado de forma eficiente usando uma arquitetura **modular e escalável**, onde diferentes funcionalidades são desenvolvidas como **mini aplicativos independentes** (microfrontends ou MFEs) e integradas dinamicamente ao app principal.

Essa abordagem é viabilizada por tecnologias como:

- **Module Federation**: Permite que cada funcionalidade seja carregada sob demanda e atualizada independentemente.
- **Webpack 5**: Gerencia o empacotamento dos módulos com recursos avançados como code splitting e caching.
- **Re.Pack**: Adapta o Webpack para funcionar com React Native, substituindo o Metro Bundler e permitindo o uso de Module Federation.

## Benefícios de usar essa arquitetura em um Super App

| Benefício | Descrição |
|----------|-----------|
| **Escalabilidade** | Cada módulo pode ser desenvolvido por uma equipe diferente. |
| **Modularidade** | Funcionalidades como pagamentos, chat, delivery, etc., são separadas. |
| **Atualizações independentes** | Um módulo pode ser atualizado sem afetar o restante do app. |
| **Desempenho otimizado** | Módulos são carregados apenas quando necessários. |
| **Reutilização de código** | Módulos podem ser compartilhados entre diferentes apps. |

## Exemplo de Estrutura de um Super App com React Native

- **Host App**: Interface principal e navegação.
- **Módulo de Pagamentos**: Carregado sob demanda via Module Federation.
- **Módulo de Delivery**: Desenvolvido por outra equipe, hospedado remotamente.
- **Módulo de Chat**: Compartilhado com outro app da empresa.
- **Módulo de Investimentos**: Atualizado separadamente, com deploy independente.

## Module Federation

### O que é Module Federation?

**Module Federation** é um padrão arquitetural introduzido no **Webpack 5** que permite que diferentes aplicações JavaScript compartilhem módulos entre si em tempo de execução[1](https://module-federation.io/guide/start/). Ele é especialmente útil em arquiteturas de **microfrontends**, onde grandes aplicações são divididas em partes menores e independentes, desenvolvidas e implantadas separadamente.

#### Principais funcionalidades:
- **Compartilhamento de código** entre múltiplas aplicações sem duplicação.
- **Carregamento dinâmico** de módulos remotos.
- **Atualizações independentes** de partes da aplicação.
- **Redução de tamanho do bundle** e melhoria na performance.
- **Suporte a múltiplos bundlers** como Webpack e Rspack.

### Module Federation no React Native com Re.Pack

No contexto do **React Native**, o uso de Module Federation é viabilizado por ferramentas como o **Re.Pack**, que substitui o Metro Bundler e traz suporte ao Webpack e Rspack [2](https://www.callstack.com/open-source/re-pack).

#### Como funciona:
- A aplicação é dividida em:
  - **Host App**: carrega e consome módulos remotos.
  - **Remote Apps (MFEs)**: expõem componentes ou funcionalidades que podem ser carregadas pelo host.
- Os módulos são carregados dinamicamente usando `React.lazy()` e `Suspense`, com suporte ao `ScriptManager` para resolver e baixar os scripts remotos [3](https://dev.to/callstackengineers/how-to-use-module-federation-with-repack-3-555b).

#### Exemplo de uso:
```tsx
const MiniApp = React.lazy(() => Federated.importModule('MiniApp', './App'));

<Suspense fallback={<Text>Carregando... />}>
  <MiniApp />
</Suspense>
```

#### Configuração via Re.Pack:
```js
new Repack.plugins.ModuleFederationPlugin({
  name: 'HostApp',
  remotes: {
    MiniApp: 'MiniApp@http://localhost:9001/MiniApp.container.js.bundle',
  },
  shared: {
    react: { singleton: true, eager: true },
    'react-native': { singleton: true, eager: true },
  },
});
```

### Vantagens na Arquitetura

- **Escalabilidade**: Permite que múltiplas equipes trabalhem em partes diferentes do app sem conflitos.
- **Modularidade**: Cada mini-app pode ser desenvolvido, testado e implantado de forma independente.
- **Atualizações dinâmicas**: É possível atualizar funcionalidades específicas sem precisar recompilar ou republicar o app inteiro.
- **Performance otimizada**: Carregamento sob demanda reduz o tempo de inicialização e uso de memória.

### Alternativas

- **Monorepo com Metro**: Estrutura tradicional com múltiplos pacotes, mas sem carregamento dinâmico.
- **Expo Modules**: Compartilhamento de funcionalidades via pacotes, mas com menos flexibilidade.
- **Haul**: Bundler alternativo baseado em Webpack, menos usado atualmente.
- **Native Federation**: Variante do Module Federation com suporte a múltiplos bundlers (Webpack, Vite, Rspack) [4](https://docs.zephyr-cloud.io/recipes/repack-mf).


## 🔗 Module Federation + Webpack 5 + Re.Pack: O que fazem juntos?

### 🧠 Webpack 5
É o **motor de empacotamento**. Ele transforma e agrupa os arquivos do projeto (JavaScript, imagens, estilos etc.) em bundles otimizados. Com Webpack 5, você ganha acesso a recursos avançados como:

- **Module Federation**
- **Code Splitting**
- **Tree Shaking**
- **Caching inteligente**

### 🧩 Module Federation
É uma **funcionalidade do Webpack 5** que permite que diferentes aplicações compartilhem módulos entre si **em tempo de execução**. Isso viabiliza:

- **Microfrontends**: cada parte do app pode ser desenvolvida e implantada separadamente.
- **Atualizações independentes**: sem recompilar o app inteiro.
- **Carregamento dinâmico**: módulos são carregados sob demanda.

### 🚀 Re.Pack
É a **ferramenta que conecta o Webpack 5 ao React Native**. Ele substitui o Metro Bundler e adapta o Webpack para funcionar com Android e iOS. Com Re.Pack, você pode:

- Usar Webpack 5 no React Native
- Configurar Module Federation
- Gerar bundles compatíveis com dispositivos móveis
- Carregar módulos remotos com `ScriptManager`

## 🏗️ O que eles fazem juntos?

Quando usados em conjunto, eles criam uma arquitetura **modular, escalável e dinâmica** para apps React Native:

### 🔄 Fluxo de funcionamento:

1. **Re.Pack** configura o Webpack 5 para empacotar o app.
2. **Module Federation** permite que o app principal (Host) carregue módulos de outros apps (Remotes).
3. Os módulos são carregados **sob demanda**, reduzindo o tempo de inicialização e permitindo atualizações independentes.

## 📊 Benefícios combinados

| Benefício | Descrição |
|-----------|-----------|
| **Modularidade** | Divisão do app em partes independentes |
| **Escalabilidade** | Equipes podem trabalhar em módulos separados |
| **Performance** | Bundles menores e carregamento sob demanda |
| **Flexibilidade** | Uso de plugins e loaders do Webpack |
| **Atualizações dinâmicas** | Sem necessidade de recompilar o app inteiro |

## 🧪 Exemplo prático

Imagine um app bancário com os seguintes módulos:

- **Host App**: Interface principal
- **Cartões**: Módulo remoto
- **Investimentos**: Módulo remoto
- **Crédito**: Módulo remoto

Cada módulo pode ser desenvolvido por uma equipe diferente, implantado separadamente e carregado apenas quando o usuário acessa aquela funcionalidade.
