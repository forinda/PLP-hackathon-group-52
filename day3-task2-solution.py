"""
Challenge Task Two (Day 3)

Calories from Fat and Carbohydrates A nutritionist who works for a fitness club helps
members by evaluating their diets. As part of her evaluation, she asks members for the
number of fat grams and carbohydrate grams that they consumed in a day. Then, she
calculates the number of calories that result from the fat, using the following formula:
Calories from fats fat grams * 9
Next, she calculates the number of calories that result from the carbohydrates, using
the following formula:
Calories from carbs carb grams * 4
The nutritionist asks you to write a program that will make these calculations.
    """
def calculatecaloriesfromfat(fatgrams):
    caloriesfromfat = fatgrams * 9
    return{caloriesfromfat}

caloriesfromfat = 'calculatecaloriesfromfat',('userfatgrams')
caloriesfromcarb = 'calculatecaloriesFromcarb',('userCarbGrams')

def calculatecaloriesfromcarbs(carbgrams):
    caloriesfromcarbs = carbgrams * 4
    return 'caloriesfromcarbs'

def main():
    userfatgrams = float(input("enter fat grams"))
    usercrabgrams = float(input("enter carbohydrates grams"))


print("calories from Fat: " + str["caloriesfromfat", ".2f"],("calories from Carbs: ") + str['caloriesFromCarbs', ".2f"])
main()