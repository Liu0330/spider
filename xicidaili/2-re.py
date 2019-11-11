import re

# s = 'hello world python high salary 123 456 Hello 789.' \
#     ' precious things are very few in the world,' \
#     'that is the reason there is only one you!'
# # pattern = re.compile(r'[A-Za-z]+')
# pattern = re.compile(r'[\s.,\n!]')
# # result = re.findall(pattern,s)
# result = re.split(pattern,s)
# print(result)

s = 'Hello World,Hello Python'

pattern = r'(\w+) (\w+)'
# result = re.sub(pattern,r'\2 \1',s)
# print(result)
def convert(m):
    return m.group(2) + ' ' + m.group(1).upper()
result = re.sub(pattern,convert,s)
print(result)