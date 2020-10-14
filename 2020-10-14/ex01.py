import CaboCha

c = CaboCha.Parser()
sentence = "太郎はこの本を二郎を見た女性に渡した。"
tree =  c.parse(sentence)
chunks = []
text = ""
toChunkId = -1

for i in range(0, tree.size()):
    token = tree.token(i)
    text = token.surface if token.chunk else (text + token.surface) 
    toChunkId = token.chunk.link if token.chunk else toChunkId
    if i == tree.size() - 1 or tree.token(i+1).chunk:
       chunks.append({'c': text, 'to': toChunkId})

for chunk in chunks:
    if chunk['to'] >= 0:
        print(chunk['c'] + " →　" + chunks[chunk['to']]['c'])
