class Solution:
    def isValid(self, s: str) -> bool:
        close_braces_stack = []
        for char in s:
            if char in ['(', '[', '{']:
                close_braces_stack.append(char)
            else:
                if not close_braces_stack:
                    return False
                if char == ')' and close_braces_stack[-1] == '(' \
                        or char == '}' and close_braces_stack[-1] == '{' \
                        or char == ']' and close_braces_stack[-1] == '[':
                    close_braces_stack.pop()
                else:
                    return False
        if close_braces_stack:
            return False
        return True


print(Solution().isValid('()[]{}'))
print(Solution().isValid('()[]{'))
