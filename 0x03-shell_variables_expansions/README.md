#0x03 Shell, init files, variables and expansions

0. create an alias using "alias ls='rm * '
1. print "hello user" where user is the current Linux user using "echo hello $USER"
2. add /action to the end of PATH using "PATH=$PATH:/action"
3. counts the number of directories in PATH using "echo $PATH | tr -s ':' '\n' | wc -l
4. lists environment variables using "printenv"
5. lists all local variables, environment variables, and functions using "set"
6. creates a new local variable using "BETTY="Holberton"
7. creates a new global variable using "export HOLBERTON="Betty"
8. prints the result of the addition of 128 with the value stored in the environment variable TRUEKNOWLEDGE using "echo $((TRUEKNOWLEDGE + 128))
9. prints the result of POWER divided by DIVIDE using "echo $((POWER/DIVIDE))
10. displays the result of BREATH to the power of LOVE using "echo $((BREATH * * LOVE))
11. converts a number from base 2 to base 10 using "echo "$((2#$BINARY))"
12. prints all possible combinations of two letters, except oo, using "printf "%s\n" {a..z}{a..z} | grep -v oo | sort"
13. prints a number with two decimal places using "printf "%0.2f\n" $NUM"
14. converts a number from base 10 to base 16 using "printf "%x\n" $DECIMAL"
17. encodes and decodes a text using the rot13 encryption using "tr 'A-Za-z' 'N-ZA-Mn-za-m'"

