class Solution(object):

    def reverse(self, x):

        # Store sign
        sign = -1 if x < 0 else 1

        # Make x positive
        x = abs(x)

        a = ""

        while x > 0:

            a += str(x % 10)

            x = x // 10

        # Special case for 0
        if a == "":
            return 0

        # Convert first, then apply sign
        x = sign * int(a)
        if x < -2**31 or x>2**31 - 1:
            return 0

        return x