import hashlib, time, sys
from itertools import permutations 

# hash = '34302959e138917ce9339c0b30ec50e650ce6b40'
start = time.clock()
hash = hashlib.sha1('password' + ' ' + '1234').hexdigest()
attempts=0
with open('password_list.txt') as f:
    words = [line.rstrip() for line in f]
    for pair in permutations(words, 2):
        attempts+=1
        password = ' '.join(pair)
        if hash == hashlib.sha1(password).hexdigest():
            print(password)
            print(attempts)
            print(time.clock() - start)