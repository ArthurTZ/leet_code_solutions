
# **LeetCode: Palindrome Checker**

## **Descrição do Problema**

Dado um número inteiro, o objetivo é verificar se ele é um **palíndromo** – ou seja, se ele é lido da mesma forma da esquerda para a direita e vice-versa. Retorne `True` se for um palíndromo; caso contrário, retorne `False`.

### **Exemplo**:

Entrada:
```python
121
```
Saída:
```python
True
```

Entrada:
```python
-121
```
Saída:
```python
False
```
Explicação: A leitura de trás para frente resulta em 121-, o que não é igual a 121.

## **Soluções**

### **1. Solução Bruta (O(n²))**
A primeira abordagem converte o número em uma string e armazena cada caractere em uma lista para facilitar a comparação dos caracteres da esquerda para a direita e vice-versa. Comparando o primeiro e o último caractere até o meio da string, podemos verificar se é um palíndromo.

#### **Complexidade de Tempo**: O(n²)  
**Explicação**: A criação da lista e o loop de comparação para cada elemento resulta em complexidade quadrática.

#### **Código**:
```python
class Solution:
    def isPalindrome(self, x):
        x = str(x)
        lista = [x for x in x]
        for idx, val in enumerate(lista):
            if idx >= len(lista) // 2:
                break
            if val != lista[-(idx +1)]:
                return False
        return True
```

### **2. Solução Otimizada (O(n))**
Na solução otimizada, eliminamos a lista e usamos comparações diretas de índices dentro da string. Esta versão reduz a complexidade ao simplificar o código e evitar operações desnecessárias.

#### **Complexidade de Tempo**: O(n)  
**Explicação**: Comparamos diretamente os índices da string até o meio, reduzindo a complexidade para linear.

#### **Código**:
```python
class Solution:
    def isPalindrome(self, x):
        x = str(x)
        if x < 0:
            return False
        for idx in range(len(x) // 2):
            if x[idx] != x[-(idx + 1)]:
                return False
        return True
```

## **Conclusão**

- A **Solução Bruta** é mais intuitiva, mas cria uma lista extra e é menos eficiente.
- A **Solução Otimizada** simplifica o processo e é mais adequada para números maiores.
---

