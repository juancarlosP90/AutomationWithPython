import pytest

# Test case code must be written inside a method
#  name must be started with test

a=101


#Decorator
#@pytest.mark.skip

#Conditional skip
#@pytest.mark.skipif(a>100, reason="testing mood")

def test_tc001_LoginLogoutTesting():
    print("this is out test case code.....")
    print("this is end of my test cases.....")


def test_tc003_Login_Logout_Invalid_Credentials():
    print("test # 3")
    print("End test case")


