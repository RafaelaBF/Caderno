# Componentes Básicos e Estilos no React Native

Os componentes fundamentais do React Native são elementos essenciais que formam a base para a construção de interfaces de usuário em aplicativos móveis. 

## Index 
**Componentes**
- [View](#view)
- [Text](#text)
- [Image](#image)
- [ScrollView](#scrollview)
- [TextInput](#textinput)
- [Button](#button)

**Estilo**
- [StyleSheet](#stylesheet)

## View
Ele funciona de forma semelhante à tag div em HTML e é usado para criar contêineres que agrupam outros componentes ou elementos da interface.

### Exemplo
A função App retorna uma estrutura JSX com um estilizado que contém um exibindo "Olá, React Native!". 

~~~js
import { StyleSheet, Text, View } from 'react-native';

export default function App() {
    return (
      <View style={styles.container}> 
        <Text>Olá, React Native!</Text>
      </View>
    );
}

const styles = StyleSheet.create({ // Bloco de estilos
    container: { // Define o estilo do contêiner
      flex: 1, // Para ocupar toda a tela
      alignItems: 'center', // Centralizar o conteúdo
      justifyContent: 'center', // Centralizar o conteúdo
      backgroundColor: '#f0f0f0', // Cor do fundo
     },
});      
~~~

## Text
É usado para exibir textos. Ele é semelhante às tags p ou span em HTML e é fundamental para mostrar informações textuais no aplicativo.

Propriedades importantes:
- **numberOfLines**: Limita o número de linhas exibidas.
- **ellipsizeMode**: Define como o texto deve ser cortado (tail, head, middle).

### Exemplo
A função App retorna um elemento com estilo embutido, definindo o tamanho da fonte como 20 e a cor do texto como azul. O texto exibido na tela é "Este é um exemplo de componente de texto".

~~~js
import { Text } from 'react-native';

export default function App() {
    return (
       <Text style={{ fontSize: 20, color: 'blue' }}>
            Este é um exemplo de componente de texto.
       </Text>
    );
}
~~~

## Image
É usado para exibir imagens de recursos locais ou URLs remotas.

Propriedades importantes:
- **source**: Define a origem da imagem, que pode ser um recurso local ou uma URL.
- **resizeMode**: Controla como a imagem é redimensionada (cover, contain, stretch, repeat, center).

### Exemplo
O componente é retornado com a propriedade source, que especifica a URL da imagem a ser exibida ('https://reactnative.dev/img/tiny_logo.png'). O componente é estilizado com um objeto de estilo embutido que define a largura (width: 100) e a altura (height: 100) da imagem.

~~~js
import { Image } from 'react-native';

export default function App() {
     return (
        <Image
            source={{ uri: 'https://reactnative.dev/img/tiny_logo.png' }}
            style={{ width: 100, height: 100 }}
        />
     );
}
~~~

## ScrollView
É um contêiner de rolagem que permite que seus elementos filhos sejam roláveis. Ele é ideal para listas de conteúdo pequenas e layouts que exigem rolagem.

Propriedades importantes:

- **horizontal**: Define se a rolagem será horizontal (por padrão, é vertical).
- **showsHorizontalScrollIndicator e showsVerticalScrollIndicator**: Controlam a visibilidade das barras de rolagem

### Exemplo
É retornado com um estilo que aplica uma margem superior de 50 (marginTop: 50). Dentro dele, há três componentes que exibem "Item 1", "Item 2" e "Item 3"

~~~js
import { ScrollView, Text } from 'react-native';

export default function App() {
     return (
        <ScrollView style={{ marginTop: 50 }}>
            <Text>Item 1</Text>
            <Text>Item 2</Text>
            <Text>Item 3</Text>
            {/* Adicione mais itens para ver a rolagem em ação */}
        </ScrollView>
     );
}
~~~

## TextInput
É usado para capturar entradas de texto do usuário.

Propriedades importantes:

- **placeholder**: Texto que aparece quando o campo está vazio.
- **secureTextEntry**: Oculta o texto (útil para campos de senha).
- **keyboardType**: Define o tipo de teclado (por exemplo: numeric, email-address).

### Exemplo
Um contêiner que ocupa todo o espaço disponível na tela (`flex: 1`), centralizando seu conteúdo verticalmente com `justifyContent: 'center'` e aplicando um padding de 20. Dentro do contêiner, há um componente com o estilo `styles.input`, que inclui uma borda cinza (`borderColor: 'gray'`), uma largura de borda de 1 (`borderWidth: 1`), um preenchimento interno de 10 (`padding: 10`), e bordas arredondadas com um borderRadius de 5. O TextInput também possui um placeholder que exibe a mensagem "Digite aqui..." até que o usuário comece a digitar. 

~~~js
import { View, TextInput, StyleSheet } from 'react-native';
   

export default function App() {
     return (
        <View style={styles.container}>
            <TextInput
              style={styles.input}
              placeholder="Digite aqui..."
            />
        </View>
     );
 }

 const styles = StyleSheet.create({
     container: {
          flex: 1,
          justifyContent: 'center',
          padding: 20,
      },
      input: {
          borderWidth: 1,
          borderColor: 'gray',
          padding: 10,
          borderRadius: 5,
      },
 });      
~~~

## Button
É um botão simples que pode ser usado para capturar interações do usuário.

Propriedades importantes:
- **title**: O texto que aparece no botão.
- **onPress**: Função que é chamada quando o botão é pressionado.
- **color**: Cor do botão (iOS).

### Exemplo
Cria um aplicativo que inclui um botão interativo que exibe um alerta quando pressionado. A função App retorna um contêiner `<view>` com um estilo embutido que aplica uma margem superior de 50 (marginTop: 50). Dentro desse `<view>`, há um componente `<button>` com a propriedade `title` que define o texto do botão como "Pressione-me". A propriedade `onPress` é uma função que é chamada quando o botão é pressionado; nesse caso, ela exibe um alerta com a mensagem "Botão pressionado!" usando `Alert.alert`.

~~~js
import React from 'react';
import { Button, View, Alert } from 'react-native';

export default function App() {
    return (
       <View style={{ marginTop: 50 }}>
          <Button
            title="Pressione-me"
            onPress={() => Alert.alert('Botão pressionado!')}
        />
       </View>
    );
}
~~~

> OBS: O comando `Alert.alert()` é projetado para funcionar em dispositivos móveis nativos, como Android e iOS, mas não tem suporte completo em navegadores. Para funcionar completamente, teste este exemplo em seu dispositivo móvel.

## StyleSheet

StyleSheet é uma API do React Native que permite criar e gerenciar estilos de maneira semelhante ao CSS, mas com sintaxe em JavaScript. Ele é usado para definir um objeto de estilo que pode ser aplicado aos componentes.

Principais propriedades:
- **flex**: Controla a flexibilidade do componente.
- **justifyContent**: Alinha os itens no eixo principal (flex-start, center, space-between, etc.).
- **alignItems**: Alinha os itens no eixo perpendicular (flex-start, center, stretch, etc.).
- **margin e padding**: Adicionam espaçamento interno e externo.
- **width e height**: Definem o tamanho do componente.
- **fontSize e color**: Usados para estilizar textos.

### Benefícios do uso do StyleSheet
- **Modularidade**: Os estilos podem ser definidos em um único lugar e aplicados a vários componentes, facilitando a manutenção e a reutilização de estilos.
- **Desempenho**: O uso do StyleSheet.create() otimiza o processo de renderização, pois o React Native converte os estilos em um formato que pode ser processado de forma mais eficiente.
- **Legibilidade**: Organiza o código e melhora a legibilidade ao manter os estilos separados da lógica do componente.

### Diferenças em Relação ao CSS da Web
- **CamelCase**: As propriedades de estilo usam camelCase em vez de kebab-case (por exemplo, backgroundColor em vez de background-color).
- **Unidades Implícitas**: No React Native, as unidades de medida, como px, não são usadas; todos os valores são considerados pontos de densidade de pixels.
- **Propriedades Exclusivas**: Algumas propriedades específicas, como flex e alignItems, são usadas de forma similar ao CSS Flexbox para layouts.

### Exemplo
Um app simples em React Native que mostra o texto "Olá, React Native!" centralizado na tela. O fundo é cinza claro, e o texto azul tem tamanho 20. O layout usa flex: 1 para ocupar toda a tela e centraliza o conteúdo com justifyContent e alignItems no centro.

~~~js
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

export default function App() {
   return (
      <View style={styles.container}>
          <Text style={styles.text}>Olá, React Native!</Text>
      </View>
   );
}

const styles = StyleSheet.create({
   container: {
        flex: 1,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#f0f0f0',
    },
    text: {
        fontSize: 20,
        color: 'blue',
    },
});
~~~
