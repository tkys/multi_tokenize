# multi-tokenize
トークナイザをいくつかまとめたもの

- Sudachi:日本語形態素解析器
  - Sudachi辞書のバージョンを更新するとそれまでの分割結果と差異がでる可能性があります
- N-gram 
- ICU: Unicodeで規定された単語分割器`icu::BreakIterator`のPythonラッパー`PyICU`で分割
  - `PyICU`のICU辞書とUnicodeの最新バージョンでのICU辞書はバージョンが異なる場合に分割結果に差異があります

 　　

## How to use

### Install

```
pip install git+https://github.com/tkys/multi-tokenize.git
```

### Quick start
```
import multi_tokenize as mt

text = "東京都には無い東京ディズニーランド"


print(mt.sudachi(text))

print(mt.n_gram(text,2))

print(mt.icu_jp(text))

```


### Sudachi　（Mode:C）

```
import multi_tokenize as mt

text = "東京都には無い東京ディズニーランド"


mt.sudachi(text)

>>>　['東京都', 'に', 'は', '無い', '東京ディズニーランド']

```
### N_gram  

#### n=1 uni-gram

```
import multi_tokenize as mt

text = "東京都には無い東京ディズニーランド"


mt.n_gram(text,1) 

>>> ['東', '京', '都', 'に', 'は', '無', 'い', '東', '京', 'デ', 'ィ', 'ズ', 'ニ', 'ー', 'ラ', 'ン', 'ド']

```

#### n=2 bi-gram
```
import multi_tokenize as mt

text = "東京都には無い東京ディズニーランド"


mt.n_gram(text,2) 

>>> ['東京', '京都', '都に', 'には', 'は無', '無い', 'い東', '東京', '京デ', 'ディ', 'ィズ', 'ズニ', 'ニー', 'ーラ', 'ラン', 'ンド']

```

#### n=3 tri-gram

```
import multi_tokenize as mt

text = "東京都には無い東京ディズニーランド"


mt.n_gram(text,3) 

>>> ['東京都', '京都に', '都には', 'には無', 'は無い', '無い東', 'い東京', '東京デ', '京ディ', 'ディズ', 'ィズニ', 'ズニー', 'ニーラ', 'ーラン', 'ランド']

```

### ICU

```
import multi_tokenize as mt

text = "東京都には無い東京ディズニーランド"


mt.icu_jp(text)

>>> ['東京', '都', 'に', 'は', '無い', '東京', 'ディズニーランド']

```

#### ICU ユーザー定義辞書 

引数 `extra_protected_patterns` で指定したtokenは分割させずに固定されます

```
import multi_tokenize as mt

text = "東京都には無い東京ディズニーランド"


extra_protected_patterns = ["東京都","東京ディズニーランド"]

mt.icu_jp(text, extra_protected_patterns)

>>> ['東京都', 'に', 'は', '無い', '東京ディズニーランド']

```

