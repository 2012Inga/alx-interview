#!/usr/bin/python3
"""
Calculates the minimum operations needed to achieve exactly n 'H' characters
using 'Copy All' and 'Paste' operations.
"""

def minOperations(n):
    if n <= 0:
        return 0
    
    dp = [float('inf')] * (n + 1)
    dp[1] = 0
    
    for i in range(2, n + 1):
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + (i // j))
    
    return dp[n] if dp[n] != float('inf') else 0

# Example usage:
if __name__ == "__main__":
    n = 4
    print(f"Min number of operations to reach {n} characters: {minOperations(n)}")

    n = 12
    print(f"Min number of operations to reach {n} characters: {minOperations(n)}")
