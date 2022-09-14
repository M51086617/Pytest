import re

strr = '<input type="hidden" id="bsToken" name="bsToken" value="cebc-1b4e-a3a064b432427e2c82828842" />'
pattern = re.compile(r'value="(.{4})-(.{4})-.{24}')
result = pattern.search(strr)
print(result[1])
