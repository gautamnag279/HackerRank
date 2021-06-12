n , k = [int(i) for i in input().strip().split()]
s = [int(i)%k for i in input().strip().split()] #stores the remainder

remainder=[0]*k
count = 0

for i in s:
    remainder[i] += 1
for i in range(1 , k//2):
    count += max(remainder[i] , remainder[k-i])
    
if remainder[0]>0:
    count += 1
if k%2==0 and remainder[k//2]>0:
    count += 1
elif k%2==1 and k>1:
    count += max(remainder[k//2] , remainder[k-k//2])

    print(count)
