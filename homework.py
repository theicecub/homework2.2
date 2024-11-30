#zadanie 1
class phone1:
    def __init__(self, model):
        self.model = model

class phone2(phone1):
    def __init__(self, model, name):
        super().__init__(model)
        self.name = name

class phone3(phone2):
    def __init__(self, model, name, year):
        super().__init__(model, name)
        self.year = year

class phone4(phone3):
    def __init__(self, model, name, year, processor):
        super().__init__(model, name, year)
        self.processor=processor
    def show_info(self):
        print(f"Phone: {self.model} {self.name}, Year: {self.year}, Processor: {self.processor}")

Samsung = phone4("Samsung", "S21 FE", 2021, "Snapdragon 888")
Samsung.show_info()