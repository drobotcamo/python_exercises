# function that will evaluate if a string composed only of the characters 
# ( ) { } [ ]
# has a valid closing bracket, in the proper order

def isValid(s: str) -> bool:

    # first check if the string has an even length, otherwise, return False
    if len(s) % 2 != 0:
        return False

    # we are going to maintain the current state in a STACK, the top element of which 
    # represent the next bracket to be closed
    is_open = []

    # this dictionary will define the matching opening bracket for each closing bracket
    MATCHING_PAIR_CHARS = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    # iterate through each character in the string
    for char_index in range(0,len(s)):

        # if the current character is an opening character, add it to the top of the stack
        if s[char_index] in MATCHING_PAIR_CHARS.values():
            is_open.append(s[char_index])

        # else, if the character is a closing character, (and there is an open pair) we can 
        # pop from the stack and evaluate
        elif s[char_index] in MATCHING_PAIR_CHARS.keys() and len(is_open) > 0:
            curr = is_open.pop()

            #if the character that came off of the stack isn't the matching opening character, fail
            if not curr == MATCHING_PAIR_CHARS[s[char_index]]:
                return False
        # if we encounter a closing character when the stack is empty, fail
        else:
            return False
    # at the end of the loop, if there are unclosed pairs, then fail
    if len(is_open) > 0:
        return False
    
    # if we didn't fail, then good job, we did it!
    return True