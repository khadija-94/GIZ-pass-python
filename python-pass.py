class Solution:

  def longest_palindromic(s: str) -> str:
    # Create a string to store the result
    palindrome = ''

    for i in range(len(s)):

      for j in range(len(s), i, -1):

        # break
        if len(palindrome) >= j - i:
            break

        # Update if match is found
        elif s[i:j] == s[i:j][::-1]:
            palindrome = s[i:j]
            break

      return palindrome
  print(longest_palindromic("cbaba"))