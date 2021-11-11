FROM dockerfile/python
MAINTAINER Chris Goller <goller@gmail.com>

RUN apt-get update
RUN apt-get install -qq -y build-essential python-dev libev4 libev-dev
WORKDIR /
ADD . /usr/src/casstest
RUN pip install -e /usr/src/casstest
CMD run-cass-test
