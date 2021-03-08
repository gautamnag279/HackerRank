#Using the count sort algorithm
num = input()
count = [0]*6
for i in map(int , input().strip().split()):
    count[i] = count[i] + 1
print(count.index(max(count)))


#Using HashMap
def migratoryBirds(arr):
    most = 1
    hashMap = {1:0,2:0,3:0,4:0,5:0}
    for i in arr:
        hashMap[i]+=1  
        if hashMap[i] > hashMap[most]:
            most = i
        elif hashMap[i] == hashMap[most] :
            if i < most:
                most = i
            
    return most
print(migratoryBirds([2, 2, 1, 1]))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

