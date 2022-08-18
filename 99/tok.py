# 日本語のサブワード化
import sentencepiece as spm
import re

sp = spm.SentencePieceProcessor()
sp.Load('kyoto_ja.model')

src = input()

for x in src:
    x = x.strip()
    x = re.sub(r'\s+', ' ', x)
    x = sp.encode_as_pieces(x)
    x = ' '.join(x)
    print(x)