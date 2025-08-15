import os
import pytest

if __name__ == '__main__':
    pytest.main(["-sq","./test1/test_address.py","--clean-alluredir","--alluredir=./allure/tmp1"])
    # os.system("allure generate ./allure/tmp -o ./allure/report -c")