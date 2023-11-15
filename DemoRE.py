# DemoRE.py
import re

#일반적인 검색
result = re.search("[0-9]*th", "  35th")
print(result)
print(result.group())

#정확하게 검색
# result = re.match("[0-9]*th", "  35th")
# print(result)
# print(result.group())

result =re.search("\d{4}", "Year 2023")
print(result.group())

result = re.search("\d{5}", "Zip-code 51200")
print(result.group())