#Brett Meirhofer 2036955


class FoodItem:
    def __init__(self,name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))


if __name__ == '__main__':
    FirstItem = FoodItem()
    Name = input()
    Fat = float(input())
    Carbs = float(input())
    Protein = float(input())
    SecondItem = FoodItem(Name,Fat,Carbs,Protein)
    Servings = float(input())
    Items = [FirstItem, SecondItem]


    for Item in Items:
        Item.print_info()
        print("Number of calories for {:.2f} serving(s): {:.2f}".format(Servings, Item.get_calories(Servings)))
        if Item != Items[-1]:
            print("")






