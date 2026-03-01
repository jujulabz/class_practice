"""
Make a list called sandwich_orders and fill it with the names of various sandwiches.
Then make an empty list called finished_sandwhiches. Loop throug the list of sandwhich orders
and print a message for each order, such as "I made your tuna sandwich". As each sandwhich is made,
move it to the list of finished sandwhiches. After all the sandwhiches have been made, print a message
listing each sandwhich that was made.    
    """
    
sandwich_orders = ['Ruben','Cuban','BLT','P B & J', 'hotdog']

finished_orders = []

while sandwich_orders:
    current_order = sandwich_orders.pop()
    
    print(f"Working on {current_order if current_order == 'hotdog' else current_order+' sandwich'}")
    finished_orders.append(current_order)
    
    #display all confirmed users 
    
    print("\nDone making all of the following sandwhiches")
    for finished_sandwhiches in finished_orders:
        
        print(f"{finished_sandwhiches if finished_sandwhiches == 'hotdog' else finished_sandwhiches + ' sandwich'}")