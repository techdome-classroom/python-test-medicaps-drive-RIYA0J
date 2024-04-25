class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Create a dictionary to store the mappings of open and close brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        # Initialize an empty stack to keep track of open brackets
        stack = []
        
        # Iterate through each character in the input string
        for char in s:
            # If the character is an open bracket, push it onto the stack
            if char in bracket_map.values():
                stack.append(char)
            # If the character is a close bracket
            elif char in bracket_map:
                # If the stack is empty or the top of the stack does not match the corresponding open bracket, return False
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                # Pop the top of the stack as it's been successfully matched with its corresponding open bracket
                stack.pop()
            # If the character is neither an open nor a close bracket, skip it
            else:
                continue
        
        # After iterating through all characters, if the stack is empty, return True (all brackets are valid)
        return not stack

