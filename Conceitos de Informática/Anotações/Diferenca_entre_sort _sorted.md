# A diferença entre `sort` e  `sorted`

As funções `sort` e `sorted` são usadas para ordenar coleções, mas elas têm diferenças importantes na forma como operam e no tipo de coleção que retornam.

## `sort`

A função `sort` é uma extensão mutável que ordena a própria coleção em que é chamada. Isso significa que a coleção original será modificada.

### Exemplo em kotlin:

```kotlin
val list = mutableListOf(3, 1, 2)
list.sortBy { it } // A lista original será alterada
println(list) // Output: [1, 2, 3]
```
### Exemplo em Python:

```python
list = [3, 1, 2]
list.sort()  # A lista original será alterada
print(list)  # Output: [1, 2, 3]
```
### Exemplo em Javascript:

```javascript
let array = [3, 1, 2];
array.sort();  // O array original será alterado
console.log(array);  // Output: [1, 2, 3]
```
### Exemplo em Java:

```java
import java.util.ArrayList;
import java.util.Collections;

public class Main {
    public static void main(String[] args) {
        ArrayList<Integer> list = new ArrayList<>();
        list.add(3);
        list.add(1);
        list.add(2);
        
        Collections.sort(list);  // A lista original será alterada
        System.out.println(list);  // Output: [1, 2, 3]
    }
}
```

## `sorted`

A função `sorted`, por outro lado, não modifica a coleção original. Em vez disso, ela retorna uma nova lista contendo os elementos ordenados.

### Exemplo em kotlin:

```kotlin
val list = listOf(3, 1, 2)
val sortedList = list.sortedBy { it } // A lista original permanece inalterada
println(sortedList) // Output: [1, 2, 3]
println(list) // Output: [3, 1, 2]
```
### Exemplo em Python:

```python
list = [3, 1, 2]
sorted_list = sorted(list)  # A lista original permanece inalterada
print(sorted_list)  # Output: [1, 2, 3]
print(list)  # Output: [3, 1, 2]
```

### Exemplo em Javascript:

```javascript
let array = [3, 1, 2];
let sortedArray = [...array].sort();  // O array original permanece inalterado
console.log(sortedArray);  // Output: [1, 2, 3]
console.log(array);  // Output: [3, 1, 2]
```

### Exemplo em Java:

```java
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(3);
        list.add(1);
        list.add(2);
        
        List<Integer> sortedList = new ArrayList<>(list);
        Collections.sort(sortedList);  // A lista original permanece inalterada
        System.out.println(sortedList);  // Output: [1, 2, 3]
        System.out.println(list);  // Output: [3, 1, 2]
    }
}
```

## Resumo das diferenças

- **Mutabilidade:** `sort` modifica a coleção original, enquanto `sorted` retorna uma nova lista ordenada sem alterar a coleção original.
- **Uso:** `sort` é usada quando você deseja ordenar a própria coleção mutável, enquanto `sorted` é usada quando você precisa de uma nova lista ordenada sem modificar a original.
