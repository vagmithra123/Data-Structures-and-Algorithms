USE list.count() TO COUNT THE NUMBER OF OCCURRENCES OF ONE ELEMENT
Use list.count(value) to count the number of occurrences of value.

a_list = ["a", "b", "a"]

occurrences = a_list.count("a")
count the "a"'s


print(occurrences)
OUTPUT
2
USE collections.Counter() TO COUNT THE NUMBER OF OCCURRENCES OF ALL ELEMENTS
Call collections.Counter() on a list to return the number of occurrences of each element as a Counter object. Specific values of the object can be accessed by callling an index lookup on a value, such as counter_object[value]

a_list = ["a", "b", "a"]

occurrences = collections.Counter(a_list)

object resembles a dictionary

print(occurrences)
OUTPUT
Counter({'a': 2, 'b': 1})
print(occurrences["a"])
OUTPUT
2