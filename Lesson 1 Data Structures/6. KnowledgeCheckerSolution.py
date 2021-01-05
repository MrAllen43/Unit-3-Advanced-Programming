Films =[]

for index in range(0,4):
    Films.append(input("Enter a film that you have seen recently: "))

print(Films)

SeenFilm = input("Enter a film's name to see if you have already seen the film: ")

for index in range (0,(len(Films) - 1)):

    if Films[index] == SeenFilm:

        print("You have already seen this film")

    else:

        print("you have not seen this film")


