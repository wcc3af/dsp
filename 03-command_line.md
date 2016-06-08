# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

'pushd' --> puts current directory into a list and moves to a different place

'popd' --> goes to the most recent directory in that list that pushd created

'mkdir p' --> can make an entire path instead of just one directory at a time

'cp source target' --> copies file from source to target (can make recurssive with -R)

'mv source target' --> move file from source to target (also recurssive ability)

'man' --> get information on any command (and 'q' to quit)

'apropos' --> find the command that does the thing you are looking for (apropos copy) (can also use this to make your command line fill with indecipherable text so non-computer people think you are a genius)

'env' --> Get information about your computer environment (can pipe this through grep to match certain strings, like a username or folder)

'grep' --> basically the command line version of a regular expression (complete with wildcard '*' symbols)

'export' --> used to change environment variables (needs the unset command to undo this)


---

###Q2.  List Files in Unix   

What do the following commands do:  

`ls`  --> lists all (unhidden) files/directories in a directory

`ls -a`  --> lists all files/directories in a directory (hidden files/directories included)

`ls -l`  --> prints files/directories in long listing format (dates, users, etc...)

`ls -lh`  --> same as 'ls -l' but prints file/directory sizes in human readable format

`ls -lah`  --> same as 'ls -lh' but also lists hidden files and directories

`ls -t`  --> sorts by modification time (as usual, lists files and directories but only non-hidden)

`ls -Glp`  --> same as 'ls -l' but does not list group (-G) and appends directory indicator (-p)



---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

'-a' is definitely a favorite espeically after working with meteor (all of the actually meat in meteor is in a hidden .meteor file)

'--author' from working with my research partner in grad school...definitely helpful to see who added something when it happened a while ago and I couldn't remember who put it there

'-h' Like this for when I'm cleaning out my computer and looking for the biggest things I don't need anymore

'-R' Used this in web development a lot when I forgot where I put some template or stylesheet

'-S' Used in conjunction with '-h' when I'm looking for the biggest things to take off my computer


---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

The xargs command gets some input from stdin and then executes some other provided command over the entire input.  This can be particularly useful for filtering results obtained from a 'find' command:

'find . -name '*.txt' | xargs grep 'waldo''

This command will return any files that contained the word 'waldo' :wink:
 

