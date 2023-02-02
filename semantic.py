#-----------md DATA SET---------------
import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

#-----------sm DATA SET---------------
# You get this warning - The model you're using has no word
# vectors loaded, so the result of the Doc.similarity method 
# will be based on the tagger, parser and NER, which may not 
# give useful similarity judgements. This may happen if you're 
# using one of the small models, e.g. `en_core_web_sm`, which 
# don't ship with word vectors and only use context-sensitive 
# tensors. You can always add your own word vectors, or use 
# one of the larger models instead if available.
print("========================================")
print("============sm data set=================")

nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
# seeing the datasts results, we can see with the smaller set 
# all results have lower confidence and also that they don't seem 
# to make the same semantic sense

#===============================
# testing some of my own words, I chose some relavant to my
# own business in the cannabis industry

#-----------md DATA SET---------------
nlp = spacy.load('en_core_web_md')
word1 = nlp("Vape")
word2 = nlp("Cannabis")
word3 = nlp("Tobacco")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "dry herb vaporizer"
sentences = ["weed vape",
"cannabis vape",
"eliquid vape",
"nicotine vape",
"vape pen"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)