import re


def get_palingrams_v2(txt: str) -> dict:
    """
    gets palingrams(extended format) in the text specified

    input: '<phrase to be suspected>, <phrase to be suspected>, <phrase to be suspected> ...'

    returns: dictionary where key is a word, value is an integer position of phrase in the text
    """
    phrases: str = txt.split(',')
    res = dict()
    
    for i in range(len(phrases)):
        phrase: str = phrases[i].replace(' ', '').strip()
        unique_letters = list(set(phrase))
        
        count_of_even_reps: int = 0
        
        for j in range(0, len(unique_letters)):
            if phrase.count(unique_letters[j]) % 2 != 0:                
                count_of_even_reps += 1  
        
        if count_of_even_reps < 2:
            res[phrases[i].strip()] = i
        
    return res

def get_palingrams(txt: str) -> dict:
    """
    gets palingrams(simplified format) in the text specified

    input: '<phrase to be suspected>, <phrase to be suspected>, <phrase to be suspected> ...'

    returns: dictionary where key is a word, value is an integer position of phrase in the text
    """
    phrases: str = txt.split(',')
    res = dict()

    for i in range(len(phrases)):
        if is_palindrome(phrases[i].replace(' ', '')):
            res[phrases[i].strip()] = i

    return res


def get_all_palindromes(txt: str) -> dict:
    """
    gets all palindromes in the input text specrified

    returns: dictionary where key is a word, value is an integer position in the text
    """
    words: list = re.findall(r'\b\w+\b', txt)

    res = dict()

    for i in range(len(words)):
        if is_palindrome(words[i]):
            res[words[i]] = i

    return res


def is_palindrome(word: str) -> bool:
    """
    checks whether the word is a palindrome
    """
    return word == custom_reverse(word)


def custom_reverse(in_str: str) -> str:
    """
    reversing any string

    returns: reversed string
    """
    out_str: str = ''

    for i in range(len(in_str)-1, -1, -1):
        out_str += in_str[i]

    return out_str
