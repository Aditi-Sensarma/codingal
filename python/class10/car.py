class Car:
    def __init__(self, brand, model):
        self.is_started = False
        self.brand = brand
        self.model = model

    def start(self):
        self.is_started = True
        print("The car is started!")
    def stop(self):
        self.is_started = False
        print("The car is stopped!")
    def display_info(self):
        print(f"Car status:{self.is_started} Brand name {self.brand} Car model {self.model}")

    
BMW = Car("BMW","X5")
Tesla = Car("Tesla","Model 3")

BMW.display_info()
BMW.start()
BMW.display_info()

Tesla.display_info()
Tesla.start()
Tesla.display_info()
Tesla.stop()

BMW.model=input("Enter the model of the BMW")
BMW.display_info()

