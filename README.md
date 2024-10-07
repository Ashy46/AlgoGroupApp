I answered the implementing Stack Method. 
Without using any containers to implement a Stack structure, I decided that using 
nodes would be best. The idea is that I could keep track of the last value in by just taking the head and making that the next, behind the new one. I also kept track of the current depth of the stack. 

In push, I created a new node which had the head as its next one and increment the depth. I then replaced the head of stack  with the new node. 

In pop, I did the reverse, setting the next node to head as the new head, decremented the depth, and returned the value of the previous head. If head was empty, I  returned a exception. 

In peek, I return the value of the head node and if  head is empty, return an exception. 

Lastly, in size, I returned the depth counter. 