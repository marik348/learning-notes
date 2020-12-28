# List Comprehension

List comprehensions are used to derive a new list from an existing list.

~~~
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)
~~~

The advantage of using list comprehensions is that it reduces the amount of boilerplate code required when we use loops to process each element of a list and store it in a new list.