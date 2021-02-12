fizzbuzz = " "

başla = int(input("başlama sayısı:"))
sonlandır = int(input("bitiş sayısı:"))

for i in range(başla,sonlandır+1):
    if i%3 == 0:
        fizzbuzz += "fizz"
    if i%5 == 0:
        fizzbuzz += "buzz"
    if i%3 != 0 and i%5 != 0:
        fizzbuzz += str(i)
    fizzbuzz += " "

print(fizzbuzz)