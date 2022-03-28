# Homework 6
File main.py implements the problem of the barbershop.

This program allows customers to go to a waiting room in a barbershop until the room is full. Meanwhile,
one of the customers in the waiting room gives signal to the barber that he can start making him a haircut. 
After barber has finished he gives a signal back to customers that one of them can come to recieve a haircut.
The customer after getting the haircut frees a place in the waiting room and another can come in and wait.

Mine implementation of this problem doesn't use FIFO queue, thus customers can cut the waiting line.

File main.py contains:
Class Shared that contains variables: roomCapacity with value from parameter n, customers with default value 0, room is an empty 
array. Variables: customer, barber, customerDone, barberDone are instances of Semaphore and mutex is an instance of
Mutex. Variable room holds indetificators of customers inside the waiting room, it's only used for printing.

Function customer collects customers in a waiting room. If a customer comes to the room the number of customers
is incremented and his identificator is put to an array. If the number of customers is equal to the capacity of
the room, no more customers can come in. Function gives signal to the barber that he is ready to recieve a haircut
and waits until he is done. Then the number of customers is decremented and customers' id is removed from the 
array. Which means that another customer can come to the waiting room. Function prints the current state of the
waiting room when a customer comes in, leaves or when the waiting room is full.

Function barber waits for customer' signal and then proceeds to make a haircut for him. After that he signals the
waiting customers that one of them can come in and recieve a haircut.

Function cut_hair simulates cutting hair while barber proceed to make a haircut. Additionally, it prints a
message that the barber is working at the moment.

Function main creates threads for the customers and the barber and an instance of class Shared which they share.

