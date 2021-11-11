FROM ubuntu:18.04

RUN apt-get update                                                      && \
    apt-get -y install build-essential git cmake python3.8 python3-pip  && \
    apt-get -y install libpq-dev postgresql-server-dev-10               && \ 
    apt-get clean

RUN pip3 install flask

# build core
RUN git clone https://github.com/Tyill/zmey.git                   
WORKDIR /zmey/build
RUN cmake -B . -S ../core -DCMAKE_BUILD_TYPE=Release && cmake --build .

# prepare flask app
ENV FLASK_APP=/zmey/web/server
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV LD_LIBRARY_PATH=/zmey/build/Release
RUN printf "[Params]\n \
DbConnectStr=host=192.168.0.104 port=5432 user=alm password=123 dbname=zmeydb connect_timeout=10" \
> /zmey/zmserver.cng

WORKDIR /zmey