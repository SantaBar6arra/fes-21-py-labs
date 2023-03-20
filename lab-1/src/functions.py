from typing import Tuple
import re


def readFile(filePath: str) -> Tuple[str, int, int]:
    file = open(filePath, 'r')
    text: str = file.read()
    
    result: Tuple[str, int, int] = (filePath, countWords(text), countSentences(text))
    file.close()

    return result

def countWords(input: str) -> int:
    return len(re.findall(r'\b\w+\b', input))

def countSentences(input: str) -> int:
    return len(re.findall(r'([A-Z][^\.!?]*[\.!?])', input))
def getPalingramsSimplified(sentence: str) -> dict:
    phrases: str = sentence.split(',')
    listOfPalindromes = dict()

    for i in range(len(phrases)):
        if isPalindrome(phrases[i].replace(' ', '')):
            listOfPalindromes[phrases[i].strip()] = i

    return listOfPalindromes

def getPalingramsExtended(sentence: str) -> dict:
    phrases: str = sentence.split(',')
    listOfPalindromes = dict()
    
    for i in range(len(phrases)):
        phrase: str = phrases[i].replace(' ', '').strip()
        uniqueLetters = list(set(phrase))
        
        countOfEvenRepetitions: int = 0
        
        for k in range(0, len(uniqueLetters)):
            if phrase.count(uniqueLetters[k]) % 2 != 0:                
                countOfEvenRepetitions += 1  
        
        if countOfEvenRepetitions < 2:
            listOfPalindromes[phrases[i].strip()] = i
        
    return listOfPalindromes

def getAllPalindromes(sentence: str) -> dict:
    words: list = re.findall(r'\b\w+\b', sentence)
    listOfPalindromes = dict()

    for i in range(len(words)):
        if isPalindrome(words[i]):
            listOfPalindromes[words[i]] = i

    return listOfPalindromes


def isPalindrome(word: str) -> bool:
    return word == customReverse(word)


def customReverse(input: str) -> str:
    output: str = ''

    for i in range(len(input)-1, -1, -1):
        output += input[i]

    return output