import string

def palindrome(word: str) -> bool:
    # Convert to lowercase
    cleaned = word.lower()
    # Remove spaces and punctuation
    cleaned = ''.join(ch for ch in cleaned if ch.isalnum())
    # Check if cleaned word equals its reverse
    return cleaned == cleaned[::-1]


# Test cases
print(palindrome("racecar"))             
print(palindrome("Nurses Run"))            
print(palindrome("Sit on a potato pan, Otis.")) 
print(palindrome("Hello"))                  