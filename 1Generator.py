def generate_sentences (a,b,c):
    
    #Checking that the lists are not empty
    if a and b and c:
        
       #order alphabetically
       a.sort()
       b.sort()
       c.sort()
       text = []
       for subject in a:
           for predicate in b:
               for obj in c:
                   sentence = (subject,predicate,obj)
                   #separate words with spaces
                   x = " ".join(sentence)      
                   text.append(x)
       #separate sentences with ". " and end with "."
       return(". ".join (text)+".")
   
    else:
        
        #if any list is empty I can't form the sentence
        return ("The sentence cannot be generated. Missing elements")


def test_generate_sentences1():
    assert generate_sentences(["Mark", "Mary"], ["hates", "loves"], ["apples", "bananas"]) == "Mark hates apples. Mark hates bananas. Mark loves apples. Mark loves bananas. Mary hates apples. Mary hates bananas. Mary loves apples. Mary loves bananas."
    
    
def test_generate_sentences2():
    assert generate_sentences(["Vlad", "John"], ["drives"], ["car", "motorcycle", "bus"]) == "John drives bus. John drives car. John drives motorcycle. Vlad drives bus. Vlad drives car. Vlad drives motorcycle."
  

def test_generate_sentences3():
    assert generate_sentences(["Maria", "Anne", "Peter"], ["sells", "buys"], ["car"]) == "Anne buys car. Anne sells car. Maria buys car. Maria sells car. Peter buys car. Peter sells car."

def test_generate_sentences_missing_elements():
    assert generate_sentences([], ["drives"], ["car", "motorcycle", "bus"]) == "The sentence cannot be generated. Missing elements"    
    

