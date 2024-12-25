
#cfg to pda
nt=int(input("\nEnter the number of non terminals capital letters():"))
NT=[]
for i in range(nt):
    print("\nEnter the non terminal:",i+1)
    item=input()
    NT.append(item)

t=int(input("\nEnter the number terminals(small letters):"))
T=[]
for i in range(t):
    print("\nEnter the non terminal:",i+1)
    item=input()
    T.append(item)
p=int(input("\nEnter the number production:"))
tempr=[]
for i in range(p):
    print("\nEnter the production symbols:",i+1)
    item=input()
    tempr.append(item)
print(tempr)
pr={}
for i in tempr:
    pr[i]={}
    print("\nEnter the production for ",i,":")
    pr[i]=input()
print(pr)
states=['q0','q1','q2']
print("\n The transitions for the cfg to PDA are : ")
print(f"&(q0,^,z0)=(q1,{tempr[0]}-z0)")
for i in tempr :
    print(f"&(q1,^,{i})=(q1,{pr[i]})")
for i in T :
    print(f"&(q1,{i},{i})=(q1,^)")
print("&(q0,^,q2)=(q1,z0)")