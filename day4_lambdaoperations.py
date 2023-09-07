a=int(input())
b=int(input())
print("arithmetic operators")
x1=lambda a1,b1:a1+b1
print("addition a+b ",x1(a,b))
x2=lambda a2,b2:a2-b2
print("subtraction a-b ",x2(a,b))
x3=lambda a3,b3:a3*b3
print("multiplication a*b ",x3(a,b))
x4=lambda a4,b4:a4/b4
print("division a/b ",x4(a,b))
x5=lambda a5,b5:a5//b5
print("floor division a//b",x5(a,b))
x6=lambda a6,b6:a6%b6
print("modulus a%b ",x6(a,b))
x7=lambda a7,b7:a7**b7
print("exponentiation a**b ",x7(a,b))
print("relational operators")
x8=lambda a8,b8:a8>b8
print("greater than a>b ",x8(a,b))
x9=lambda a9,b9:a9<b9
print("less than a<b ",x9(a,b))
x10=lambda a10,b10:a10>=b10
print("greater than or equal a>=b ",x10(a,b))
x11=lambda a11,b11:a11<=b11
print("less than or equal to a<=b",x11(a,b))
x12=lambda a12,b12:a12==b12
print("equal to a==b ",x12(a,b))
x13=lambda a13,b13:a13!=b13
print("not equal to a!=b",x13(a,b))
print("logocal operators")
x14=lambda a14,b14: a14<b14 and a14>b14
print("logical and operator a<b and a>b",x14(a,b))
x15=lambda a15,b15:a15>=b15 or a15<=b15
print("logical or operator a>=b or a<=b",x15(a,b))
x16=lambda a16,b16:not a16==b16
print("logical not operator not a==b",x16(a,b))
print("bitwise operator")
x17=lambda a17,b17:a17 &b17
print("bitwise and a&b",x17(a,b))
x18=lambda a18,b18:a18 | b18
print("bitwise or a | b",x18(a,b))
x19=lambda a19:~a19
print("bitwise not ~a",x19(a))
x20=lambda a20,b20:a20 ^ b20
print("bitwise xor a^b ",x20(a,b))
x21=lambda a21:a21>>1
print("bitwise right shift a>>",x21(a))
x22=lambda a22:a22<<1
print("bitwise left shift a<<",x22(a))
m=input()
n=input()
print("membership operator")
x23=lambda m1,n1:m1 in n1
print("membership in x in y",x23(m,n))
x24=lambda m2,n2: m2 not in n2
print("membership not in x not in y",x24(m,n))
print("Identity operator")
x25=lambda m3,n3: m3 is n3
print("identity operator i x is y",x25(m,n))
x26=lambda m4,n4: m4 is not n4
print("identity operator is not x is not y",x26(m,n))