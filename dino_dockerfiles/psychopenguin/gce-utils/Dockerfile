FROM python:3-alpine

RUN apk add --no-cache gcc g++ make openlibm-dev openssl-dev
RUN pip install --upgrade pip
RUN pip install pipenv
WORKDIR /usr/local/src
ADD Pipfile .
ADD Pipfile.lock .
RUN pipenv install --system
ADD . .
RUN python setup.py install
WORKDIR /
