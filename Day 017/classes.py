# class must have content, at least pass
class Empty:
    pass


# class naming PascalCase
# NOT camelCase (anywhere in python)
# NOT snake_case (for class but everywhere else in python)!
class User:
    pass


user_1 = User()
user_1.id = '23nfo35nep'
user_1.username = 'Angela'
print(user_1.id)
print(user_1.username)


# CONSTRUCTOR:
class Person:

    def __init__(self, name, age, favorite_colour):
        print("New person being created!")
        self.name = name
        self.age = age
        self.favorite_colour = favorite_colour
        self.friends = []

    def get_older(self, number_of_years):
        self.age += number_of_years

    def make_friends(self, friend):
        self.friends.append(friend)
        friend.friends.append(self)


person_1 = Person("Angela", 33, "purple")
print(person_1.name)
print(person_1.age)
print(person_1.favorite_colour)
print(person_1.friends)

person_1.get_older(5)
print(person_1.age)

person_2 = Person("Michael", 40, "green")
person_3 = Person("Jack", 88, "blue")
person_1.make_friends(person_2)
person_1.make_friends(person_3)
print(len(person_1.friends))
print(person_1.friends[0].name)
print(person_1.friends[1].name)
print(len(person_2.friends))
print(person_2.friends[0].name)


