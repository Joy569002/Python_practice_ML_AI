#oop
class User:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def run(self):
        print(f"run {self.name} or die at {self.age} years old")
class Driver(User):
    def __init__(self,name,age):
        super().__init__(name,age)
    def carname(self):
        print(f"Has BMW ,licensed {self.name}")
#inheritance
class Information(User):
    def __init__(self,name,age):
        #called constructor using super
        super().__init__(name,age)
    def JobInfo(self):
        print(f"Has reall cool job at {self.age} years old")
#multiple inheritance
class Me(Driver,Information):
    def __init__(self,name,age):
        super().__init__(name,age)

def main():
        me = Me("James", 25)
        me.JobInfo()
        me.carname()
        me.run()
if __name__ == "__main__":
    main()
