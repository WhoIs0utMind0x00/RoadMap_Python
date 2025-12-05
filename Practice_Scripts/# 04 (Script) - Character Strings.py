# Instrucción ->> Crea un programa que analice dos palabras diferentes y realice comprobaciones para descubrir si son:
# Palíndromos
# Anagramas
# Isogramas

def compare_words(word_1, word_2):
    # Palindromes
    palindrome_1 = word_1.lower() == word_1.lower()[::-1]
    palindrome_2 = word_2.lower() == word_2.lower()[::-1]
    # Anagram
    anagram = sorted(word_1) == sorted(word_2) and len(word_1) == len(word_2)
    # Isograms
    isogram_1 = len(word_1) == len(set(word_1))
    isogram_2 = len(word_2) == len(set(word_2))

    # ->> Palindrome
    if palindrome_1 and palindrome_2:
        print(f"{word_1} and {word_2} are palindromes")
    elif palindrome_1 and not palindrome_2:
        print(f"{word_1} is a palindrome, {word_2} it's not")
    elif not palindrome_1 and palindrome_2:
        print(f"{word_1} is not a palindrome, but {word_2} is")

    # ->> Anagram
    elif anagram:
        print(f"{word_1} and {word_2} are anagrams")
    
    # ->> Isogram
    elif isogram_1 and isogram_2:
        print(f"{word_1} and {word_2} are isograms")
    elif isogram_1 and not isogram_2:
        print(f"{word_1} is an isogram, but {word_2} is not")
    elif not isogram_1 and isogram_2:
        print(f"{word_1} is not an isogram, but {word_2} is")
    else:
        print("Neither applies")