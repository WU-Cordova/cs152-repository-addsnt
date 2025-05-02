Menu -- Bag:
- has a fixed number (five in this case) but order does not matter
- is flexible in being able to add or remove items

    complexity:
    - add: O(1) because just adding, no iteration needed
    - remove: O(n) because of iteration through elements
    - count: O(n) for iteration and ocunting of items
    - iteration: O(n) to go through the items

    trade-off:
    - I could use an array for this, and there would be O(1) for accessing in the display, but 5 is small enough that it doesn't matter and I think the flexiblity of adding and dropping wins

Customer Order -- LinkedList:
- number of drinks varies so this allows for them to be added easily and it is easy to travel along

    complexity:
    - append: O(1) just adding no need to search for it
    - iteration: O(n) have to go through all...
    
    trade-off:
    - accessing is O(n) but if it was an Array or ListStack resizing would be necessary so this is better in long run


Order Confirmation -- i lowk don't use one... #oops:
- i am just iterating through the LinkedList because it has the customer orders, and then i display it for confirmation
- when i went through the pedalogical i can see why a ListStack is a good idea, but this worked for me so why chnage it #lol😛


Open Orders -- circularqueue:
- orders done in a FIFO way
    * no angry customers!!!

    complexity:
    - enqueue: O(1) if not full, O(n)? if its full and removing and adding but is O(1) on avg
    - dequeue: O(1) removing and return and you know which one!
    - empty/full: O(1) one opperation to check

    trade_off:
    - LinkedList could work, but the cirqueue fixed size is good for memory and not overworking whatever poor barista that would have to use this


Completed Orders -- deque:
- super flexible!!! able to store orders ALL orders from the day and keep them organized for what has been compleeted and what hasn't by moving stuff to the back
- best of both words with stack and queue imo

    complexity;
    - enqueue: O(1) with LinkedList append
    - dequeue: O(1) with LinkedList pop_front
    - iterating: O(n) to go over all elements

    trade-off:
    - LinkedList is similar woith adding but the deque is wayyy better for being able to keep everything and allow for rearranging


Instructions:
1. go to the (annoying) debug thing to allow it to actually run
    a. have to be in project 3 too
2. run it
3. honeslty just follow printed directions they are really self explanatory
4. option list will be printed and use that to do different things
5. exit when done!

run example:
--- Welcome to Addison's Bistro! ---
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 1

 💫🪷🌞Addison's Bistro Menu⚡️🪼🫧
1. Latte (Medium) - $5.00
2. Chai Latte (Medium) - $5.00
3. Lemonade (Medium) - $4.00
4. Matcha (Medium) - $6.00
5. Hote Tea (Medium) - $4.00
-------------------


--- Welcome to Addison's Bistro! ---
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 2
Enter customer name: Addison

 💫🪷🌞Addison's Bistro Menu⚡️🪼🫧
1. Latte (Medium) - $5.00
2. Chai Latte (Medium) - $5.00
3. Lemonade (Medium) - $4.00
4. Matcha (Medium) - $6.00
5. Hote Tea (Medium) - $4.00
-------------------

Enter the number of the drink to order (or 'done'): 3
Enter customization for Lemonade (optional): none

 💫🪷🌞Addison's Bistro Menu⚡️🪼🫧
1. Latte (Medium) - $5.00
2. Chai Latte (Medium) - $5.00
3. Lemonade (Medium) - $4.00
4. Matcha (Medium) - $6.00
5. Hote Tea (Medium) - $4.00
-------------------

Enter the number of the drink to order (or 'done'): done

--- Order Confirmation ---
Order for Addison
- Medium Drink() with none
Confirm order? (yes/no): yes
Order for Addison added to the queue.

--- Welcome to Addison's Bistro! ---
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 3

--- Open Orders ---
- Addison: Lemonade
---------------------


--- Welcome to Addison's Bistro! ---
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 4
After enqueue(CustomerOrder()): [CustomerOrder()]
Order for Addison marked as complete.

--- Welcome to Addison's Bistro! ---
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 2
Enter customer name: hi

 💫🪷🌞Addison's Bistro Menu⚡️🪼🫧
1. Latte (Medium) - $5.00
2. Chai Latte (Medium) - $5.00
3. Lemonade (Medium) - $4.00
4. Matcha (Medium) - $6.00
5. Hote Tea (Medium) - $4.00
-------------------

Enter the number of the drink to order (or 'done'): 2
Enter customization for Chai Latte (optional): oat milk

 💫🪷🌞Addison's Bistro Menu⚡️🪼🫧
1. Latte (Medium) - $5.00
2. Chai Latte (Medium) - $5.00
3. Lemonade (Medium) - $4.00
4. Matcha (Medium) - $6.00
5. Hote Tea (Medium) - $4.00
-------------------

Enter the number of the drink to order (or 'done'): done

--- Order Confirmation ---
Order for hi
- Medium Drink() with oat milk
Confirm order? (yes/no): yes
Order for hi added to the queue.

--- Welcome to Addison's Bistro! ---
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 4
After enqueue(CustomerOrder()): [CustomerOrder(), CustomerOrder()]
Order for hi marked as complete.

--- Welcome to Addison's Bistro! ---
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 5

--- Daily Report ---
--- Drinks Sold ---
- Lemonade: 1 (Total Sales: $4.00)
- Chai Latte: 1 (Total Sales: $5.00)

--- Total Revenue ---: $9.00
-------------------------


--- Welcome to Addison's Bistro! ---
1. Display Menu
2. Take New Order
3. View Open Orders
4. Mark Next Order as Complete
5. View End-of-Day Report
6. Exit
Enter your choice: 6
Thank you for using Addison's Bistro system!

bugs/limits:
- customizations are just a string, no cost factor is added
- order rejection with circularqueue but i think it is good overall
- invalid user input is pretty limited
- i stuck with just one size

future adds:
- more sizes!
- having a cost for any customizations
    * syrup option
    * milk options
    * the bistro also has a "here vs. to-go" pricing so maybe something like that too
- any of the other extra credit stuff tbh... but the end of the semester really got to me there was no going back