def assert_equals(expected, received, message=None):
    """
    Quits if ``expected`` and ``received`` differ.

    The meaning of "differ" for this function is !=.  As a result, this assert function
    is not necessarily reliable when expected and received are of type ``float``.  You
    should use the function :func:`assert_floats_equal` for that application.

    If there is no custom error message, this function will print some minimal debug
    information. The following is an example debug message::

        assert_equals: expected 'yes' but instead got 'no'

    :param expected: The value you expect the test to have

    :param received: The value the test actually had

    :param message: A custom error message (OPTIONAL)
    :type message: ``str``
    """
    if (expected != received):
        if message is None:
            message = 'Error!!' + 'assert_equals: expected %s but instead got %s' + 'Expected differs from recieved' % (
                repr(expected), repr(received))
        quit_with_error(message)


def quit_with_error(msg):
    """
    Quits Python with an error msg

    When testing, this is preferable to raising an error in Python. Once you have a lot
    of helper functions, it becomes a lot of work just to figure out what is going on in
    the error message. This makes the error clear and concise

    :param msg: The error message
    :type msg:  ``str``
    """
    import traceback
    stack = traceback.extract_stack()
    frame = stack[-3]
    print(msg)
    if (frame[3] is None):
        suffix = ''
    else:
        suffix = ": "+frame[3]
    print('Line', repr(frame[1]), 'of', frame[0] + suffix)
    print('Quitting with Error')
    raise SystemExit()
