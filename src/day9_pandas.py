#task 1

import pandas as pd
products = pd.Series([700,150,300], index = ('monitor','mouse','keyboard'))
print(products['monitor'])
print(products[:2])

#task 2

import pandas as pd
grades = pd.Series([85, None, 92, 45, None, 78, 55])
print(grades.isnull())
print(grades)
print(grades.fillna(0))
passed = grades[grades>60]
print(passed)

#task 3

import pandas as pd
usernames = pd.Series([' Alice ', 'bOB', ' Charlie_Data ', 'daisy'])
print(usernames)
print(usernames.str.strip())
a = usernames.str.strip()
print(a.str.lower())
print(a.str.contains('a'))
