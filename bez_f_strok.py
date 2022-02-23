def test_input_text(expected_result, actual_result):
    try:
        assert expected_result == actual_result
        print('x = y')
        print('test is OK')
    except AssertionError:
        #print("expected", {expected_result}, "got", {actual_result})
        print("expected " + expected_result + ", got " + actual_result)

expected_result = input("Enter X: ")
actual_result = input("Enter Y: ")

test_input_text(expected_result, actual_result)


# assert expected_result == actual_result, \
#         "expected " + expected_result + ", got " + actual_result