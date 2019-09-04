from random import choice

all_char = ['A','B','C','D','E']

for x in range(1,11):
    all_char.append(x)


tries=0
winners='losers'
while '123AB' != ''.join(sorted(winners)):
    n=0
    winners=''
    tries+=1
    while n < 5:
        pick = str(choice(all_char))
        if pick not in winners:
            n+=1
            winners+=pick


print (f"it took {tries} to win!")



