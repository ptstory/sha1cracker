# SHA-1 Brute Force Cracker

This Python 2.7 program cracks a given SHA-1 hash by checking against a password list using only standard Python libraries.

### Prerequisites

- You will need Python 2.7

### Installing

- Clone this repo to your local machine using `https://github.com/ptstory/sha1cracker`

## Using the program

To use the program, you will need to input a hash value as an argument. If attempting to crack a salted hash value, you may provide the salt term as an optional argument. The following hash values were used in development and testing:

```
b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3
801cdea58224c921c21fd2b183ff28ffa910ce31
ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
```

After cloning the repo, navigate to the directory containing `sha1cracker.py` and run:

```shell
$ python sha1cracker.py <hash value> <optional salt term>
```

Example usage with salted hash:

```shell
$ python sha1cracker.py ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
```

![Image of original program output](/original.png?raw=true)


## Running the improved program

`sha1cracker_improved.py` uses Threads, Queues, and separate functions to improve performance. It can be used in the same way as `sha1cracker.py`:

```shell
$ python sha1cracker_improved.py ece4bb07f2580ed8b39aa52b7f7f918e43033ea1 f0744d60dd500c92c0d37c16174cc58d3c4bdd8e
```

The improved program provides the same information as the original (plaintext password, attempts, duration), but in a more concise way without printing complete sentences. By executing fewer nested loops, the imroved program is able to crack the salted hash in around half the time as the original:

![Image of improved program output](/improved.png?raw=true)

## Solutions to exercises

- a) (20 points) testing program hash: b7a875fc1ea228b9061041b7cec4bd3c52ab3ce3:\
    `['password: letmein', 'attempts: 16', 'time: 0.1066']`
- b) (25 points) medium hacker hash: 801cdea58224c921c21fd2b183ff28ffa910ce31:\
    `['password: vjhtrhsvdctcegth', 'attempts: 999968', 'time: 3.849783']`
- c) (30 points) leet hacker hash: ece4bb07f2580ed8b39aa52b7f7f918e43033ea1:\
    `['password: harib', 'attempts: 546155', 'time: 2.322378']`


## Authors

* **Perry Story** - (https://github.com/ptstory)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Dr. Juan Banda for the assignment
* Password list used: https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt
* Learning materials used: https://www.youtube.com/watch?v=pcErNYk7vCs and countless StackOverflow questions
