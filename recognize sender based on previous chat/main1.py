from nltk.tokenize import word_tokenize
from nltk import FreqDist
import sys

reload(sys)

sys.setdefaultencoding('Utf8')

pers1file = open('pers1','r')
pers2file = open('pers2','r')

pers1words = list()
pers2words = list()

txt = pers1file.readlines()

for line in txt :
       l = line.strip('\n').lower()
       pers1words+= word_tokenize(str(l))

txt = pers2file.readlines()

for line in txt :
      l = line.strip('\n').lower()
      pers2words+= word_tokenize(str(l))

pers1file.close()
pers2file.close()  

pers1wordfeq = FreqDist(pers1words)
pers2wordfeq = FreqDist(pers2words)

pers1word_prob = {}
pers2word_prob ={}


for x in pers1wordfeq :
      pers1word_prob[x] = float(pers1wordfeq[x])/float(len(pers1words))

for x in pers2wordfeq :
      pers2word_prob[x] = float(pers2wordfeq[x])/float(len(pers2words))



print "Enter the sentence :"

stmnt = raw_input()

stmnt = stmnt.lower()

test_words = word_tokenize(stmnt)

pers1_prob = 0.5
pers2_prob = 0.5

pers1_word_list = pers1wordfeq.keys()
pers2_word_list = pers2wordfeq.keys()


for x in test_words :
     if x in pers1_word_list and x in pers2_word_list :
           pers1_prob = pers1_prob*pers1word_prob[x]
           pers2_prob = pers2_prob*pers2word_prob[x]
     elif x not in pers2_word_list and x in pers1_word_list :
           pers1_prob = pers1_prob*pers1word_prob[x]
           pers2_prob = pers2_prob*min(pers2word_prob.values())
     elif x not in pers1_word_list and x in pers2_word_list :
           pers2_prob = pers2_prob*pers2word_prob[x]
           pers1_prob = pers1_prob*min(pers1word_prob.values())
           

pers1f = pers1_prob/(pers1_prob+pers2_prob)
pers2f = pers2_prob/(pers1_prob+pers2_prob)

print " person_1 probability : ",pers1f
print " person_2 probability : ",pers2f

if pers1f > pers2f :
    print " person_1 might have said this sentence/statement"
else :
     print " person_2 might have said this sentence/statement"
 
