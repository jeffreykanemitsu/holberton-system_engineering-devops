# 0x19 Postmortem

## Issue Summary
Between the times of 4:44PM and 5:45PM on Sunday, January 28th, 2018, while working on the Application Server #0 project for Holberton School, I encountered an issue with trying to replicate the correct output for the first task of the project. I kept getting a 404 error whenever I tried to run the command "curl http://127.0.0.1/airbnb-onepage/" and I couldn't figure out why. The root cause of the 404 error was that I had been updating the nginx configurations in the sites-enabled, rather than the sites-available.

## Timeline

* 4:44PM: After reading the given documentation for this project, I began to implement the necessary code into the sites-enabled and created a airbnb-onepage configuration file.

* 4:45PM: I began to test the code to replicate the given example outputs.

* 4:46PM: The first output for the example was correct but the second example was printing out a 404 error.

* 4:50PM: Immediately, I began to look through all the files that I had altered within the past 20 minutes, to see if there were any typos of filenames or typos within the files themselves that would be causing the 404 error.

* 5:00PM: After realizing that there were no typos, I began to do side-by-side comparisons between my code and the previously edited code in case I had deleted anything on accident.

* 5:06PM: I decided to restart my terminal, hoping that the problem would magically be fixed. I tend to do this now ever since I encounted an error while setting up a firewall, where restarting my terminal magically fixed everything.

* 5:08PM: As I was restarting my terminal, I remembered that I needed to restart my Nginx so it could reload with the new configured files that I had written. Proceeded to restart Nginx to refresh it.

* 5:13PM: Still receiving the status error 404. So I began to google what are some common possible causes as to why I am receiving a 404 error.

* 5:30PM: After doing some re-reading on the documentation for this project, I realized that I had inserted the newly written code, as well as code from previous projects, into the wrong directory. 

* 5:40PM: I copied the code that was originally in sites-enabled into sites-available, deleted the default file within sites-enabled, and then created a new symbolic link between sites-available and sites-enabled. 

* 5:45PM: I then restarted Nginx once more and was able to produce the proper output.

## Root cause and resolution
The root cause of this outage was because I had been editing the wrong file as well as forgetting to restart Nginx to refresh it with the edited files. When I tried to run the code to produce the desired output, it was unable to find the configurations necessary to produce the correct output. Restarting the Nginx and having the proper symbolic link between the two sites-enabled/available directories was able to resolve the issues that I was having. 

## Corrective and preventative measures
Careful consideration when altering a file in any way should be checked again thoroughly to prevent any issues from occurring in the future. This error that occurred was my own fault for not following the necessary steps in order to configure a web server. Although it was quickly resolved, it will be uncertain if the speed of the fix will be similar in the future. 

** Possible fixes  **
- Follow directions more thoroughly to prevent errors from occurring in the future.
- Document changes to files in order to easily track where a possible error could have occurred..
- Make better comments to describe what code I have implemented in order to not skip over previous code that I have touched.
