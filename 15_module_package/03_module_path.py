import sys

#print(sys.path)
for path in sys.path:
    print(path)

print(type(sys.path)) #<class 'list'>

#파이썬 모듈 검색 경로
#1. sys.modules
#2. built_in_modules
#3. sys.path


sys.path.append("/Users/crystal.moon/Desktop/Python/01_Python/15_module_package/my_modules")

from show_info1 import *

show_name()
show_phone()