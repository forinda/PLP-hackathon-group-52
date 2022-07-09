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


from datetime import datetime
from time import sleep, time


def logger_decorator(func):
    """Decorator for logging current executing function"""
    def wrapper(*args, **kwargs):
        with open('nutrition-logs.log', '+a') as f:
            f.writelines(
                f"* Running {func.__name__} method -  on {datetime.now().strftime('%A %d %B %Y %H:%M:%S')}\n")
        print("Running {} function".format(func.__name__))

        return func(*args, **kwargs)
    return wrapper


def timer(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        with open('bench-mark-logs.log', '+a') as f:
            f.write(
                f'*Function {func.__name__!r} executed in {(t2-t1):.4f}s\n')
        return result
    return wrap_func


class NutritionCommands:
    calories_from_fat = 'calories_from_fats'
    calories_from_carbs = 'calories_from_carbs'


class Nutrition(object):

    CARBOHYDRATES_PER_GRAM = 4
    FAT_PER_GRAM = 9

    def __init__(self):
        self._fat_grams = 0
        self._carb_grams = 0

    @property
    @timer
    def fat_grams(self):
        return self._fat_grams

    @fat_grams.setter
    @timer
    def fat_grams(self, value):
        self._fat_grams = value

    @property
    @timer
    def carb_grams(self):
        return self._carb_grams

    @carb_grams.setter
    @timer
    def carb_grams(self, value):
        self._carb_grams = value

    @timer
    @logger_decorator
    def calculate_calories_from_fat(self):
        calories_from_fat = self.fat_grams * self.FAT_PER_GRAM
        return calories_from_fat

    @timer
    @logger_decorator
    def calculate_calories_from_carbs(self):
        calories_from_carbs = self.carb_grams * self.CARBOHYDRATES_PER_GRAM
        return calories_from_carbs

    @timer
    @logger_decorator
    def get_fat_input(self):
        try:
            return int(input('Enter the number of fat grams: '))
        except ValueError:
            print("Value error")

    @timer
    @logger_decorator
    def get_carb_input(self):
        try:
            return int(input('Enter the number of carb grams: '))
        except ValueError:
            print("Value error")

    @timer
    @logger_decorator
    def process(self):
        print(' Welcome to calories converter '.center(50, '*'))
        command = ""
        while command != 'quit' or command != 'q' or command != 'exit':
            command = input(
                "Select \n1 Get calories from fats \n2 Get calories from carbohydrates:\n")
            if command == '1':
                self.fat_grams = self.get_fat_input()
                print('*' * 50)
                print('** Calories from fat  = ',
                      self.calculate_calories_from_fat())
                print('*' * 50)
                continue
            elif command == '2':
                self.carb_grams = self.get_carb_input()
                print('*' * 50)
                print('* Calories from carbohydrates is =  ',
                      self.calculate_calories_from_carbs())
                print('*' * 50)
                continue
            elif command == 'quit' or command == 'q' or command == 'exit':
                print('Goodbye')
                return False
            else:
                print('Invalid command')
                continue


if __name__ == '__main__':
    def main():
        nutrition = Nutrition()
        nutrition.process()
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nCTRL + C closing terminal... in 2 seconds\n")
        sleep(2)
    except KeyError:
        print("Key error.....")
