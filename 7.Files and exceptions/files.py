"""
The keyword with closes the file once access to it is no longer needed.
Notice how we call open() in this program but not close(). You could open
Files and Exceptions and close the file by calling open() and close(), but if a bug in your program
prevents the close() statement from being executed, the file may never
close. This may seem trivial, but improperly closed files can cause data
to be lost or corrupted. And if you call close() too early in your program,
you’ll find yourself trying to work with a closed file (a file you can’t access),
which leads to more errors. It’s not always easy to know exactly when you
should close a file, but with the structure shown here, Python will figure that
out for you. All you have to do is open the file and work with it as desired,
trusting that Python will close it automatically when the time is right.
Once we have a file object representing pi_digits.txt, we use the read()
method in the second line of our program to read the entire contents of
the file and store it as one long string in contents. When we print the value
of contents, we get the entire text file back.
"""
filename = './pi_digits.txt'
#Reading all content of the file
with open(filename) as file_object:
    contents = file_object.read()
    print(contents)
#Reading line by line of the file
with open(filename) as file_object:
    for line in file_object:
        print(line)
#Making a list of lines from file
with open(filename) as file_object:
    lines = file_object.readlines()
#Writing text file
filename = 'programming.txt'
with open(filename, 'w') as file_object: #open has options: 'r' (read mode) 'w' (write mode) 'a' (append mode)
    file_object.write("I love programming.")