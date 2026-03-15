class ClassTest:
    def instance_method(self):
        print(f"Called instance_method of {self}")
        # print(f"Called instance_method of '{self.__class__.__name__}'.")

    @classmethod
    def class_method(cls):
        print(f"Called class_method of {cls}")
    
    @staticmethod
    def static_method():
        print("Called static_method.")


test1 = ClassTest()
test1.instance_method()
ClassTest.instance_method(ClassTest())
print()
ClassTest.class_method()
print()
ClassTest.static_method()
