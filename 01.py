x = input('Please input:\n')
# '5 7' -- '5', '7'
y = x.split()
z =map(int,y)
n1,n2 = z
#n1,n2 = map(int, x.split())
print(n1 +n2)