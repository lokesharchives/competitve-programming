"""Levenshtein Distance
Write a function that takes in two strings and returns the minimum number of edit operations that need to be performed on the first string to obtain the second string.

There are three edit operations: insertion of a character, deletion of a character, and substitution of a character for another.

Sample Input
str1 = "abc"
str2 = "yabd"
Sample Output
2 // insert "y"; substitute "c" for "d"

"""

def levenshtein_distance(str1, str2):
    # Create a 2D array to store the edit distances
    dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]

    # Initialize the base cases (transformations from empty string)
    for i in range(len(str1) + 1):
        dp[i][0] = i  # Cost of deleting all characters of str1
    for j in range(len(str2) + 1):
        dp[0][j] = j  # Cost of inserting all characters of str2

    # Fill the array
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            # If characters are the same, no operation is needed
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # Consider all possibilities (insert, delete, substitute) and find the minimum
                dp[i][j] = 1 + min(
                    dp[i - 1][j],    # Deletion
                    dp[i][j - 1],    # Insertion
                    dp[i - 1][j - 1]  # Substitution
                )

    return dp[-1][-1]
