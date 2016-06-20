# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Tuples and Lists are basically the same thing EXCEPT Tuples and immutable whereas lists are mutable (and they have different synatx).  Tuples have a memory and performance boost over lists
because of their immutability.  However, there is a philosophical difference between the two.  Tuples are best used as heterogenous collections expressing different concepts, while lists are
generally thought of and employed as homogenous collections.

Only tuples can be used as keys in dictionaries.  This is a direct result of their immutability and the way python dictionaries work.  Dictionaries in python require that the key objects provide a hash function to allow for O(1) lookup performance.  Lists don't provide a valid way of hashing by their contents, as tuples do, because the contents of a list can be changed.  If the list is changed then its hash function would change and could cause collisions with other hash values corresponding to that dictionary.  This is clearly undesirable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

Sets will remove duplicate values, sets are unordered (they utilize a hash lookup for searching), and sets can only contain hashable items (due to the hash lookup).  Sets also allow for functions like intersection, union, difference, and symmetric difference.

Sets are much faster at determining if an object is present, but slower at iterating over their contents.  This is because sets use a hash function to find items in the set, while lists are ordered thus making it easier to iterate.

This is my favorite way of using lists and sets together.  If you have a list and you want it to be a list but you want it to be a list of unique values you can do:

unique_list = list(set(original_list))

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

Lambda is an example of an "anonymous function" (function that is not bound to a name).  A Lambda function is essentially a fast, syntactically convenient way to make a standard function definition that are limited to a single expression.  They are often used in conjunction with map(), filter(), and reduce() functions.

Say we have a dataset called people, with columns Name, Age, and FavoriteColor and we want to sort by the age in ascending ordered
sorted_people = sorted(people, key=lambda person: person[1])

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

A List comprehension is an easy way to create a list.  Mostly used to create a list that is the result of applying some operations to each element in another list/sequence/iterable thing.

creating a list of squares of another list

new_list = [x**2 for x in old_list] --> new_list = map(lambda x: x**2, old_list)

filtering to only return "true" values

new_list = [x for x in old_list if x] --> new_list = filter(lambda x: x, old_list)

In most situations for python, using a list comprehension will perform better because it doesn't have any of the overhead of creating a function like the map and filter commands do.

Set Comprehension:

if old_list = [1,2,3,4,5], this will create set([1,4,9,16,25])

new_set = {x**2 for x in old_list}

Dictionary Comprehension:

this will create the dictionary {0:0, 1:1, 2:4, 3:9, 4:16}

d = {x: x**2 for x in range(5)}


---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

937 days

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

7850 days

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)
