"""
Unit test for the `toolbox` module.

When run as an script, this module invokes several procedures that
test the various functions in the `toolbox` module.

Developed by Al Palanuwech (ap689) and Professor Bracy for CS1110SP A1.

Author: Kene Chukwuma (ebc68) and Monalisa Almeida (mca74)
Date:   02/15/23
"""


import toolbox
import introcs

# STUDENTS DO NOT MODIFY BELOW
# ========================================================================
# example test function for file_to_string:


def test_file_to_string():
    """ Tests the function file_to_string(), will be completed given to students
    """
    print("Testing toolbox.file_to_string()")

    # 1. Test small file containing 'Hello World'
    ans = 'Hello World'
    result = toolbox.file_to_string("test_string_file.txt")
    introcs.assert_equals(ans, result)

    # 2. Test 'case1.txt' file, multi-line file
    ans = ('0:{suspects:al palanuwech;lenhard thomas;anne bracy, time:4:39,}' +
           '\n1:{name:pirlevh xlsqew, time:4:15,}\n2:{time:4:45, name:ep tepe' +
           'ryaigl,}\n')
    result = toolbox.file_to_string("case1.txt")
    introcs.assert_equals(ans, result)

    print("Done Testing toolbox.file_to_string()")
# =========================================================================

# start writing test functions
# TODO: There should be 3 new test functions added
def test_before_first():
    """Tests the function toolbox.before_first()"""
    print('Testing toolbox.before_first()')
    #insert test cases in the middle
    # test 1 digit marker
    result = toolbox.before_first('ab+c', '+')
    introcs.assert_equals('ab', result)

    # test 2 or more digit marker
    result = toolbox.before_first('to+++b', '+++')
    introcs.assert_equals('to', result)

    #test marker at the beginning
    result = toolbox.before_first('-strap' , '-')
    introcs.assert_equals('', result)

    #test marker at the end
    result = toolbox.before_first('earth-' , '-')
    introcs.assert_equals('earth', result)

    #test multiple markers in the string
    result = toolbox.before_first('food', 'o')
    introcs.assert_equals('f', result)

    print('Done Testing toolbox.before_first()')
    pass

def test_after_first():
    """Tests the function toolbox.test_after_first"""
    print('Testing toolbox.test_after_first()')
    #insert test cases in the middle
     # test 1 digit marker
    result = toolbox.after_first('ab+c', '+')
    introcs.assert_equals('c', result)

    # test 2 or more digit marker
    result = toolbox.after_first('to+++b', '+++')
    introcs.assert_equals('b', result)

    #test marker at the beginning
    result = toolbox.after_first('-strap' , '-')
    introcs.assert_equals('strap', result)

    #test marker at the end
    result = toolbox.after_first('earth-' , '-')
    introcs.assert_equals('', result)

    #test multiple markers in the string
    result = toolbox.after_first('fodo', 'o')
    introcs.assert_equals('do', result)
    print('Done Testing toolbox.test_after_first')

def test_get_value():
    """Tests the function toolbox.test_get_value()"""
    print('Testing toolbox.test_get_value()')

    #insert test cases at the middle

    #test keyword at the beginning
    result = toolbox.get_value('{name:John White, time:4:45,}','name')
    introcs.assert_equals('John White', result)

    #test keyword at the middle
    result = toolbox.get_value('{name:John White, ln:White, time:4:45,}','ln')
    introcs.assert_equals('White', result)

    #test keyword at the end
    result = toolbox.get_value('{name:John White, time:4:45,}','time')
    introcs.assert_equals('4:45', result)

    #test multiple keyword in the string
    result = toolbox.get_value('{time:John White, time:4:45,}','time')
    introcs.assert_equals('John White', result)

    print('Done Testing toolbox.test_get_value()')

print("Start testing module toolbox")
test_file_to_string()
test_before_first()
test_after_first()
test_get_value()
# add calls to test procedures here
print("Success! Everything looks good.")
