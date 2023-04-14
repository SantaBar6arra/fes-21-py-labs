import re
import sys

def IsPalinfrome_Test() -> None:
    assert IsPalindrome('deified') == True
    assert IsPalindrome('word') == False

def GetPalingrams_Test() -> None:
    TestDict: dict = GetPalingrams('nurses run, bedroom boredom')
    
    assert TestDict['nurses run'] == 0
    assert TestDict.__contains__('bedroom boredom') == False
    
def GetPalingrams_V2_Test() -> None:
    TestDict: dict = GetPalingrams_Better('lived devils, Nurses run, stir grits, bedroom boredom, GARDEN DANGER')
    
    assert TestDict['lived devils'] == 0
    assert TestDict.__contains__('Nurses run') == False
    assert TestDict['stir grits'] == 2
    assert TestDict['bedroom boredom'] == 3
    assert TestDict['GARDEN DANGER'] == 4

def CountWordsTest() -> None:
    File = open('C:/Users/Ivan/OneDrive/Рабочий стол/Folders/Lab for Uni/course2sem2/lab1py/text.txt', 'r')
    txt: str = File.read()
    File.close() 
    
    assert CountWords(txt) == 4563
    
def GetPalingrams_Better(txt: str) -> dict:
    Phrases: str = txt.split(',')
    PalindromesList = dict()
    
    for i in range(len(Phrases)):
        phrase: str = Phrases[i].replace(' ', '').strip()
        unique_letters = list(set(phrase))
        
        count_of_even_reps: int = 0
        
        for j in range(0, len(unique_letters)):
            if phrase.count(unique_letters[j]) % 2 != 0:                
                count_of_even_reps += 1  
        
        if count_of_even_reps < 2:
            PalindromesList[Phrases[i].strip()] = i
        
    return PalindromesList

def GetPalingrams(txt: str) -> dict:
    phrases: str = txt.split(',')
    PalingramsList = dict()

    for i in range(len(phrases)):
        if IsPalindrome(phrases[i].replace(' ', '')):
            PalingramsList[phrases[i].strip()] = i

    return PalingramsList


def GetAllPalindromes(txt: str) -> dict:
    words: list = re.findall(r'\b\w+\b', txt)

    PalindromesList = dict()

    for i in range(len(words)):
        if IsPalindrome(words[i]):
            PalindromesList[words[i]] = i

    return PalindromesList


def IsPalindrome(word: str) -> bool:
    return word == ReverseList(word)


def ReverseList(in_str: str) -> str:
    out_str: str = ''

    for i in range(len(in_str)-1, -1, -1):
        out_str += in_str[i]

    return out_str

from typing import Tuple
import re


def ReadFile(file_path: str) -> Tuple[str, int, int]:
    file = open(file_path, 'r')

    txt: str = file.read()

    res: Tuple[str, int] = (file_path, CountWords(txt))

    file.close()

    return res


def CountWords(in_txt: str) -> int:
    return len(re.findall(r'\b\w+\b', in_txt))

