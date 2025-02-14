popA = 80
popB = 200
anos = 0
taxa_a = 1 + (3/100)
taxa_b = 1 + (1.5/100)
while True:
    popA *= taxa_a
    popB *= taxa_b
    anos += 1
    if popA == popB or popA > popB:
        break
print(anos)