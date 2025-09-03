# -------------------------------
# Exercise 1: Palindrome Checker
# -------------------------------

def palindrome(word: str) -> bool:
    # Convert to lowercase
    cleaned = word.lower()
    # Remove spaces and punctuation
    cleaned = ''.join(ch for ch in cleaned if ch.isalnum())
    # Check if cleaned word equals its reverse
    return cleaned == cleaned[::-1]

print(palindrome("racecar"))             
print(palindrome("Nurses Run"))            
print(palindrome("Sit on a potato pan, Otis.")) 
print(palindrome("Hello"))  


# -------------------------------
# Exercise 2: Balanced Parentheses
# -------------------------------
def parentheses(sequence: str) -> bool:
    balance = 0
    for char in sequence:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:  # Too many closing parentheses
                return False
    return balance == 0  # Must end balanced


# Test Cases
print(parentheses("((blah)()()())"))    
print(parentheses("(((())blee))"))      
print(parentheses("(()hello((())()))"))  
print(parentheses("((((((())"))          
print(parentheses("()))"))       
