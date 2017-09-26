<p align="center">
<a href="https://www.holbertonschool.com/"><img src="https://s3.amazonaws.com/bloc-global-assets/almanac-assets/bootcamps/logos/000/002/676/original/Holberton-School.png?1467187334"/>
</a>
</p>

![shellcheck](https://img.shields.io/badge/Shellcheck-lightgrey.svg)

# 0x05. Processes and signals  #

* [Table of Contents](#table-of-contents)
	* [Author](#author)
	* [Description](#description)
	* [Objectives](#objectives)
	* [Compilation](#compilation)
	* [Requirements](#requirements)
	* [Tasks](#tasks)
	  * [Mandatory 0](#mandatory-0)
	  * [Mandatory 1](#mandatory-1)
	  * [Mandatory 2](#mandatory-2)
	  * [Mandatory 3](#mandatory-3)
	  * [Mandatory 4](#mandatory-4)
	  * [Mandatory 5](#mandatory-5)
	  * [Mandatory 6](#mandatory-6)
	  * [Mandatory 7](#mandatory-7)
	  * [Mandatory 8](#mandatory-8)

### Author ###
* Jeffrey Kanemitsu
    * [Github](https://github.com/jeffreykanemitsu)
    * [Twitter](https://twitter.com/canofmisosoup)

### Description ###
Understanding concepts of system engineering and DevOps.

<p align="center">
<a href="https://www.reddit.com/r/devops/comments/3rpzem/devops_vs_sysadmin/"><img src="http://static1.squarespace.com/static/58b71e6f6a4963b4cc2c78b8/58d02ebbdb29d67782682bff/58d02ed3bebafbc474c7a529/1494356728752/AAEAAQAAAAAAAAKYAAAAJDQ5YmZjODZkLTU5YmEtNDBjZi1iM2E2LWEyNjdjYTk4NWZhNQ.png?format=1000w"/>
</a>
</p>

### Objectives ###

<ul>
<li>What is a PID</li>
<li>What is a process</li>
<li>How to find a process PID</li>
<li>How to kill a process</li>
<li>What is a signal</li>
<li>What are the 2 signals that cannot be ignored</li>
</ul>

### Shellcheck ###
Your programs and functions will be checked with Shellcheck.

### Requirements ###

<ul>
<li>Allowed editors: <code>vi</code>, <code>vim</code>, <code>emacs</code></li>
<li>All your files will be interpreted on Ubuntu 14.04 LTS</li>
<li>All your files should end with a new line</li>
<li>A <code>README.md</code> file, at the root of the folder of the project, is mandatory</li>
<li>All your Bash script files must be executable</li>
<li>Your Bash script must pass <code>Shellcheck</code> (version <code>0.3.3-1~ubuntu14.04.1</code> via <code>apt-get</code>) without any error</li>
<li>The first line of all your Bash scripts should be exactly <code>#!/usr/bin/env bash</code></li>
<li>The second line of all your Bash scripts should be a comment explaining what is the script doing</li>
</ul>

### Tasks ###

#### Mandatory 0 ####
<p>Write a Bash script that displays its PID.</p>

<pre><code>sylvain@ubuntu$ ./0-what-is-my-pid
4120
sylvain@ubuntu$
</code></pre>

#### Mandatory 1 ####
 <p>Write a Bash script that displays a list of currently running processes.</p>

<p>Requirements:</p>

<ul>
<li>Must show all processes, for all users, including those which might not have a TTY</li>
<li>Display a user-oriented format</li>
<li>Show process hierarchy</li>
</ul>

<pre><code>sylvain@ubuntu$ ./1-list_your_processes | head -50
USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root         2  0.0  0.0      0     0 ?        S    Feb13   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ksoftirqd/0]
root         4  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/0:0]
root         5  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kworker/0:0H]
root         7  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [rcu_sched]
root         8  0.0  0.0      0     0 ?        S    Feb13   0:03  \_ [rcuos/0]
root         9  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcu_bh]
root        10  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [rcuob/0]
root        11  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [migration/0]
root        12  0.0  0.0      0     0 ?        S    Feb13   0:02  \_ [watchdog/0]
root        13  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [khelper]
root        14  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kdevtmpfs]
root        15  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [netns]
root        16  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [writeback]
root        17  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kintegrityd]
root        18  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [bioset]
root        19  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kworker/u3:0]
root        20  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kblockd]
root        21  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [ata_sff]
root        22  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [khubd]
root        23  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [md]
root        24  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [devfreq_wq]
root        25  0.0  0.0      0     0 ?        S    Feb13   0:41  \_ [kworker/0:1]
root        27  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [khungtaskd]
root        28  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kswapd0]
root        29  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [vmstat]
root        30  0.0  0.0      0     0 ?        SN   Feb13   0:00  \_ [ksmd]
root        31  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [fsnotify_mark]
root        32  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [ecryptfs-kthrea]
root        33  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [crypto]
root        45  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kthrotld]
root        46  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/u2:1]
root        65  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [deferwq]
root        66  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [charger_manager]
root       108  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kpsmoused]
root       125  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [scsi_eh_0]
root       126  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kworker/u2:2]
root       172  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [jbd2/sda1-8]
root       173  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [ext4-rsv-conver]
root       409  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [iprt]
root       549  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [kworker/u3:1]
root       808  0.0  0.0      0     0 ?        S    Feb13   0:00  \_ [kauditd]
root       834  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [rpciod]
root       846  0.0  0.0      0     0 ?        S&lt;   Feb13   0:00  \_ [nfsiod]
root         1  0.0  0.4  33608  2168 ?        Ss   Feb13   0:00 /sbin/init
root       373  0.0  0.0  19472   408 ?        S    Feb13   0:00 upstart-udev-bridge --daemon
root       378  0.0  0.2  49904  1088 ?        Ss   Feb13   0:00 /lib/systemd/systemd-udevd --daemon
root       518  0.0  0.1  23416   644 ?        Ss   Feb13   0:00 rpcbind
statd      547  0.0  0.1  21536   852 ?        Ss   Feb13   0:00 rpc.statd -L
sylvain@ubuntu$
</code></pre>

#### Mandatory 2 ####
<p>Requirements:</p>

<ul>
<li>You cannot use <code>pgrep</code></li>
<li>The third line of your script must be <code># shellcheck disable=SC2009</code> (for more info about ignoring <code>shellcheck</code> error <a href="https://github.com/koalaman/shellcheck/wiki/Ignore">here</a>)</li>
</ul>

<pre><code>sylvain@ubuntu$ sylvain@ubuntu$ ./2-show_your_bash_pid
sylvain   4404  0.0  0.7  21432  4000 pts/0    Ss   03:32   0:00          \_ -bash
sylvain   4477  0.0  0.2  11120  1352 pts/0    S+   03:40   0:00              \_ bash ./2-show_your_bash_PID
sylvain   4479  0.0  0.1  10460   912 pts/0    S+   03:40   0:00                  \_ grep bash
sylvain@ubuntu$ 
</code></pre>

<p>Here we can see that my Bash PID is <code>4404</code>.</p>

#### Mandatory 3 ####
ode>bash</code>.</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>ps</code></li>
</ul>

<pre><code>sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4555 bash
sylvain@ubuntu$ ./3-show_your_bash_pid_made_easy
4404 bash
4557 bash
sylvain@ubuntu$ 
</code></pre>

<p>Here we can see that: </p>

<ul>
<li>For the first iteration: <code>bash</code> PID is <code>4404</code> and that the <code>3-show_your_bash_pid_made_easy</code> script PID is <code>4555</code></li>
<li>For the second iteration: <code>bash</code> PID is <code>4404</code> and that the <code>3-show_your_bash_pid_made_easy</code> script PID is <code>4557</code></li>
</ul>

#### Mandatory 4 ####
  <p>Write a Bash script that displays <code>To infinity and beyond</code> indefinitely. </p>

<p>Requirements:</p>

<ul>
<li>In between each iteration of the loop, add a <code>sleep 2</code></li>
</ul>

<pre><code>sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
^C
sylvain@ubuntu$ 
</code></pre>

<p>Note that I <code>ctrl+c</code> (killed) the Bash script in the example.</p>

#### Mandatory 5 ####
<p>We killed our <code>4-to_infinity_and_beyond</code> process using <code>ctrl+c</code> in the previous task, there is actually another way to do this.</p>

<p>Write a Bash script that kills <code>4-to_infinity_and_beyond</code> process.</p>

<p>Requirements:</p>

<ul>
<li>You must use <code>kill</code></li>
</ul>

<p>Terminal #0</p>

<pre><code>sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
sylvain@ubuntu$ 
</code></pre>

<p>Terminal #1</p>

<pre><code>sylvain@ubuntu$ ./5-kill_me_now 
sylvain@ubuntu$ 
</code></pre>

#### Mandatory 6 ####
 <p>Write a Bash script that kills <code>4-to_infinity_and_beyond</code> process.</p>

<p>Requirements:</p>

<ul>
<li>You cannot use <code>kill</code> or <code>killall</code></li>
</ul>

<p>Terminal #0</p>

<pre><code>sylvain@ubuntu$ ./4-to_infinity_and_beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Terminated
sylvain@ubuntu$ 
</code></pre>

<p>Terminal #1</p>

<pre><code>sylvain@ubuntu$ ./6-kill_me_now_made_easy
sylvain@ubuntu$ 
</code></pre>

#### Mandatory 7 ####
 <p>Write a Bash script that displays: </p>

<ul>
<li><code>To infinity and beyond</code> indefinitely</li>
<li>With a <code>sleep 2</code> in between each iteration</li>
<li><code>I am invincible!!!</code> when receiving a <code>SIGTERM</code> signal</li>
</ul>

<p>Make a copy of your <code>6-kill_me_now_made_easy</code> script, name it <code>67-kill_me_now_made_easy</code>,  that kills the <code>7-highlander</code> process instead of the <code>4-to_infinity_and_beyond</code> one.</p>

<p>Terminal #0</p>

<pre><code>sylvain@ubuntu$ ./7-highlander
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
I am invincible!!!
To infinity and beyond
To infinity and beyond
To infinity and beyond
I am invincible!!!
To infinity and beyond
^C
sylvain@ubuntu$ 
</code></pre>

<p>Terminal #1</p>

<pre><code>sylvain@ubuntu$ ./67-kill_me_now_made_easy 
sylvain@ubuntu$ ./67-kill_me_now_made_easy
sylvain@ubuntu$ ./67-kill_me_now_made_easy
sylvain@ubuntu$ 
</code></pre>

#### Mandatory 8 ####
<p>Write a Bash script that kills the process <code>7-highlander</code>.</p>

<p>Terminal #0</p>

<pre><code>sylvain@ubuntu$ ./7-highlander 
To infinity and beyond
To infinity and beyond
To infinity and beyond
To infinity and beyond
Killed
sylvain@ubuntu$ 
</code></pre>

<p>Terminal #1</p>

<pre><code>sylvain@ubuntu$ ./8-beheaded_process
sylvain@ubuntu$ 
</code></pre>
