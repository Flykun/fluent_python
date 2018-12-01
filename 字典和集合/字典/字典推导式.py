'''
常用的字典推导式
'''
dial_codes = [
    (86, 'China'),
    (91, 'India'),
    (1, 'US'),
    (62, 'Indonesia'),
    (55, 'Brazil')
]
country_code = {country:code for code, country in dial_codes}
# {'China': 86, 'India': 91, 'US': 1, 'Indonesia': 62, 'Brazil': 55}
print(country_code)
