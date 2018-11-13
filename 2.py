sum = 0
fibPrev = 1
fibTemp = 0
fibCurrent = 0
while fibCurrent <= 4000000:
    fibCurrent = fibTemp + fibPrev
    if fibCurrent % 2 == 0:
        sum += fibCurrent
    fibTemp = fibPrev
    fibPrev = fibCurrent
print(sum)
