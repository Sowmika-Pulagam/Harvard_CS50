def main():
    fruit = input("Item: ")
    calfruit(fruit)



def calfruit(fruit):
    fruits = {
        "apple":"130",
        "Avocado":"50",
        "Sweet Cherries":"100",
        "Banana":"110",
        "Grapes":"90",
        "Grapefruit":"60",
        "Kiwifruit":"90",
        "Lemon":"15",
        "pear":"100"

    }
    if fruit in fruits:
        print("Calories:",fruits[fruit])

main()






