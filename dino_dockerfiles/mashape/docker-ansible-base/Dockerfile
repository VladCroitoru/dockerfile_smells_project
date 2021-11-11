FROM williamyeh/ansible:ubuntu14.04

RUN apt-get update \
  && apt-get install -yf python-virtualenv python-distutils-extra python-apt make git \
    libssl-dev libffi-dev python-dev libcurl4-openssl-dev

RUN pip install https://pypi.python.org/packages/3.4/s/setuptools/setuptools-11.3.1-py2.py3-none-any.whl
