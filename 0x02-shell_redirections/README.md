#0x02 Shell, I/O Redirections and filters

0. prints "Hello, World" using "echo 'Hello, World'"
1. displays a confused smiley using "echo "\"(Ôo)'""
2. displays the content of the /etc/passwd" file using "cat /etc/passwd"
3. displays the content of two files using "cat /etc/passwd /etc/hosts"
4. displays the last 10 lines of /etc/passwd using "tail /etc/passwd"
5. displays the first 10 lines of /etc/passwd using "head /etc/passwd"
6. displays the third line of the file iacta using "cat iacta | head -3 | tail -1"
7. writes the result of ls -la into file ls_cwd_content using "ls -la >> ls_cwd_content"
8. creates a file containing text using "echo "Holberton School" > \\\*\\\\\'\"Holberton\ School\"\\\'\\\\\*\$\\\?\\\*\\\*\\\*\\\*\\\*\:\)"
9. duplicated the last line of file "iacta" using "tail -n 1 iacta >> iacta"
10. deletes all regular files with a .js extension that is in the current directory and all of its subfolders using "find . -type f -name '.js' -delete"
11. counts the number of directories and sub-directories in the current directory using "find . -mindepth 1 -type d | wc -l"
12. display the 10 newest files in the current directory using "ls -1t | head -10"
13. takes a list of words as input and prints only words that appear once using "sort | uniq -u"
14. display lines containing the pattern "root" from file /etc/passwd using "grep root /etc/passwd"
15. display the number of lines that contain the pattern "bin" in the file /etc/passwd using "grep -c bin /etc/passwd"
16. display lines containing the pattern "root" and 3 lines after them in the file /etc/passwd using grep -A 3 'root' /etc/passwd"
17. display all the lines in the file /etc/passwd that do not contain the pattern "bin" using "grep -v bin /etc/passwd"
18. display all lines of the file /etc/ssh/sshd_config starting with a letter using "grep -i ^[a-z] /etc/ssh/sshd_config
19. replaces all characters A and c from input to Z and e using "tr [A,c] [Z,e]
20. removes all letters c and C from input using [tr -d Cc]
21. reverse its input using "rev"
22. displays all users and their home directories, sorted by users using "cut -d ':' -f 1,6 /etc/passwd | sort
