def kapital(n,g,z):
    if n == 0:
        return g
    else:
        return kapital(n-1,g,z)*z
    
n = int(input("Nach wie vielen Jahren möchtest du den Zins wissen?"))
g = int(input("Wie gross ist das Startkapital?"))
a = int(input("Wie gross ist der Zinssatz in Prozent?"))
z = a/100 + 1
print(kapital(n,g,z))
