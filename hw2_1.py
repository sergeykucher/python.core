zen_of_python = '''Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!'''

# Mode 1 & Old style
print ("Mode 1 & Old style:")
count_better = len(zen_of_python.split('better'))-1
count_never = len(zen_of_python.split('never'))-1
count_is = len(zen_of_python.split('is'))-1
print("Number of 'better' is %d" %count_better)
print("Number of 'never' is %d" %count_never)
print("Number of 'is' is %d" %count_is)
# Mode 2 & New style
print ("Mode 2 & New style:")
print ("Number of 'better' is {}".format(zen_of_python.count('better')))
print ("Number of 'never' is {}".format(zen_of_python.count('never')))
print ("Number of 'is' is {}".format(zen_of_python.count('never')))

print(zen_of_python.upper())
zen_of_python = zen_of_python.replace('i','&')
print(zen_of_python)
