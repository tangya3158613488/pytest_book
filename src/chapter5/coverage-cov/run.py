# Author: lindafang
# Date: 2020-07-14 10:24
# File: run.py

import pytest

if __name__ == '__main__':
    pytest.main([r"--cov=D:\学习资料\pytest框架与自动化测试应用\pytest_book\src\chapter5\coverage-cov", "--cov-report=html",
                 r"--cov-config=D:\学习资料\pytest框架与自动化测试应用\pytest_book\src\chapter5\coverage-cov\.coveragerc"])
