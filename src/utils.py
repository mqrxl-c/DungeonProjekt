import random

## line for visuals
BREAKLINE = "+" + "-"*64 + "+"


def print_line():
    '''prints the visual breakpoint'''
    print(BREAKLINE)


def get_json_data():
    #https://www.geeksforgeeks.org/python/reading-and-writing-json-to-a-file-in-python/
    print("Test")


def check_input_number(text, min_value = None, max_value = None):
    '''checks an input for a number until it recieves a valid number'''
    while True:
        try:
            num = int(input(text))
            if min_value is not None and num < min_value:
                print("Please enter a valid number.")
            elif max_value is not None and num > max_value:
                print("Please enter a valid number.")
            else:
                return num
        except ValueError:
            print("Please enter a valid number.")

name_list = ["Bat", "Bear", "Dog", "Wolf", "Ant Eater", "Spider"]


def randomize_name():
    '''returns a randomized name from name_list'''
    int = random.randint(0, len(name_list) - 1)
    return name_list[int]


ascii_image_list = [
    r""""                                
                                
          _.---._    /\\        
       ./'       "--`\//        
     ./              o \        
    /./\  )______   \__ \       
   ./  / /\ \   | \ \  \ \      
      / /  \ \  | |\ \  \7      
       "     "    "  "          
                                """,
    r"""     .--.              .--.     
    : (\ ". _......_ ." /) :    
     '.    `        `    .'     
      /'   _        _   `\      
     /     0}      {0     \     
    |       /      \       |    
    |     /'        `\     |    
     \   | .  .==.  . |   /     
      '._ \.' \__/ './ _.'      
      /  ``'._-''-_.'``  \      """,
    r"""                                
            /      \            
         \  \  ,,  /  /         
          '-.`\()/`.-'          
         .--_'(  )'_--.         
        / /` /`""`\ `\ \        
         |  |  ><  |  |         
         \  \      /  /         
             '.__.'             
                                """,
    r"""                                
     =/\                 /\=    
     / \'._   (\_/)   _.'/ \    
    / .''._'--(o.o)--'_.''. \   
   /.' _/ |`'=/ " \='`| \_ `.\  
  /` .' `\;-,'\___/',-;/` '. '\ 
 /.-'       `\(-V-)/`       `-.\
 `            "   "            `
                                
                                """,
]