## I answered option 2: Implement Stack
Given we are not allowed to use any containers to implement a Stack structure, I decided that I would use nodes for my implementation. The idea is that I could keep track of the last value in by just taking the head and making that the next, behind the new one. I also kept track of the current depth of the stack. 

In push, I created a new node which had the head as its next one and incremented the depth. I then replaced the head of stack  with the new node. 

In pop, I did the reverse, setting the next node of the current head as the new head, decrementing the depth, and returning the value of the previous head. If head was empty, I returned an exception. 

In peek, I return the value of the head node and if head is empty, return an exception. 

Lastly, in size, I returned the depth counter. 
