#!/bin/bash 

Shell, permissions

0. Changes userid using "usermod -u betty vagrant"
1. Prints userid using "whoami"
2. Creates an empty file using "touch hello"
3. Prints all groups the current user is a part of using "groups vagrant"
4. Change ownership of file "hello" to user "betty" using "chown betty hello"
5. Adds execute permission to the owner of the file "hello" using "chmod 100 hello"
6. Added execute permission to owner and group owner and read permission to others using "chmod 114 hello" 
