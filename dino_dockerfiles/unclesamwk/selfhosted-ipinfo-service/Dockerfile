FROM python
MAINTAINER Sam <unclesamwk@googlemail.com>

RUN apt update \
 && apt upgrade -y

RUN pip install Flask-HTTPAuth flask

RUN git clone https://github.com/chrislim2888/IP2Location-Python.git \
 && cd IP2Location-Python \
 && python setup.py build \
 && python setup.py install

ADD api.py .

CMD python api.py
