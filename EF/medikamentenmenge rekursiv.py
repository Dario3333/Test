def medikamentenmenge(n):
    if n == 0:
        return 0
    else:
        return 5 + medikamentenmenge(n-1)*0.6
    

n = 10
print(medikamentenmenge(n))