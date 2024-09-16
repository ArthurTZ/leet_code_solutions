import string

### - String Transformation HackeRank
### - Para cada caractere subsequente, compare-o com o caractere anterior:
# Se o caractere anterior precede o atual no alfabeto, transforme o atual em maiúsculo.
# Se o caractere anterior vem depois do atual no alfabeto, transforme o atual em minúsculo.
# Se os caracteres forem iguais, o caractere atual permanece inalterado.


# If the previous character precedes the current one in the alphabet, make the current one uppercase.
# If the previous character comes after the current one in the alphabet, make the current one lowercase.
# If the characters are the same, the current character remains unchanged



def string_transformation(sentence):
    alphabet = string.ascii_lowercase  
    result = [] 
    
    for word in sentence.split():
        transformed_word = word[0] 
        
        for i, letter in enumerate(word[1:], start=1):  
            prev_letter = word[i-1].lower()  
            curr_letter = letter.lower()  
            
            if alphabet.index(prev_letter) < alphabet.index(curr_letter):
                transformed_word += letter.upper()  
            elif alphabet.index(prev_letter) > alphabet.index(curr_letter):
                transformed_word += letter.lower()  
            else:
                transformed_word += letter 
        result.append(transformed_word)
    
    return ' '.join(result)  