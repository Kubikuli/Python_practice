mcase = {'P': 300, 'R': 34, 'p': 65, 's': 3}
# a dictionary associating each character from mcase keys (tranfered to lower
# case) with the sum of the values (in case of the appearance of both - the 
# lower and upper case in mcase, or the frequency of the appearing character) 
mcase_frequency = {key.lower(): sum(v for k,v in mcase.items() if k.lower() == key.lower()) for key in mcase.keys()}
print(mcase_frequency)
# expected output:  
{'p': 365, 'r': 34, 's': 3}
