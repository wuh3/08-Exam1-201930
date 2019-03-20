"""
Exam 1, problem 3.

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Mark Hays, Amanda Stouder, Aaron Wilkin, their colleagues,
         and PUT_YOUR_NAME_HERE.
"""  # TODO: 1. PUT YOUR NAME IN THE ABOVE LINE.

import testing_helper
import time


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem3a()
    run_test_problem3b()


###############################################################################
# TODO: 2.  READ the doc-string for the  sum_of_digits  and   is_prime
# functions defined below.  They are the same as what you have seen before.
# After you UNDERSTAND the doc-string (JUST the doc-string, NOT the code),
# ASKING QUESTIONS AS NEEDED, change the above _TODO_ to DONE.
###############################################################################

def sum_of_digits(number):
    """
    What comes in:  An integer.
    What goes out:  Returns the sum of the digits in the given integer.
    Side effects:   None.
    Example:
      If the integer is 83135,
      this function returns (8 + 3 + 1 + 3 + 5), which is 20.
    """
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  sum_of_digits function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------
    if number < 0:
        number = -number

    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def is_prime(n):
    """
    What comes in:  An integer n >= 2.
    What goes out:
      -- Returns True if the given integer is prime,
         else returns False.
    Side effects:   None.
    Examples:
      -- is_prime(11) returns  True
      -- is_prime(12) returns  False
      -- is_prime(2)  returns  True
    Note: The algorithm used here is simple and clear but slow.
    """
    for k in range(2, (n // 2) + 1):
        if n % k == 0:
            return False

    return True
    # -------------------------------------------------------------------------
    # Students:
    #   Do NOT touch the above  is_prime  function - it has no _TODO_.
    #   Do NOT copy code from this function.
    #
    # Instead, ** CALL ** this function as needed in the problems below.
    # -------------------------------------------------------------------------


def run_test_problem3a():
    """ Tests the   problem3a   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3a  function:')
    print('--------------------------------------------------')

    format_string = '    problem3a( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = 2 + 3 + 5 + 7 + 11  # which is 28
    print_expected_result_of_test([2, 4], expected, test_results,
                                  format_string)
    actual = problem3a(2, 4)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = 0  # Since there are no numbers to consider between 5 and 5**1.
    print_expected_result_of_test([5, 1], expected, test_results,
                                  format_string)
    actual = problem3a(5, 1)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = 11 + 23 + 29 + 41 + 43 + 47 + 61   # which is 255
    print_expected_result_of_test([8, 2], expected, test_results,
                                  format_string)
    actual = problem3a(8, 2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = 205585
    print_expected_result_of_test([7, 4], expected, test_results,
                                  format_string)
    actual = problem3a(7, 4)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = 2625496
    print_expected_result_of_test([100, 2], expected, test_results,
                                  format_string)
    actual = problem3a(100, 2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = 112925
    print_expected_result_of_test([12, 3], expected, test_results,
                                  format_string)
    actual = problem3a(12, 3)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 7:
    expected = 0
    print_expected_result_of_test([89, 1], expected, test_results,
                                  format_string)
    actual = problem3a(89, 1)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 8:
    expected = 1703968
    print_expected_result_of_test([6, 5], expected, test_results,
                                  format_string)
    actual = problem3a(6, 5)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 9:
    expected = 2625496
    print_expected_result_of_test([100, 2], expected, test_results,
                                  format_string)
    actual = problem3a(100, 2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 10:
    expected = 34090347
    print_expected_result_of_test([101, 2], expected, test_results,
                                  format_string)
    actual = problem3a(200, 2)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 11:
    expected = 5 + 7 + 11  # which is 23
    print_expected_result_of_test([4, 2], expected, test_results,
                                  format_string)
    actual = problem3a(4, 2)
    print_actual_result_of_test(expected, actual, test_results)
    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem3a(a, b):
    """
    What comes in:  Positive integers a and b, with a >= 2.
    What goes out:
      An integer X is "doubly prime" if X is prime AND the sum of the digits
        of X is also prime.  For example, 23 is doubly prime (because 23 is
        prime and also 2 + 3 = 5 is prime), but 17 is NOT doubly prime
        (since 1 + 7 = 8 is NOT prime).  Ask your instructor for help if
         you do not understand this definition of "doubly prime".

      This function returns the sum of all the doubly prime integers from a
      to a**b, but NOT counting a**b.

    Side effects:   None.
    Examples:
      -- problem3a(2, 4) returns 2 + 5 + 7 + 11  (which is 28)
      -- problem3a(5, 1) returns 0 (because there are NO numbers between
                                    5 and 5**1, not counting 5**1)
      -- problem3a(8, 2) = 11 + 23 + 29 + 41 + 43 + 47 + 61  (which is 255)
    """
    # -------------------------------------------------------------------------
    # TODO: 3. Implement and test this function.
    #          Tests have been written for you (above).
    #
    ###########################################################################
    # IMPORTANT:
    #    **  For full credit you must appropriately
    #    **  use (call) the appropriate function(s) that are DEFINED ABOVE.
    ###########################################################################


def run_test_problem3b():
    """ Tests the   problem3b   function. """
    print()
    print('--------------------------------------------------')
    print('Testing the   problem3b  function:')
    print('--------------------------------------------------')

    format_string = '    problem3b( {}, {} )'
    test_results = [0, 0]  # Number of tests passed, failed.

    # Test 1:
    expected = True
    print_expected_result_of_test([2, 22], expected, test_results,
                                  format_string)
    actual = problem3b(2, 22)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 2:
    expected = True
    print_expected_result_of_test([2, 23], expected, test_results,
                                  format_string)
    actual = problem3b(2, 23)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 3:
    expected = False
    print_expected_result_of_test([2, 24], expected, test_results,
                                  format_string)
    actual = problem3b(2, 24)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 4:
    expected = True
    print_expected_result_of_test([7, 205383], expected, test_results,
                                  format_string)
    actual = problem3b(7, 205383)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 5:
    expected = True
    print_expected_result_of_test([7, 205384], expected, test_results,
                                  format_string)
    actual = problem3b(7, 205384)
    print_actual_result_of_test(expected, actual, test_results)

    # Test 6:
    expected = False
    print_expected_result_of_test([7, 205385], expected, test_results,
                                  format_string)
    actual = problem3b(7, 205385)
    print_actual_result_of_test(expected, actual, test_results)

    # SUMMARY of test results:
    print_summary_of_test_results(test_results)


def problem3b(m, x):
    """
    What comes in:  A positive integer m >= 2, and an integer x.
    What goes out:
      -- Returns True if the number of doubly prime integers from m**2 to m**4,
         not counting m**4, is greater than or equal to x.
          eturns False otherwise.
    Side effects:   None.
    Examples:
      -- problem3b(6, 4) returns
           1/4  +  2/(5**2)  +  3/(6**3)  +  4/(7**4)  +  5/(8**5)  + 6/(9**6),
           which is approximately 0.3457187393495064.
      -- problem3b(3, 1) returns
           1/1  +  2/(2 ** 2)  +  3/(3 ** 3), which is approximately 0.6111111.
      -- problem3b(2, 35) returns
           1/35  +  2/(36**2), which is approximately 0.03011463844797178.
      -- problem3b(4, 0.1) returns
           1/(0.1)  +  2/((1.1)**2)  +  3/((2.1)**3)  +  4/(3.1)**4)),
           which is approximately 12.020144157845959.
     """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    #          Tests have been written for you (above).
    ###########################################################################
    ###########################################################################
    # IMPORTANT:
    #    **  For full credit you must appropriately
    #    **  use (call) the appropriate function(s) that are DEFINED ABOVE.
    ###########################################################################


###############################################################################
# Our tests use the following to print error messages in red.
# Do NOT change it.  You do NOT have to do anything with it.
###############################################################################

def print_expected_result_of_test(arguments, expected,
                                  test_results, format_string, suffix=''):
    testing_helper.print_expected_result_of_test(arguments, expected,
                                                 test_results, format_string,
                                                 suffix)


def print_actual_result_of_test(expected, actual, test_results,
                                precision=None):
    testing_helper.print_actual_result_of_test(expected, actual,
                                               test_results, precision)


def print_summary_of_test_results(test_results):
    testing_helper.print_summary_of_test_results(test_results)


# To allow color-coding the output to the console:
USE_COLORING = True  # Change to False to revert to OLD style coloring

testing_helper.USE_COLORING = USE_COLORING
if USE_COLORING:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_colored
else:
    # noinspection PyShadowingBuiltins
    print = testing_helper.print_uncolored

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# The   try .. except   prevents error messages on the console from being
# intermingled with ordinary output to the console.
# -----------------------------------------------------------------------------
try:
    main()
except Exception:
    print('ERROR - While running this test,', color='red')
    print('your code raised the following exception:', color='red')
    print()
    time.sleep(1)
    raise
