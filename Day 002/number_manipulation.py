print(round(8 / 3, 2))          # 2.67
print(round(8 / 3, 5))          # 2.66667

print((8 // 3))                 # 2
print(4 / 2)                    # 2.0

result = 4 / 2
result /= 2
print(result)                   # 1.0

score = 55
score += 1
score -= 1
score *= 2
score /= 3


# f-strings
print("Your score is " + str(2200))
isWinning = True
finalScore = 500208
toPrint = f"Situation: your final score is {finalScore}, and you are winning is {isWinning}"
print(toPrint)
numberDecimals = 0.123456789
print(f"Print three decimals of {numberDecimals}: {numberDecimals:.3f}")
