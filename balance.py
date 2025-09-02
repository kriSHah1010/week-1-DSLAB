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
