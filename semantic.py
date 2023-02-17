#====================[NOTE ,different between 'sm','md']==============================
# The different between ['en_core_web_sm'] & ['en_core_web_md']

# -> ''' This message appeared when i used 'sm' in short models like words
# -> ['sm' >> has no word vectors loaded, so the result of the Token.similarity 
#     method will be based on the tagger, parser and NER, which may not give useful
#     similarity judgement. This may happen if you're using one of the small models,
#     e.g. `en_core_web_sm`, which don't ship with word vectors and only use 
#     context-sensitive tensors. You can always add your own word vectors, 
#     or use one of the larger models instead if available.]
# ->  'md' is more accurate than 'sm'    

#====================#[MY EXAMPLE TO TRY NOTE]=========================================
# i choose to Herbivore animals (cow,gout) , and carnivorous animal (lion,tiger)
# the two Herbivore animals (cow,gout)are  producing milk too so the similarity was high 
# the carnivorous animal (lion,tiger) the similarity was less than  (cow,gout) because they are carnivorous only
#===================================================================================================
import spacy
#nlp = spacy.load('en_core_web_sm')
nlp = spacy.load('en_core_web_md')

#========================================
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#==================================
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
   for token2 in tokens:
         print(token1.text, token2.text, token1.similarity(token2))
#===============[MY EXAMPLE TO TRY]===================
tokens = nlp('cow goat lion tiger')
for token1 in tokens:
   for token2 in tokens:
         print(token1.text, token2.text, token1.similarity(token2))
        
#===================================
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
#=====================================