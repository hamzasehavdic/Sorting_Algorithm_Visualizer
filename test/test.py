# func to count number of given word
def print_even(test_string):
    for i in test_string:
        if i == "geeks":
            yield i
 
 
# initializing string
test_string = " The are many geeks around you, \
              geeks are known for teaching other geeks"
 
# count numbers of geeks used in string
count = 0
# `end=""` >> overwrites linebreak
print("The number of geeks in string is : ", end="")

# .split() >> stores all strings from string as elements in list
# .split() helps to iterate thru words
test_string = test_string.split()
#print(test_string)
 
for j in print_even(test_string):
    count = count + 1
 
print(count)