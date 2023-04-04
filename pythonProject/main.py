import re


def read_file(file_path: str) -> tuple:
    """Reads a file and returns the contents as a tuple of strings.

    Args:
        file_path (str): The path to the file to read.

    Returns:
        tuple[str, int, int]: A tuple containing the contents of the file, the
            number of lines in the file, and the number of characters in the
            file.
    """
    with open(file_path, "r") as f:
        text = f.read()
        words_count = len(re.findall(r"\w+(?:['-.\/]\w+)*", text))
        sentences_count = len(re.findall(r'[.?!]+', text))

    return text, words_count, sentences_count


def get_all_palindromes(content: str) -> dict:
    """Returns a dictionary of palindromes in the given text.

    Args:
        content (str): The text to search for palindromes.

    Returns:
        dict: A dictionary of palindromes in the given text.
    """
    content = content.lower()
    words = re.findall(r'\b\w+\b', content)
    palindromes = {}

    for word in words:
        if word == word[::-1] and len(word) > 1:
            if word in palindromes:
                palindromes[word] += 1
            else:
                palindromes[word] = 1

    return palindromes


def get_palingrams(content: str) -> dict:
    """Returns a dictionary of palingrams in the given text.

    Args:
        content (str): The text to search for palingrams.

    Returns:
        dict: A dictionary of palingrams in the given text.
    """
    letters_only = re.sub(r'[^a-zA-Z\s]', "", content).lower()

    # Split the text into sentences
    sentences = re.split(r'[.?!]', letters_only)
    palingrams = {}

    for sentence in sentences:
        words = sentence.split()
        for i in range(len(words) - 1):
            left_word = words[i]
            right_word = words[i + 1]
            if len(left_word) == 1 or len(right_word) == 1:
                continue
            if left_word in right_word[::-1] or right_word in left_word[::-1]:
                word = left_word + " " + right_word
                if word in palingrams:
                    palingrams[word] += 1
                else:
                    palingrams[word] = 1

    return palingrams


def get_anagrams(content: str) -> dict:
    """Returns a dictionary of anagrams in the given text.

    Args:
        content (str): The text to search for anagrams.

    Returns:
        dict: A dictionary of anagrams in the given text.
    """
    content = content.lower()
    words = re.findall(r'\b\w+\b', content)
    anagrams = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word in anagrams and word not in anagrams[sorted_word]:
            anagrams[sorted_word].append(word)
        else:
            anagrams[sorted_word] = [word]

    list_of_anagrams = list(anagrams.items())
    real_anagrams = {}
    for i in range(len(list_of_anagrams)):
        if len(list_of_anagrams[i][1]) > 1:
            real_anagrams[list_of_anagrams[i][0]] = list_of_anagrams[i][1]

    return real_anagrams


def run():
    file_path = "words"
    text, words_count, sentences_count = read_file(file_path)
    print(f'The text has {words_count} words and {sentences_count} sentences.')

    palindromes = get_all_palindromes(text)
    list_of_palindromes = list(palindromes.items())
    print("\nThe following are the palindromes in the text :")
    print(len(list_of_palindromes), "palindromes found")
    for i in range(min(10, len(list_of_palindromes))):
        print(list_of_palindromes[i], end=" ")

    print("\n\nThe following are the palingrams in the text:")
    palingrams = get_palingrams(text)
    list_of_palingrams = list(palingrams.items())
    print(len(list_of_palingrams), "palingrams found")
    for i in range(min(10, len(list_of_palingrams))):
        print(list_of_palingrams[i], end=" ")

    print("\n\nThe following are the anagrams in the text:")
    anagrams = get_anagrams(text)
    list_of_anagrams = list(anagrams.items())
    print(len(list_of_anagrams), "anagrams found")
    for i in range(min(10, len(list_of_anagrams))):
        print(list_of_anagrams[i], end=" ")


if __name__ == "__main__":
    run()