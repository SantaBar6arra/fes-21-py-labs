import sys
sys.path.append('C:/Programming/Projects/LNU labs/My labs/Python/fes-21-py-labs/lab-1/src')
from functions import countWords, countSentences, isPalindrome, getPalingramsSimplified, getPalingramsExtended

def countWords_test() -> None:
    textFile = open('C:/Programming/Projects/LNU labs/My labs/Python/fes-21-py-labs/lab-1/text.txt', 'r')
    text: str = textFile.read()
    textFile.close() 
    
    assert countWords(text) == 41
    
def countSentences_test() -> None:
    textFile = open('C:/Programming/Projects/LNU labs/My labs/Python/fes-21-py-labs/lab-1/text.txt', 'r')
    text: str = textFile.read()
    textFile.close() 
    
    assert countSentences(text) == 8

def isPalindrome_test() -> None:
    assert isPalindrome('deified') == True
    assert isPalindrome('word') == False

def getPalingramsSimplified_test() -> None:
    output: dict = getPalingramsSimplified('noons noon, live evil')
    
    assert  output['noons noon'] == 0
    assert  output.__contains__('live evil') == True
    
def getPalingramsExtended_test() -> None:
    output: dict = getPalingramsExtended('radar radar, erefer refer, deified edified, tenet tenet')
    
    assert  output['radar radar'] == 0
    assert  output.__contains__('refer refer') == False
    assert  output['deified edified'] == 2
    assert  output['tenet tenet'] == 3