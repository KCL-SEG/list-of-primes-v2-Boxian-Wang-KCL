"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    
    l = [2]
    n = 3
    
    while len(l) < number_of_primes:
        isP = True
        for i in range(2, n):
            if n % i == 0:
                isP = False
        if isP:
            l.append(n) 
            
          
        n += 1       
        
    if number_of_primes <= 0:
        raise ValueError
    
    return l
