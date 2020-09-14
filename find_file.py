import fnmatch
import os

pattern  = ['*.py']
matches = []

for root, dirnames, filenames in os.walk(".") :
    for extensions in pattern :
        for filename in fnmatch.filter(filenames, extensions):
            matches.append(os.path.join(root, filename))
            print(root, filename)
print (matches)