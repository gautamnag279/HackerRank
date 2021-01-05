if __name__ == '__main__':
    N = int(input())
    L = []
for _ in range(N):
    #*args is used to pass a variable number of arguments
    command, *args = input().split()
    try:
        getattr(L, command)(*(int(x) for x in args))
    except AttributeError:
        print(L)
