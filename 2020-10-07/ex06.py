import MeCab

# text = "昨日の天気は晴れでした。"
text = input()
mecab = MeCab.Tagger()

parses = mecab.parse(text)
parse = parses.split('\n')

for par in parse:
    p = par.split(',')
    if p[0] == "EOS":
        break
    print(p[0], "\t", p[-3])
