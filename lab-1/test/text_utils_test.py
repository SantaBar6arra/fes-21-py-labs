import sys
sys.path.append('../src')
from text_utils import *

def is_palindrome_test() -> None:
    assert is_palindrome('deified') == True
    assert is_palindrome('word') == False

def get_palingrams_test() -> None:
    fn_res: dict = get_palingrams('nurses run, bedroom boredom')
    
    assert fn_res['nurses run'] == 0
    assert fn_res.__contains__('bedroom boredom') == False
    
def get_palingrams_v2_test() -> None:
    fn_res: dict = get_palingrams_v2('lived devils, Nurses run, stir grits, bedroom boredom, GARDEN DANGER')
    
    assert fn_res['lived devils'] == 0
    assert fn_res.__contains__('Nurses run') == False
    assert fn_res['stir grits'] == 2
    assert fn_res['bedroom boredom'] == 3
    assert fn_res['GARDEN DANGER'] == 4
    