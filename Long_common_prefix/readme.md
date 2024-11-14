
# **LeetCode: Longest Common Prefix (LCP)**

## **Descrição do Problema**

Dada uma lista de strings, o objetivo é encontrar o **prefixo comum mais longo** entre elas. Se não houver um prefixo comum, a função deve retornar uma string vazia.

### **Exemplo**:
Entrada:
```python
["flower", "flow", "flight"]
```
Saída:
```python
"fl"
```

Entrada:
```python
["dog", "racecar", "car"]
```
Saída:
```python
""
```

## **Soluções**

### **1. Solução Bruta (O(n²))**
A primeira solução utiliza dois loops para comparar cada caractere de todas as strings. Esta abordagem verifica se todos os caracteres de uma posição são iguais entre todas as strings, e se não forem, retorna o prefixo encontrado até ali.

#### **Complexidade de Tempo**: O(n²)  
**Explicação**: O primeiro loop percorre cada caractere de todas as strings (loop externo), e o segundo loop percorre cada string (loop interno), o que resulta em complexidade O(n²).

#### **Código**:
```python
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs: 
            return ""
        prefix = ""
        min_len = min(len(word) for word in strs)
        for idx in range(min_len):
            current = strs[0][idx]
            for word in strs:
                if word[idx] != current:
                    return prefix
            prefix += current    
        return prefix
```

### **2. Solução Otimizada (O(n log n))**
A segunda solução começa ordenando as strings, o que tem uma complexidade O(n log n). Após a ordenação, comparamos apenas o primeiro e o último elemento da lista, já que, após a ordenação, eles têm o maior número de caracteres em comum.

#### **Complexidade de Tempo**: O(n log n)  
**Explicação**: A operação de ordenação tem complexidade O(n log n), e o loop de comparação percorre o tamanho da string mais curta (O(n)).

#### **Código**:
```python
class Solution:
    def longestCommonPrefix(self, strs: list[str]):
        if not strs: 
            return ""
        result = []
        strs.sort()  # Ordena as strings
        first = strs[0]
        last = strs[-1]

        for idx in range(min(len(first), len(last))):
            if first[idx] != last[idx]:
                break
            result.append(first[idx])
        
        return ''.join(result)
```

## **Conclusão**

- A solução **O(n²)** é simples e direta, mas pode ser ineficiente quando o número de strings ou o comprimento delas aumenta.
- A solução **O(n log n)** é mais eficiente, aproveitando a ordenação para reduzir as comparações, tornando-a mais adequada para listas grandes.

---

