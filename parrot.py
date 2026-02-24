prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

while True:
    message = input(prompt)
    
    if message == 'quit':
        break
    elif message == 'parrot':
        print("Oh, think you're a wise guy hun?")
        break
   
    else:
        print(message)
        
        