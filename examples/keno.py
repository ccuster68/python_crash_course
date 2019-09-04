from random import randint
import array

num_plays=0
num_3wins=0
num_2wins=0
tries=40
winners=[]
picked = []
num_wins = [0,0,0,0]

while tries>0:
    n=0
    winners=[]
    tries-=1
    hits=0
    num_plays+=1
    
    while n < 20:
        pick = randint(1,80)
        if pick not in winners:
            winners.append(pick)
            n += 1
        
            if pick in [1,2,3]:
                hits+=1  
    
    if hits == 4:
        tries += 12 
        num_wins[2] += 1           
    elif hits == 3:
        tries += 3
        num_wins[1] += 1
    elif hits==2:
        tries += 0
        num_wins[0] += 1
    elif hits==5:
        tries += 810
        num_wins[3] += 1
    


print (f"Number of plays:{num_plays}")
#print (f"Number of 5 wins:{num_wins[3]}")
#print (f"Number of 4 wins:{num_wins[2]}")
print (f"Number of 3 wins:{num_wins[1]}")
print (f"Number of 2 wins:{num_wins[0]}")


