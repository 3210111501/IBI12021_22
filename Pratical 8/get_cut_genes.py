#import the module
import re
#"D:\GIT\IBI1_2021-22\Pratical 9\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
#The instruction on https://blog.csdn.net/qq_18369669/article/details/103408600 is used as the reference of the code.
def readFa(fa):
    with open(fa,'r') as FA:
        seqName,seq='',''
        while 1:
            line=FA.readline()
            line=line.strip('\n')
            if (line.startswith('>') or not line) and seqName:
                yield(seqName,seq)
            if line.startswith('>'):
                seqName=line.strip("gene:")[1:8]
                seq=''
            else:
                seq+=line
            if not line:break
fa="D:\\GIT\\IBI1_2021-22\\Pratical 8\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
#set a new fasta file to write the results into
f=open("cut_genes.fa","x")
#find whether there are digestive sites in the sequence, if there are digestive sites, then write the name and the length into the file.
for seqName,seq in readFa(fa):
    if seq.find('GAATTC'):
        seqLen = len(seq)
        f.write(str(seqName)+' '+str(seqLen)+'\n'+seq+'\n')
    else:
        continue
#close the file
f.close()


























