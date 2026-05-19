class Solution(object):

    def diagonalPrime(self, nums):

        n = len(nums)

        # Check if number is prime
        def isPrime(num):

            if num <= 1:
                return False

            for i in range(2, int(num ** 0.5) + 1):

                if num % i == 0:
                    return False

            return True

        largest = 0

        # Traverse diagonals
        for i in range(n):

            main = nums[i][i]

            secondary = nums[i][n - i - 1]

            if isPrime(main):
                largest = max(largest, main)

            if isPrime(secondary):
                largest = max(largest, secondary)

        return largest