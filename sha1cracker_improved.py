import hashlib, time, sys
from Queue import Queue
from threading import Thread

def find_salt(hashed_salt):
    if not hashed_salt:
        return
    with open('password_list.txt', 'r') as salt_list:
        for salt in salt_list.readlines():
            if hashed_salt == hashlib.sha1(salt.rstrip('\n')).hexdigest():
                return salt

def find_hash(hash, q, *salt):
    start = time.clock()
    attempts=0
    plaintext_salt=str(salt)
    with open('password_list.txt', 'r') as password_list:
        for password in password_list.readlines():
            attempts+=1
            if hash == hashlib.sha1(password.rstrip('\n')).hexdigest():
                q.put('password: ' + password.rstrip('\n'))
                q.put('attempts: ' + str(attempts))
                q.put('time: ' + str(time.clock()-start))

def find_salted_hash(hash, q, salt):
    start = time.clock()
    attempts=0
    plaintext_salt=str(salt)
    with open('password_list.txt', 'r') as password_list:
        for password in password_list.readlines():
            attempts+=1
            if hash == hashlib.sha1(plaintext_salt.rstrip('\n') + password.rstrip('\n')).hexdigest():
                q.put('password: ' + password.rstrip('\n'))
                q.put('attempts: ' + str(attempts))
                q.put('time: ' + str(time.clock()-start))

if __name__ == '__main__':
    q = Queue()
    if len(sys.argv) == 3:
        salt = find_salt(sys.argv[2])
        t2=Thread(target = find_salted_hash, args=(sys.argv[1], q, salt))
        t2.start()
        t2.join()
    t1=Thread(target = find_hash, args=(sys.argv[1], q))
    t1.start()
    t1.join()

    print list(q.queue)
