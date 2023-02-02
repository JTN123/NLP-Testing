import spacy
nlp = spacy.load('en_core_web_md')

compare = "Will he save\
their world or destroy it? When the Hulk becomes too dangerous for the\
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a\
planet where the Hulk can live in peace. Unfortunately, Hulk land on the\
planet Sakaar where he is sold into slavery and trained as a gladiator."

model_sentence = nlp(compare)
most_similar = 0
with open("movies.txt", "r", encoding="utf-8") as f:
    # we read in contents as a list of tuples splitting 'movie x:' and the desciption
    # for more accuracy
    contents = f.readlines()
    list = []
    for line in contents:
        key, value = line.strip().split(":")
        list.append((key, value))
    
    # we then only compare movie descripitons with the input movie 'hulks' description
    # for loop itterates throuh each descriptions and saves the movie with the highest confidence
    for i in range(len(list)):
        similarity = nlp(list[i][1]).similarity(model_sentence)
        if similarity > most_similar:
            most_similar = similarity
            most_similar_movie = contents[i]            
print("---------------------------------------")
print(f"The movie description:\n{compare}")
print("---------------------------------------")
print(f"Most similar movie:\n{most_similar_movie}With a confidence of {most_similar}")


            
