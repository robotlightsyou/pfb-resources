Why start with the shell?

It's far more common for programmer's to interact with their machines through the command line than with a mouse and GUI. The shell is your ticket to such interactions. Starting with a few lectures from MIT's Missing semester, we'll dive into why so many choose this interface.

----------
### MIT Missing Semester Lecture One
----------
#### What are terminal, shell, command line, and command prompt?

Terminal is the program to access the shell on mac, which is a command line interface(cli) for your file system. Clear as mud? For our purposes these terms are mostly interchangeable, terminal is the app we will be using to access the command line, and the rest of it is underlying architecture we don't need to concern ourselves with.

They mention 'whitespace delimited'. Whitespace is programmer talk for characters. In the shell things are split by spaces instead of commas, periods, or other punctuation. For that reason it's important to be careful any multiword arguments are wrapped in quotations.

$PATH - Not our biggest concern here, but it will be an important concept when we get to python, good to take a moment now. PATH is where your computer looks for executable files. When you download new python libraries they will be added to your path so you can access them without having to type their full name each time.

----------
#### Operators

* \>
* \>>
* |
* ;
* ''
* ""
----------
#### unix/linux commands to cover

sidenote: I mostly use mac so we're going to be a little skewed in the beginning while I relearn windows.

<pre>
sudo -> grants super user permission
pwd -> prints the current(working)
cd:
    cd .. -> move to parent folder, can be chained "cd ../../"
    cd - -> move to last directory, handy for toggling between locations
    cd ~ -> move to the home directory
ls:
    ls -l -> prints directory contents in list form with extra details
    ls -a -> show all files in a directory including hidden
touch -> create a new file
mkdir -> create a new directory
mv -> move a file or directory
cp -> make a duplicate of a file or directory
rm -> remove a file
    rm -rf -> recursively force remove, good for deleting non-empty folders.
                 CAUTION - will delete everything in a non-restorable manner,
                    be certain
    rm-R -> remove all files in a folder recursively
rmdir -> remove an empty folder, but not one with contents
man -> short for manual, use to get help in terminal, invoke with "man query"
which -> reveal the location of a file or program, eg "which python3"
history | grep -> an awesome search tool when you can't quite remember the
                    command you used last time.
</pre>

----------
#### Lecture 1 Exercises from MIT:

* Exercise 1: 
By default macs ship with zsh now, which is just a wrapper on bash. Depending on when your mac was manufactured or what os you're currently on you may have bash by default. Either or fine, they both use bash functionality and the commands/scripting is almost 100% interchangeable. Check out which shell your Terminal app uses by default. From here on out I will be using terminal more generically to mean both the shell and the program used to access it, as they are functionally the same for us.

* Exercises 2-8: 
No special instructions, give it a try and google where needed.

* Exercise 9: 
Chmod is the first time we have to get our hands dirty with permissions. I struggled with this a little in the beginning because there are two common ways to notate this, and I wasn't doing it often enough to remember why it was different than the last time.

The two methods are numeric and by flags. I personally tend to default to the numeric way, but to the best of my knowledge it is purely personal preference. With permissions you have 3 options, for 3 types of users. This is why there are 9 `permission bits` next to each item in the `ls -la` view. The first three bits are the owner permissions. If you are the only user on your computer you are most likely the owner(there's some things that default to root, but we're not concerned with those right now). The next three bits are the owner's group permissions. Groups are a default thing with unix/linux systems. The last 3 bits are all other users. A good security precaution is to only allow these users to have read permissions, even when you are the only user on a machine(allowing all users write and execute permission without explicitly intending to is bad form, just don't let the habit form). Hey, you just mentioned three new things, what are those. Read permission allows a user to read the contents of a file, write permission allows a user to edit a file, and execute permission allows a user to run the file. You mostly only want to give all 3 to the owner, and there are many times when you don't want to give execute permission to anyone. I don't run into those often, but I read that they exist. So what are some good default settings?

For files that you own and whose security isn't too great a good default would be:

```
sudo chmod 755 myFile # here all bits are set for all users
sudo chmod u+rwx myFile
sudo chmod go+rw myFile # using flags takes a command for each variation on the
                            setting
```
For more secure files consider only granting read privileges to non-owners:

```
sudo chmod 700 myFile
sudo chmod u+rwx; sudo chmod go+r
```

Take a few minutes and look up some of the numerical codes. I almost exclusively use 755, 644, 700, and 600.

[Some more info on chmod flags](https://linuxize.com/post/chmod-command-in-linux/)

Exercises 10-11 are optional, I did 10, but never bothered with 11.