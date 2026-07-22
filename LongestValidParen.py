


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Store indices of brackets
        stack = [-1]
        longest = 0

        for index in range(len(s)):
            if s[index] == "(":
                # Save index of opening bracket
                stack.append(index)
            else:
                # Match the latest opening bracket
                stack.pop()

                if not stack:
                    # No matching opening bracket
                    stack.append(index)
                else:
                    # Calculate current valid substring length
                    current_length = index - stack[-1]
                    longest = max(longest, current_length)

        return longest


# Input and Output
text = input().strip()

solution = Solution()
print(solution.longestValidParentheses(text))
