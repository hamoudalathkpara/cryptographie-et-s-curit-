"""
import hashlib
fichier=open("rockyou.txt","r", encoding="latin-1")
trouve=False
for mdp in fichier:
    mdp=mdp.strip()   #enleve l'espace présent à chaque ligne
    hache=hashlib.md5(mdp.encode()).hexdigest()  #encode le mot de passe présent sur la ligne
    if hache=="5a74dd4eef347734c8a0a9a3188abd11":
        print("Le mot de passe associé à ce haché est:", mdp)
        trouve=True
        break
if not trouve:
    print("Le mot de passe ne se trouve pas dans ce fichier")
fichier.close()"""

from random import randint
def strassen(n):
    a=2
    while n//2!=1:
        n=n/2
    if n>0 and (n&(n-1))==0:
        if n>2:
            for i in range(n):
                I{i}=[]
        P1=A[0][0] *(B[0][1]-B[1][1])
        P2=(A[0][0] + A[0][1])*(B[1][1])
        P3=(A[1][0] + A[1][1])*(B[0][0])
        P4=A[1][1] *(B[1][0]-B[0][0])
        P5=(A[0][0]+A[1][1]) *(B[0][0]+B[1][1])
        P6=(A[0][1]-A[1][1]) *(B[1][0]+B[1][1])
        P7=(A[0][0]-A[1][0]) *(B[0][0]+B[0][1])
        C[0][0]=P5+P4 - P2+P6
        C[0][1]=P1+P2 
        C[1][0]=P3+P4
        C[1][1]=P5+P1 - P3-P7
        return C
        
    


n=2
A=[[1,2],[3,4]]
B=[[5,6],[7,8]]
#A=[[randint(-10,10) for _ in range(n)] for _ in range(n)]
#B=[[randint(-10,10) for _ in range(n)] for _ in range(n)]
C=[[0 for _ in range(n)] for _ in range(n)]
print(strassen(n))