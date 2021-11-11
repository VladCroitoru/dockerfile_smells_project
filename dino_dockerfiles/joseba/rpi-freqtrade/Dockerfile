FROM resin/raspberrypi3-python:3

RUN [ "cross-build-start" ]

# Install TA-lib
RUN apt-get update && apt-get -y install build-essential && apt-get clean
RUN curl -L http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz | \
  tar xzvf - && \
  cd ta-lib && \
  ./configure && make && make install && \
  cd .. && rm -rf ta-lib
ENV LD_LIBRARY_PATH /usr/local/lib

RUN mkdir /freqtrade
WORKDIR /freqtrade
COPY requirements.txt /freqtrade/
RUN pip install -r requirements.txt
COPY . /freqtrade/
RUN pip install -e .

RUN [ "cross-build-end" ]

CMD ["freqtrade"]
