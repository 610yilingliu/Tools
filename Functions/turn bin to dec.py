def bin(string):
    dec=0
    k=1
    for i in range(len(string)-1,-1,-1):
        dec=dec+int(string[i])*k
        k*=2
    return dec
def main():
    k=str(input("input a bin number"))
    print(bin(k))
main()


