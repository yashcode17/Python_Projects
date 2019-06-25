import re

#match

result = re.match(r'DS PYTHON','DS PYTHON TRINER DS')

print(result)

print(result.group(0))

print(result.pos)
print(result.start(),result.end())

#search
#it will return first occurence of string

result = re.search(r'yashasvi',
                   'DSyashasvi PYTHON Trainer'
                   'yashasvi')

print(result)

print(result.group(0))

print(result.pos)
print(result.start(),result.end())

#findall
#it will return in the form of list

result = re.findall(r'yashasvi','DSyashasvi PYTHON Trainer yashasvi')

print(len(result))

print(result)

#split
# re.split(pattern,string,[maxsplit=0])
# this method helps to split string by yhe occurances of given pattern

result = re.split(r'i','yashiasivi')

print(result)

result = re.split(r'i','yashiasivi',maxsplit=1)

print(result)

#substitute
# re.sub(pattern, repl, string):
# It helps to search a pattern and replaces with a new sub string.
# If the pattern is not found, string is retruned unchanged.

result = re.sub(r'Python', 'JAVA', 'Yashasvi loves Python')

print(result)

#compile
# re.compile(pa7ttern, repl, string)
# we can combine a regural expression
# pattern into pattern objects, which can be used for pattern matching
# It also helps to search a pattern again without re-writing it.

pattern = re.compile('yashasvi')

result = pattern.findall('yashasvi Python Trainer')

print(result)

result2 = pattern.findall('yashasvi python trainer'
                          'and yashasvi is god')

print(result2)