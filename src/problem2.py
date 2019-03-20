"""
Exam 1, problem 2.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and Haozhe Wu.
"""  # done. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    test_factor_sum()


def test_factor_sum():
    """ Tests the   factor_sum   function. """
    ###########################################################################
    #  TODO: 2. Implement this TEST function, as follows:
    #
    #    1. Read the  doc-string of the   factor_sum   function defined below.
    #
    #    2. Add to THIS function at least ** 5 ** tests that, taken together,
    #       would form a    ** REASONABLY GOOD test set **
    #       for testing the   factor_sum   function defined below.
    #
    #     Use the usual format:
    #       Test XXX:
    #       expected = XXX
    #       actual = XXX
    #       print()
    #       print('Expected:', expected)
    #       print('Actual:  ', actual)
    #
    #  IMPORTANT:
    #  The function that you are TESTING is PURPOSELY implemented INCORRECTLY
    #  (it just returns 0).  Do NOT implement the   factor_sum   function.
    #  Just write these TESTS of that function after reading its doc-string.
    ###########################################################################
    print()
    print('---------------------------------------------------------')
    print('Testing the   factor_sum   function:')
    print('---------------------------------------------------------')
    print('Test 1:')
    expected1=4
    actual1=factor_sum(25)
    print('expected:',expected1)
    print('actual:',actual1)


    print('Test 2:')
    expected2 = 11
    actual2 = factor_sum(28)
    print('expected:', expected2)
    print('actual:', actual2)

    print('Test 3:')
    expected3 = 4
    actual3 = factor_sum(27)
    print('expected:', expected3)
    print('actual:', actual3)

    print('Test 4:')
    expected4 = 15
    actual4 = factor_sum(42)
    print('expected:', expected4)
    print('actual:', actual4)

    print('Test 5:')
    expected5 = 10
    actual5 = factor_sum(12)
    print('expected:', expected5)
    print('actual:', actual5)
    ###########################################################################
    # WRITE YOUR TESTS BELOW HERE:
    ###########################################################################


def factor_sum(n):
    """
    Given a positive integer n,
    returns the sum of the digits of the sum of the distinct factors of n,
    where a FACTOR of n is an integer that divides evenly into n.

    For example, if n is 28, this function returns 11, because:
      -- the distinct factors of n are:
             1  2  4  7  14  28
      -- and the sum of those numbers is   1 + 2 + 4 + 7 + 14 + 28,
             which is 56
      -- and the sum of the digits of 56 is 11,
    so this function returns 11 when n is 28.

    As another example, if n is 25, this function returns 4, because:
    -- the distinct factors of n are:
             1  5  25
      -- and the sum of those numbers is   1 + 5 + 25,
             which is 31
      -- and the sum of the digits of 31 is 4,
    so this function returns 4 when n is 28.

       *** ASK FOR AN EXPLANATION IF YOU DO NOT UNDERSTAND THE ABOVE. ***
    """
    sum=0
    for k in range(1,n+1):

        if n%k==0:
            sum=sum+k

    digitsum=sum//10+(sum-sum//10*10)

    ###########################################################################
    #  This function is PURPOSELY implemented INCORRECTLY (it just returns 0).
    #  DO NOT IMPLEMENT  factor_sum.  Just leave it as it is (returning 0).
    ###########################################################################
    return digitsum
    ###########################################################################
    # DO NOT modify the above line of code!
    ###########################################################################


main()
