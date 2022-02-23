def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f"expected {expected_result}, got {actual_result}"

x = input("Enter X: ")
y = input("Enter Y: ")

test_input_text(x,y)

print('x = y')
print('test is OK')

#test_input_text(8,11)
#test_input_text(11,11)
#test_input_text(15,11)







# def test_input_text(expected_result, actual_result):
#     # ваша реализация, напишите assert и сообщение об ошибке
# #    actual_result = "11"
#     #assert 11 == 11, "Should be 11"
#
# #test_input_text(11,112)
#
#     assert (8 == 11), f"........."
#
# test_input_text(8, 11)
