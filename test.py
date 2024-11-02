class MyClass:
    def method1(self, arg1):
        print(f"Executing method1 with arg1: {arg1}")
    
    def method2(self, arg1, arg2):
        print(f"Executing method2 with arg1: {arg1}, arg2: {arg2}")
    
    def method3(self):
        print("Executing method3")

# Create the method mapping
method_map = {
    "action1": MyClass.method1,
    "action2": MyClass.method2,
    "action3": MyClass.method3
}

# Create an instance of the class
my_instance = MyClass()

# Use the mapping to call methods with arguments
actions = [
    ("action1", ["Hello"]),
    ("action3", []),
    ("action2", ["World", 42])
]

for action, args in actions:
    if action in method_map:
        method = method_map[action]
        method(my_instance, *args)