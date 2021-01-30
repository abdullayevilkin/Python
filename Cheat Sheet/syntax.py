# >> Variables in Python

name = "asdf"
name = "xxx"
print(name)

a = 10
b = a
print(a)
print(b)

a = 20
print(a)
print(b)


# >> String formatting
greeting = "hello " + name
print(greeting + f" xx i am {a+b}")

print("Hello {}".format("Jack"))


# >> Get user input
# user_age = int(input("Enter your age"))
# month = user_age * 12
# print(f"You are a live {month} month.")


# >> Lists, Tuples and Sets
l = ["iqo", "xoe", "joo"] 
print(l[1])
l.append("zoo6")
print(l)

t = ("zx", "cx", "mx")
print(t)
# NOTE: list and tuple main difference is list can modify tuple cannot