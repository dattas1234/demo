for a in range(1,4,2):
    print(a)

else: 
 print("datta")
for x in range(2):
    pass 
print("its working")
def fun(*args):
    for a in args:
        print(a)

fun("datta","kakkad")
def fun4(*kwargs):
    print(kwargs[0:2])
    print(kwargs[1])

fun4("asewe", "faaw")   
def fun33(s="kkr"):
    print(s)
fun33("gass")
fun33("fjsn")
fun33()
def fun44(food):
    for a in food.values():
        print(a)
lis={1:"datta" ,2:"komal",3:"pooja",4:{1:"mom",2:"dad"},5:"man the game"}        
tup=("dataa","soat","ram")        
fun44(lis)   
#lis[4[1]]="kurqrt"   
#fun33(lis)  
for x,y in lis.items():
    print(x,y)
if "katta" in lis.values():
    print("this is working")    
else: 
    print("katta is not present in the dcst.")    
 
print(len(lis))   
lis["mna"]="this is the new value"
#print(lis)
lis.pop(2)
print(lis)
lis.popitem()
print(lis)
lis.popitem()
"""print(lis)
del lis[1]
print(lis)
del lis
print(lis)"""
li={1:"datta",2:"pooja",3:"komal",4:{1:"mom",2:"dad"}}
print(li)
print(len(li))
ne=li.copy()
print(ne)
li["k"]="have fun"
me=li
print(li)
print(me)
li[5]="haiii"
print(me)
me=dict(lis)
print(me)
mer={"first":me,"second":li,"third":ne}
print(mer)
print("\n\n",mer["first"])
ke=dict(datta="hiii",komal="byyy",pooja="niii")
print(ke)

me.clear()
print(me)

val=("datta","prasad","amit","suraj")
va=("friend")
crea = dict.fromkeys(val,va)
print(crea)
print(crea.get("datta"))
crea.items()
print(crea.items())
print(crea.keys())
crea.setdefault("mannu")
print(crea)
crea.update({"kedar":"friend","kishore":"friend"})
print(crea)
var={"car":"audy","game":"fun"}
lis.update(var)
print(lis)
print(crea.values())
a=lambda v:v%2
print(a(2))
print(a(5))
x=lambda a,b,c,d: a+b+c+d

print(x(1,2,4,3))
def fun1(n):
    return lambda a: a*n
doubler=fun1(4)
print(doubler(2))
"""a=2
b=3
c=add(a,b)
print(c)"""
import numpy as kp
arr=kp.array([1,3,2,4,5])
print(arr)
print(kp.__version__)
arr1=kp.array(["datta","Ram","soat"])
print(arr1)
arra2=kp.array([2.3,4.3,3.00,3.4])
print(arra2)
print(type(arra2))
arr3=kp.array(("datta","arra"))
print(arr3)

a=(1,2,3,4,5)
print(a[2])
arr4=kp.array(34)
print(arr4)
arra1=kp.array([[[1,2,3,4],["data","kedar"]],[["kakkad","pakkad"],[3.3,2.3,4.2]]])
print(arra1)
print(arra1.ndim)
print(arr4.ndim)
arra7=kp.array([1,2,3,4],ndmin=5)
print(arra7)
print("the no of dimentin are",arra7.ndim)
class myclass:
    v=22
obj=myclass()
print(obj.v)    
class anewc:
    def __init__(se,name,age):
        se.name1=name
        se.age1=age
    def my1(se):
        print("is't Working!!!")   
obj2=anewc("datta",20)
print(obj2.name1)
print(obj2.age1)
obj3=anewc("kedar",20)
obj3.my1()
obj3.age=22
print(obj3.age)
del obj3
#print(obj3)
class my2:
    pass
v3=my2()
"""import math
a=2
b=4
print(math.add(a+b))"""
class parent():
     def __init__(self,fname,lname):
         self.fname=fname
         self.lname=lname
obj0=parent("Datta","Soat")
print(obj0.fname)     
class child(parent):
     def __init__(self,fname,lname,year):
         #self.mname=fname
         #self.fname=mname 
         super().__init__(fname,lname) 
         self.graduationyear=year
     def welcome(self):
         print("heiiii!!!!! it's working")

objc=child("kedar","Tandle",2022)
print(objc.fname)    
print(objc.graduationyear)
objd=child("datta","soat",2022)
print(objd.fname)
print(objd.graduationyear)
objd.welcome()
mytup=(23,32,44,45,5)
myit=iter(mytup)
print(next(myit))
print(next(myit))
print(next(myit))
sttr="datascience"
nit=iter(sttr)
print(next(nit))
print(next(nit))
print(next(nit))
print(next(nit))
"""class my1():
    def __iter__(self):
         self.a=1
         return self
    def __next__(self):
       if self.a <= 20:
          x=self.a;
          self.a +=1
          return x
       else:
           raise StopIteration   
ob=my1()
ite=iter(ob)
for x in ite:
    print(x)

print(next(ite))
print(next(ite))
print(next(ite))"""
x1=3
def myfun2():
    global x3
    x3= 22
    x1=4
    print("this is the global one",x1)
    x=2
    print("thsi one is outer one",x)
    def myfun3():
        print("this one is global one used in ineer fun ",x1)
        print("this is my ineer fun variable",x)
    myfun3() 


myfun2()
print("this is the global dec in local scope",x3)

from module import fun2
fun2("datta")
import datetime 
x1=datetime.datetime.now()
print(x1)
print(x1.year)
print(x1.strftime("%A"))

x=datetime.datetime(2020,5,16)
print(x)
print(x1.strftime("%%"))
d=datetime.datetime.now()
print(d)
string ="darta"
string+332