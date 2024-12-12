S=int(input("INPUT s:"))
L=int(input("INPUT l:"))
n=int(input("INPUT n:"))
W=int(input("INPUT w:"))
F=int(input("INPUT F:"))
RES=F ** n
RSB=(S*L)/F
RSSB=(20/F)**W
Denom=20**n/3
bracket_sum=RSB+RSSB
Numerator=RES*bracket_sum
Total_sum=Numerator/Denom
Y=L-Total_sum
print(Y)