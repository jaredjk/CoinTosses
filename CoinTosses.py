import random

for i in range(1,5):
    random_num = random.uniform(0,1) 
    rounded = round(random_num)

    total_heads = 0
    total_tails = 0
    
    if rounded == 1:
        total_heads += 1
        print "Attempt: #{} Throwing a coin.. Its a Head! got {} head(s) so far and {} tail(s) so far".format(i,total_heads, total_tails)
    else:
        total_tails += 1
        print "Attempt: #{} Throwing a coin.. Its a Tail! got {} head(s) so far and {} tail(s) so far".format(i,total_heads, total_tails)


# x_rounded = round(x)
# y_rounded = round(y)
# print x_rounded, y_rounded