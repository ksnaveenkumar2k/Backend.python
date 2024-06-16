def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)
a=int(input())
b=int(input())
GCD=gcd(a,b)
print(f"G.C.D of {a} and {b} = {GCD}")