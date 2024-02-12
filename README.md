# 0x00. AirBnB clone - The Console

## Intro:
The console capable to do:

* Create a new object(ex: new User or new city)
* Retrieve an object from a file, dataBase etc...
* Do operation on objects (count, compute state etc...)
* Update attribute of an Object
* Destroy an Object

## Usage :
The console work like this
```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
(hbnb) 
(hbnb) quit
$
```
and also work in non-interactive mode: like shell project
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
