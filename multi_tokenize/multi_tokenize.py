# multi tokenizer

## Sudachi tokenize

from sudachipy import tokenizer
from sudachipy import dictionary

#### init dict
tokenizer_obj = dictionary.Dictionary().create()

def sudachi(sentence:str):
    mode = tokenizer.Tokenizer.SplitMode.C # ModeC
    tokens  = [m.surface() for m in tokenizer_obj.tokenize(sentence,mode)]
    return tokens



## N-gram tokenize

def n_gram(sentence:str , n:int):
    #文字数がnより少ない時は"*"で埋める
    if len(sentence) < n:
        sentence = "*"* (n - len(sentence) ) + sentence
    else:
        pass
    
    # 基準を1文字(単語)ずつ ずらしながらn文字分抜き出す
    tokens =  [ sentence[idx:idx + n] for idx in range(len(sentence) - n + 1)]
    return tokens



## ICU tokenize

from icu_tokenizer.tokenizer import Tokenizer

# create protect list
# extra_protected_patterns = ["東京都","東京ディズニーランド"] # 分割させたくないtokenをlistで渡せば固定される

def icu_jp(sentence: str, extra_protected_patterns:list=[]):
    tokenizer = Tokenizer(lang="ja", extra_protected_patterns = extra_protected_patterns)
    tokens =tokenizer.tokenize(sentence)
    return tokens
