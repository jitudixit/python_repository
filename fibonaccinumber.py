class Solution(object):
    def fib(n):
        a = 0
        b = 1
        if n < 0:
            return "Incorect Value"
        elif n == 0:
            return 0
        elif n == 1:
            return b
        else:
            for i in range(1,n):
                c = a + b
                a = b
                b = c
            return b
    print(fib(9))