t =int(input())
v =int(input())
wcf =35.74 + (0.6215*t) + ((0.4275*t) - 35.75) * pow(v,0.16)
print(f"{wcf:.2f}")