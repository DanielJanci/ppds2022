# Homework 5
File main.py implements a modification of a problem of savages from: 
https://uim.fei.stuba.sk/i-ppds/5-cvicenie-problem-fajciarov-problem-divochov-%f0%9f%9a%ac/



File contains two classes. First class is called Shared, and it contains variables: servings with value from parameter m, 
mutex is an instance of Mutex, full_pot and empty_pot is an instance of Semaphore, barrier is an instance of SimpleBarrier
Second class is called SimpleBarrier, and it contains variables: n with value from parameter n, count with default 
value 0, mutex is an instance of Mutex, barrier is an instance of Semaphore. It is an implementation of a barrier with
an addition to function wait that when the count is equal to n, it sets value servings in shared to M and signalizes 
the savages that pot is full.

This file also contains some functions. Function eating simulates the time spent when a savage is eating with a sleep
function. Function cooking simulates the time spent when a cook is cooking also with a sleep function. 

Function savage has parameters: i which is an identificator of a savage and shared which is an instance of class Shared.
This function decrements variable servings in shared by one when savage eats a meal. If there is no more meals (servings)
one savage signalizes all cooks, so they can start cooking.

Function cook has parameters: i which is an identificator of a cook and shared which is an instance of class Shared.
Function allows cook to start cooking after he was signalized. Then every cook stops at barrier where they wait each 
other and signalize savages when the serving are ready.

Finally, main function, creates an instance of class Shared with value 0, S number of threads for savages and C number 
of threads fo cooks.

Pseudocode:
```
C is the number of cooks
M is the number of servings
count = 0

while True
begin
    lock thread for i from savages
    if servings != 0
        begin
            display "savage i wakes up cooks"
            signal cooks
            wait for cooks to finish the dinner
        end    
    else
        begin
            simulate eating
            display "savage i eats"
            decrement the number of servings by 1
        end
    unlock thread i from savages
end

while True
begin 
    wait for signal from savages
    simulate cooking
    begin
        lock thread for i from cooks
        increment count by 1
        display "cook i is cooking"
        if count == C
            begin 
                display "cook i tells that dinner is ready"
                set count to 0
                set servings to M
                signal savages that they can start eating
                signal cooks that wait at barrier
            end
        unlock thread for i from cooks
        cooks wait at barrier
    end
end    
```