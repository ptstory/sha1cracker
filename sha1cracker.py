import hashlib, time, sys

hash = sys.argv[1]
if len(sys.argv) == 3:
    hashed_salt = sys.argv[2]
    
attempts = 0
start = time.clock()
try:
    with open('password_list.txt', 'r') as salt_list:
        for salt in salt_list.readlines():
            if hashed_salt == hashlib.sha1(salt.rstrip('\n')).hexdigest():
                plaintext_salt = salt
                # adding a break here improves performance significantly however if the password is after
                # the plaintext salt term in the list, it won't be found
    with open('password_list.txt', 'r') as password_list:
        for password in password_list.readlines():
            attempts+=1
            if hash == hashlib.sha1(plaintext_salt.rstrip('\n') + password.rstrip('\n')).hexdigest():
                end = time.clock()
                print("wow after cracking the salt term it only took us " + str(attempts) + " guesses and a total of " + str(end-start) + " seconds to crack your hashed password which was: " + password)
except:
    with open('password_list.txt', 'r') as password_list:
        for password in password_list.readlines():
            attempts+=1
            if hash == hashlib.sha1(password.rstrip('\n')).hexdigest():
                end = time.clock()
                print("wow it only took us " + str(attempts) + " guesses and " + str(end-start) + " seconds to crack your hashed password: " + password)
            print("your password was not found in the list (good job)")
            quit()