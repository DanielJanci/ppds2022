# Homework 7
Program in the file main.py creates and runs multiple generatos until
one of them yields for the last time.


Program contains:

Generator "task" which has two parameters. First parameter determines how many
times the generator can yield a value (a number of iterations). Second parameter 
is an identificator of the generator. Generator yields a string that consists 
of the identificator of the generator and a number of how many times a value has 
been yielded.

Function "create_tasks" greates generatos from parameter which is a list. 
For each element in the list an instance of the generator "task" is created. 
The element in list is the number of iterations in the generator and the index 
of that element is an identificator of the generator. Function return list of 
created generators.

Function "scheduler" creates a list of generators with function "create_tasks". 
Then it calls a "next" function for each generator in that list and prints the 
yielded value. If one of the generators has yielded for the last time 
(has reached the max number of iterations and raised StopIteration exception), 
the function ends. 

In the "main" function an integer list [4, 4, 4, 5, 3] is created and the "scheduler"
is called with that list as a parameter. 

Output:
```
task id: 0, times yielded: 1
task id: 1, times yielded: 1
task id: 2, times yielded: 1
task id: 3, times yielded: 1
task id: 4, times yielded: 1
task id: 0, times yielded: 2
task id: 1, times yielded: 2
task id: 2, times yielded: 2
task id: 3, times yielded: 2
task id: 4, times yielded: 2
task id: 0, times yielded: 3
task id: 1, times yielded: 3
task id: 2, times yielded: 3
task id: 3, times yielded: 3
task id: 4, times yielded: 3
task id: 0, times yielded: 4
task id: 1, times yielded: 4
task id: 2, times yielded: 4
task id: 3, times yielded: 4

Process finished with exit code 0
```

From the output we can see we have 5 instances of "task" that are running one after
another. They run in cyckles and in the last cyckle we can see that task with id: 4 
didn't yield and the program ended. It's because to that task has been assigned value 3
as a maximum of iterations. When function next was called on that task, an exception
StopIteration was raised and the program ended.