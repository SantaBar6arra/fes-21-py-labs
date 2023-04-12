from typing import Tuple, Dict

def read_file(file_path: str) -> Tuple[str, int, int]:
    with open(file_path, "r") as file:
        file_content = file.read()
    file_words_count = len(file_content.split())
    file_sentence_count = 0
    for symbol in file_content:
        if symbol in [".", "!", "?", "..."]:
            file_sentence_count += 1
    return file_content, file_words_count, file_sentence_count

def get_all_palindromes(content: str) -> Dict:
    palindromes = {}
    words = content.split()
    for word in words:
        if len(word) < 3 or any(char.isdigit() for char in word):
            continue
        for letter in word:
            if check_palindrome(word):
                if word in palindromes:
                    palindromes[word] += 1
                else:
                    palindromes[word] = 1
    return palindromes

def check_palindrome(word: str) -> bool:
    return word == word[::-1]

def get_palingrams(content: str) -> Dict:
    palingrams = {}
    words = content.split()

    for i in range(len(words)):
        if len(words[i]) < 3 or any(char.isdigit() for char in words[i]):
            continue
        for j in range(i+1, len(words)):
            if len(words[j]) < 3 or any(char.isdigit() for char in words[i]):
                continue
            phrase = words[i] + ' ' + words[j]
            if phrase == phrase[::-1]:
                palingrams[phrase] = (i, j)
            phrase = words[j] + ' ' + words[i]
            if phrase == phrase[::-1]:
                palingrams[phrase] = (j, i)

    return palingrams

file_content, file_words_count, file_sentence_count = read_file("example.txt")

print(read_file("example.txt"))

print(get_all_palindromes(file_content))

print(get_palingrams(file_content))