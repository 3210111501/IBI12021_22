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
#creat a list tag_is_a
term_is_a=[]
for term in terms:
    is_as = []
    IS_a = term.getElementsByTagName('is_a')
    for q in IS_a:
        is_a = q.childNodes[0].data
        is_as.append(is_a)
        if is_a in term_is_a:
            is_a_dictionary[is_a].append(term.getElementsByTagName('id')[0].childNodes[0].data)
        else:
            is_a_dictionary[is_a] = [term.getElementsByTagName('id')[0].childNodes[0].data]


def function1(p):
    #creat a dic to store all teh childNodes as keys in it
    global term1_is_a
    #for all terms of parentalNode
    for term1 in term_is_a[p]:
        if term1 not in term1_is_a:
            term1_is_a[term1]=0
            #if the childNode also act as a parantalNode, conduct it again
            if term1 in term_is_a:
                function1(term1)
    #return the childNode number
    return len(term1_is_a)

total = []
translation = []
for term in terms:
    ids = term.getElementsByTagName('id')[0].childNodes[0].data
    defstr = term.getElementsByTagName('defstr')[0]
    child_dic = {}
    total_child = 0
    if ids in term_is_a:
        total_child = function1(ids)
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
plt.ylabel('childnodes number')
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















