codes_and_cities = {
    "LAX": "Los Angeles",
    "LGA": "New York City",
    "IAH": "Houston",
    "BOI": "Boise",
    "SEA": "Seattle",
    "GSP": "Greenville",
}

people_ages = {
    "Alizeh": 24,
    "Haris": 21,
    "Idris": 39,
    "Nia": 42,
    "Talia": 31,
}

# == codes_and_cities = {"LAX":"Los Angeles","LGA":"New York City","IAH":"Houston","BOI":"Boise","SEA":"Seattle","GSP":"Greenville",}

code = input("What's the airport code?")

# This will return None if the key does not exist
city = codes_and_cities.get(code)
print("The city for", code, "is", city)

# This will cause an error if the value in code
# is not a key in the dictionary, like "BOO"
city = codes_and_cities[code]
print("The city for", code, "is", city)

# Add Flagstaff with the airport code FLG
codes_and_cities["FLG"] = "Flagstaff"
print(codes_and_cities.get("FLG"))

# Add Minneapolis
codes_and_cities["MSP"] = "Minneapolis"
print(codes_and_cities["MSP"])

# Remove Houston
del codes_and_cities["IAH"]
print(codes_and_cities.get("IAH", "NOTHING!"))

# Ask the human to provide a code and city
# and store those.
code = input("Please gimme an airport code. ")
city = input("Please tell me what city that's in. ")
codes_and_cities[code] = city

wants_six_entries = {
    "crew": "t-shirt",
    "mock": "turtle neck",
    "khakis": "pants",
    "ankle": "socks",
}

wants_six_entries["word"] = "nope"
wants_six_entries["words"] = "nopes"

numbers_to_words = {
  1: "one",
  2: "two",
  3: "three",
}

for key in numbers_to_words:
    print("The key is key:", key)

    # Use the key to get the value from
    # the dictionary
    value = numbers_to_words[key]
    print("The associated value is:", value)

a = 10
b = 10
c = (1,2,3,4)
d = (1,2,3,4)
e = "hello"
f = "hello"

a is 10 # evaluates to True
c is d # evaluates to False
e is not f # evaluates to False
a is not e # evaluates to True

# Correct way to compare to None
if x is None:
    print("x is None")


# Incorrect way to compare to None
if x == None:
    print("x is None and we shouldn't use ==")


# same location in mem
a=3
b=3

print(id(a))
print(id(b))


# diff location because diff types
a=3.0
b=3

print(id(a))
print(id(b))

# same mem
a="hello"
b="hello"

print(id(a))
print(id(b))

# diff mem
a=[1,2,3,4]
b=[1,2,3,4]

print(id(a))
print(id(b))


# diff mem
a=(1,2,3,4)
b=(1,2,3,4)

print(id(a))
print(id(b))

# lists and tuples do not have same mem loc (variables with literal types that can hold more than one value)
a = [1,2,3,4]
b = [1,2,3,4]
a == b # True
a is b # False
a is not b # True

# int-assigned variables do (variables with literal type that holds one value)
a = 3
b = 3
a == b # True
a is b # True
a is not b # False

4 < 2 and 4 > 2
1 > 2 and 4 < 10
4 < 10 or 1 < 2
10 == 10 or 5 == 7
10 == 10 and 5 == 7
not True
not False

10 == 15 and 25 == 50
10 == 15 or 25 == 50
not 10 == 15 and not 25 == 50

if some_list:
    # only do stuff if the list has values in it
else:
    # do stuff because the list is empty

if some_number:
    # only do stuff if the number is not zero
else:
    # do stuff because the number is zero
