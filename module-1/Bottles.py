


bottleCount = int(input("how many bottles are on the wall?"))

def bottlesOfBeerOnTheWall(bottleCount):
    while bottleCount >=1:
        if bottleCount == 1:
            print(f'''{bottleCount} bottle of beer on the wall
{bottleCount} bottle of beer. Take one down pass it around there are no more bottles of beer on the wall''')
            bottleCount -= 1
        else:
            print(f'''{bottleCount} bottles of beer on the wall
{bottleCount} bottles of beer.''')
            bottleCount = bottleCount - 1
            print(f"Take one down pass it around, {bottleCount} bottles of beer on the wall\n")

bottlesOfBeerOnTheWall(bottleCount)    

