cnt = int(input())
print(" "*(cnt-1) + "*")
if(cnt!=1):
    for i in range(1,cnt-1):
        print(" " * (cnt-1-i) + "*" + " " * (2*i-1) + "*")
    print("*" * (2*cnt-1))