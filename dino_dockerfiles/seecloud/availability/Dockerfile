FROM ubuntu:16.04

RUN apt-get update && apt-get install --yes wget python-dev build-essential

# ubuntu's pip is too old to work with the version of requests we
# require, so get pip with get-pip.py
RUN wget https://bootstrap.pypa.io/get-pip.py && \
  python get-pip.py && \
  rm -f get-pip.py

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt \
    && python setup.py install

EXPOSE 5000
