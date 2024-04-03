class Person:
    def __init__(me, name, age, gender):
        me.name = name
        me.age = age
        me.gender = gender

    def __str__(me):
        return f"Name: {me.name}, Age: {me.age}, Gender: {me.gender}"

person1 = Person("Shilpi", 26, "Female")
print(person1)
