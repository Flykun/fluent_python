'''编码之间字符的名字里有"sing"的单词'''
from unicodedata import name

print({chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')})