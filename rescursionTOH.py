"""
Tower of Hanoi Problem:
------------------------
The Tower of Hanoi is a classic puzzle where you have three rods and a number of disks of different sizes that can slide onto any rod. 
The puzzle starts with the disks stacked in descending order of size on one rod, with the smallest disk on top. The objective is to move 
the entire stack to another rod, obeying the following simple rules:
1. Only one disk can be moved at a time.
2. A disk can only be moved if it is the uppermost disk on a stack.
3. No disk may be placed on top of a smaller disk.

Pseudocode:
-----------
function move(n, source, auxiliary, target):
    if n <= 0:
        return
    move n - 1 disks from source to auxiliary, so they are out of the way
    move the nth disk from source to target
    display the current state of source, auxiliary, and target rods
    move n - 1 disks from auxiliary to target using source as auxiliary

Python Implementation:
-----------------------
"""

NUMBER_OF_DISKS = 5
A = list(range(NUMBER_OF_DISKS, 0, -1))  # Initialize rod A with disks in descending order
B = []  # Initialize rod B as empty
C = []  # Initialize rod C as empty

def move(n, source, auxiliary, target):
    """
    Recursively move disks from the source rod to the target rod using the auxiliary rod as needed.
    
    Parameters:
    - n: Number of disks to move from source to target.
    - source: List representing the source rod.
    - auxiliary: List representing the auxiliary rod.
    - target: List representing the target rod.
    """
    if n <= 0:
        return
    
    # Move n - 1 disks from source to auxiliary, so they are out of the way
    move(n - 1, source, target, auxiliary)
    
    # Move the nth disk from source to target
    target.append(source.pop())
    
    # Display the current state of rods A, B, and C
    print(A, B, C, '\n')
    
    # Move the n - 1 disks from auxiliary to target using source as auxiliary
    move(n - 1, auxiliary, source, target)

# Initiate the call from source A to target C with auxiliary B
move(NUMBER_OF_DISKS, A, B, C)
