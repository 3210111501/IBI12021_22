#define a function that can align two sequences
edit_distance=0
def alignment(seq1,seq2):
    global edit_distance
    for i in range(len(seq1)):
        if seq1[i]!=seq2[i]:
           edit_distance+=1
#set alignment score equals to edit_distance
    print("alignment score=",edit_distance)


#define a function that can calculate the percentage of indentical amino acides for each comparison
def percentage(x,y):
    if len(x)>=len(y):
        p=x
    else:
        p=y
    alignment(x,y)
    percentage=edit_distance/len(p)
    print(percentage)

#define a function which can read fasta document
def readFa(fa):
    with open(fa, 'r') as FA:
        seqName, seq = '', ''
        while 1:
            line = FA.readline()
            line = line.strip('\n')
            if (line.startswith('>') or not line) and seqName:
                yield ((seqName, seq))
            if line.startswith('>'):
                seqName = line[1:]
                seq = ''
            else:
                seq += line
            if not line: break

#read three documents and get three sequences
fa = "C:/Users/zuojingyi/GIT/IBI1_2021-22/Practical10/DLX5_human.fa"
for (seqName,seq) in readFa(fa):
    a=seq
print(a)
fa = "C:/Users/zuojingyi/GIT/IBI1_2021-22/Practical10/DLX5_mouse.fa"
for (seqName,seq) in readFa(fa):
    b=seq
print(b)
fa = "C:/Users/zuojingyi/GIT/IBI1_2021-22/Practical10/RandomSeq(1).fa"
for (seqName,seq) in readFa(fa):
    c=seq
print(c)

#every time you output a result, make the global variable into 0
percentage(a,b)
edit_distance=0
percentage(b,c)
edit_distance=0
percentage(a,c)











