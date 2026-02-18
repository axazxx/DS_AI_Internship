#task 1

s = [["click","scroll"],["click","click"],["click","scroll"],
     ["scroll","exit"],["click","exit"],["scroll","exit"],["scroll","click"]]
p = len(s)
x=0
for i in s:
    for j in i:
        if j == "click":
            x=x+1
            break
print("Probability of click atleast once",x/p)


s2 = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],
      [2,1],[2,2],[2,3],[2,4],[2,5],[2,6],
      [3,1],[3,2],[3,3],[3,4],[3,5],[3,6],
      [4,1],[4,2],[4,3],[4,4],[4,5],[4,6],
      [5,1],[5,2],[5,3],[5,4],[5,5],[5,6],
      [6,1],[6,2],[6,3],[6,4],[6,5],[6,6]]
n2=len(s2)
sum=0
for l in s2:
    if l[0]+l[1] == 7:
        sum+=1
print("Probability of sum being 7:",sum/n2)

#task 2

p_dice = 1/6
p_coin = 0.5
p_both = p_dice * p_coin
print("Probability of Heads on a coin AND rolling a 6 on a die =",p_both)


nr = 5
nb = 5
p_red = nr/(nr+nb)
p_blue = nb/(nr+nb)
p_redred = p_red * (nr-1)/(nr+nb-1)
print("Probability that both balls are red",p_redred)

#task 3

p_spam = 0.1
p_ham = 0.9
p_free_given_spam = 0.9
p_free_given_ham = 0.05

p_free = (p_free_given_spam * p_spam) + (p_free_given_ham * p_ham)
p_spam_given_free = (p_free_given_spam * p_spam) / p_free
print("Probability that an email containing 'Free' is spam = ", p_spam_given_free)
