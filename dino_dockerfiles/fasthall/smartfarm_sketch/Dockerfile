FROM ubuntu:xenial 
MAINTAINER Wei-Tsung Lin <fasthall@gmail.com>

RUN apt-get update
RUN apt-get install -y arduino-core git

RUN mkdir /smartfarm_sketch

COPY ./ /smartfarm_sketch/
WORKDIR /smartfarm_sketch/

ENTRYPOINT ["sh"]
CMD ["build.sh", "sketch/main.cpp"]
