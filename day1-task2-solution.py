"""
Sales Tax Challenge – Task Two (Day 1)
A painting company has determined that for every 115 square feet of wall space, one
gallon of paint and eight hours of labor will be required. The company charges $20.00
per hour for labor. 
Write a program that asks the user to enter the square feet of wall
space to be paint and the price of the paint per gallon. The program should display
the following data:
• The number of gallons of paint required
• The hours of labor required
• The cost of the paint
• The labor charges
• The total cost of the paint job
"""


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        print('-' * 50)
        print("Running {} function".format(func.__name__))
        print("-" * 50)
        return func(*args, **kwargs)
    return wrapper


class PaintingCompany(object):
    UNIT_AREA_IN_FEET = 115
    HOURLY_FEE_RATE = 20

    def __init__(self) -> None:
        self._area_to_paint = 0
        self._gallon_price = 0
        self.unit_area = 0

    @property
    @logger_decorator
    def area_to_paint(self) -> float:
        # Area setter for the area to be painted
        return self._area_to_paint

    @area_to_paint.setter
    @logger_decorator
    def area_to_paint(self, value: float) -> None:
        # Area setter for the area to be painted
        self._area_to_paint = value

    @property
    @logger_decorator
    def gallon_price(self) -> float:
        # Getter for price of a gallon of paint
        return self._gallon_price

    @gallon_price.setter
    @logger_decorator
    def gallon_price(self, value: float) -> None:
        # Setter for price of one gallon of paint
        self._gallon_price = value

    @staticmethod
    @logger_decorator
    def utility_converter():
        # 115 sq ft ->  8hrs and $20 per hour labour
        pass

    @logger_decorator
    def get_user_input(self) -> None:
        # Get user input for area to be painted and price of a gallon of paint
        self.area_to_paint = int(
            input("enter the square feet of wall space to be painted: "))
        self.gallon_price = int(
            input("enter the price of the paint per gallon: "))
        self.unit_area = int(self.area_to_paint/self.UNIT_AREA_IN_FEET) \
            if (self.area_to_paint %
                self.UNIT_AREA_IN_FEET == 0) \
            else \
            int(self.area_to_paint/self.UNIT_AREA_IN_FEET) + 1

    @logger_decorator
    def input_mapper(self) -> dict:
        try:
            self.get_user_input()

            number_of_gallons_of_paint_required = self.unit_area
            hours_of_labor_required = self.unit_area * 8
            cost_of_the_paint = number_of_gallons_of_paint_required * self.gallon_price
            labor_charges = int(hours_of_labor_required * self.HOURLY_FEE_RATE)
            total_cost_of_the_paint_job = cost_of_the_paint + labor_charges
            return {
                "number_of_gallons_of_paint_required": number_of_gallons_of_paint_required,
                "hours_of_labor_required": hours_of_labor_required,
                "cost_of_the_paint": cost_of_the_paint,
                "labor_charges": labor_charges,
                "total_cost_of_the_paint_job": total_cost_of_the_paint_job
            }
        except Exception as e:
            print(e)
        return {
            "number_of_gallons_of_paint_required": None,
            "hours_of_labor_required": None,
            "cost_of_the_paint": None,
            "labor_charges": None,
            "total_cost_of_the_paint_job": None
        }

    @logger_decorator
    def replace_chars(self, string: str) -> str:
        return string.title().replace("_", " ").replace("\"", "").replace("  ", " ").replace(":", " = ")

    @logger_decorator
    def run(self):
        number_of_gallons_of_paint_required, \
            hours_of_labor_required, cost_of_the_paint, \
            labor_charges, total_cost_of_the_paint_job\
            = self.input_mapper().values()
        output = f"""
number_of_gallons_of_paint_required: {number_of_gallons_of_paint_required},
hours_of_labor_required": {hours_of_labor_required},
cost_of_the_paint": {cost_of_the_paint},
labor_charges": {labor_charges},
total_cost_of_the_paint_job": { total_cost_of_the_paint_job}
        """
        print(self.replace_chars(output))


if __name__ == "__main__":
    @logger_decorator
    def main():
        while True:
            painting_company = PaintingCompany()
            painting_company.run()
            if input("Do you want to continue? (y/n): ") == "n":
                break
    main()
