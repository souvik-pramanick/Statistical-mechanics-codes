#############################
#Name: Souvik Pramanick
#Semester: 5
#Paper: PHSA CC12 Practical
#Registration no.:
#Roll No.:
#############################
import numpy as np
import matplotlib.pyplot as plt


coin=np.random.randint(0,2,10)  #a coin toss for 10times

die=np.random.randint(1,7,10)  #a ludo die thrown 10 times

playing_cards=np.random.randint(1,53,(3,4)) #3 people drawing playing cards

print('Playing head and tails, tails as 0 and heads as 1: ',coin)

print('Throwing die 10 times: ',die)

print('4 players draw 3 cards randomly:')
print('  A   B  C  D')
print(playing_cards)

plt.suptitle('Board games')
plt.subplot(1,3,1)
plt.hist(coin,bins=2,ec='yellow',label='Coin tossing')
plt.legend(loc='best')


plt.subplot(1,3,2)
plt.hist(die,bins=6,ec='pink',label='Die throwing')
plt.legend(loc='best')


plt.subplot(1,3,3)
plt.hist(playing_cards,ec='green',label='Playing cards')
plt.legend(loc='best')

plt.show()
#############################