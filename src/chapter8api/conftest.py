# Author: lindafang
# Date: 2020-10-08 16:49
# File: conftest.py
import pytest
import requests


@pytest.fixture(scope='session')
def get_access_token():
    url = 'https://api.weixin.qq.com/cgi-bin/token?' \
          'grant_type=client_credential&appid=wx492fc21d102cfde4&secret=02265e22c54da7f1d443f1b87371f7dd'
    rep = requests.get(url)
    return rep.json()['access_token']
