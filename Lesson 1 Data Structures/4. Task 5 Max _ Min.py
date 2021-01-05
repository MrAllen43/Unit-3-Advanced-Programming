Results = [56,82,91,54,92]

MaxScore = 0

for index in range(0,(len(Results))):
    if Results[index] > MaxScore:
        MaxScore = Results[index]


print(MaxScore)
