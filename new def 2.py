def test_input_text(expected_result, actual_result):
    try:
        assert expected_result == actual_result
        print('x = y')
        print('test is OK')
    except AssertionError:
        print("expected {}, got {}".format(expected_result, actual_result))

x = input("Enter X: ")
y = input("Enter Y: ")

test_input_text(x,y)

