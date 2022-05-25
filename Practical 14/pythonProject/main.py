import xml.dom.minidom
from xml.dom.minidom import parse
import matplotlib.pyplot as plt

DOMTree = xml.dom.minidom.parse('D:/GIT/IBI1_2021-22/Practical 14/go_obo.xml')
obo = DOMTree.documentElement
#calculate how many terms with <term> tag
terms = obo.getElementsByTagName('term')
number_term=len(terms)
print(number_term)
#The loop are written under the instruction of Weilun Du
#set a dictionary
is_a_dictionary = {}
#run the loop for all the terms in terms
for term in terms:
    #creat a list called term_is_a
    term_is_a= []
    #find all the terms with tag <is_a>
    is_a_ = term.getElementsByTagName('is_a')
    for term1 in is_a_:
        #find the id of term1 in is_a_
        id1 = term1.childNodes[0].data
        #input the ids we found into the list term_is_a
        term_is_a.append(id1)
        # if one id have been input into is_a_dictionary, append the nwe childNode id to the value of this id key
        if id1 in is_a_dictionary:
            is_a_dictionary[id1].append(term.getElementsByTagName('id')[0].childNodes[0].data)
        # if one id is new to is_a_dictionary, add it to the dictionary as the key and corresponding value is its childNode id
        else:
            is_a_dictionary[id1] = [term.getElementsByTagName('id')[0].childNodes[0].data]


def function1(x):
    #creat a another dictionary, the key of the dictionary are the childNode id of one id of terms
    global is_a_dictionary_1
    #for all terms of parentalNode
    for term2 in is_a_dictionary[x]:
        #add the id of childNode of one terms to the is_a_dictionary_1
        if term2 not in is_a_dictionary_1:
            #and give this key a random value
            is_a_dictionary_1[term2]=0
            #if the childNode also act as a parantalNode, conduct it again to find its childNode
            if term2 in is_a_dictionary:
                function1(term2)
    #return all the childNode number
    return len(is_a_dictionary_1)

#set two list to input data
total = []
translation = []
#input the
for term in terms:
    #find all the childNode id of one term in terms
    id2 = term.getElementsByTagName('id')[0].childNodes[0].data
    #find all the terms with <defstr> tag
    defstr = term.getElementsByTagName('defstr')[0]
    is_a_dictionary_1={}
    total_child = 0
    #use a loop to check all the id2, if it text contain word 'tanslation', put it into the list called translation
    if id2 in is_a_dictionary:
        total_child = function1(id2)
    #pay attention to that the word 'Translation' may be at the begainning of the sentence
    if "translation" in defstr.childNodes[0].data or "Translation" in defstr.childNodes[0].data:
        translation.append(total_child)
    total.append(total_child)
    
#draw the first chart
x=total
plt.boxplot(x,vert=True,whis=1.5,patch_artist=True,meanline=True,showbox=True,showcaps=True,showfliers=False,notch=False)
plt.title("The total childNodes of terms")
plt.ylabel('childNodes number')
plt.show()
#draw the second chart
x1=translation
plt.boxplot(x1,vert=True,whis=1.5,patch_artist=True,meanline=True,showbox=True,showcaps=True,showfliers=False,notch=False)
plt.ylabel('childNodes number')
plt.show()
#calculate whether the 'translation' terms contain, on average, a greater or small number of child nodes than the overall Gene Ontology
avr_total = sum(total) / len(total)
avr_trans = sum(translation) / len(translation)
if avr_total > avr_trans:
    print("The ‘translation’ terms	contain, on	average, a small number of	child nodes	than the overall Gene Ontology")
elif avr_total < avr_trans:
    print("The ‘translation’ terms	contain, on	average, a larger number of	child nodes	than the overall Gene Ontology")
else:
    print("The ‘translation’ terms	contain, on	average,the number of child nodes equals to the overall Gene Ontology")















