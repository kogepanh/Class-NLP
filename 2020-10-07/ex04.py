import MeCab


text = '形態素解析をする'
mecab = MeCab.Tagger()
par = mecab.parse(text)
print(text)
print('----------')
print(par)
