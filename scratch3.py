# Python implementation for the
# CYK Algorithm
  
# Non-terminal symbols
non_terminals = ["NP", "Nom", "Det", "AP", 
                  "Adv", "A"]
terminals = ["book", "orange", "man", 
             "tall", "heavy", 
             "very", "muscular"]
  
# Rules of the grammar
R = {
     "NP": [["Det", "Nom"]],
     "Nom": [["AP", "Nom"], ["book"], 
             ["orange"], ["man"]],
     "AP": [["Adv", "A"], ["heavy"], 
            ["orange"], ["tall"]],
     "Det": [["a"]],
     "Adv": [["very"], ["extremely"]],
     "A": [["heavy"], ["orange"], ["tall"], 
           ["muscular"]]
    }
  
# Function to perform the CYK Algorithm
def cykParse(w):
    n = len(w)
      
    # Initialize the table
    T = [[set([]) for j in range(n)] for i in range(n)]
  
    # Filling in the table
    for j in range(0, n):
  
        # Iterate over the rules
        for lhs, rule in R.items():
            for rhs in rule:
                  
                # If a terminal is found
                if len(rhs) == 1 and \
                rhs[0] == w[j]:
                    T[j][j].add(lhs)
  
        for i in range(j, -1, -1):   
               
            # Iterate over the range i to j + 1   
            for k in range(i, j + 1):     
  
                # Iterate over the rules
                for lhs, rule in R.items():
                    for rhs in rule:
                          
                        # If a terminal is found
                        if len(rhs) == 2 and \
                        rhs[0] in T[i][k] and \
                        rhs[1] in T[k + 1][j]:
                            T[i][j].add(lhs)
  
    # If word can be formed by rules 
    # of given grammar
    if len(T[0][n-1]) != 0:
        print("True")
    else:
        print("False")
      
# Driver Code
  
# Given string
w = "a very heavy orange book".split()
  
# Function Call
cykParse(w)