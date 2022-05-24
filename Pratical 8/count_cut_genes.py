#import the module
import re
#ask user to unput a fasta file
fa="D:\\GIT\\IBI1_2021-22\\Pratical 8\\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa"
#read the input file
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
#ask the user to set a new file to write the results into
f=open(input(),"x")
#search if there are digestive sites, and count the fragements after enzyme digestion
for seqName,seq in readFa(fa):
    if seq.find('GAATTC'):
        seqLen = len(seq)
        n=seq.count('GAATTC')
        f.write(str(seqName)+' '+str(n)+'\n'+seq+'\n')
    else:
        continue
f.close()

