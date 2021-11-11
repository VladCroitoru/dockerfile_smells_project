FROM google/golang

RUN go get github.com/ActiveState/tail github.com/satyrius/gonx gopkg.in/redis.v2

RUN curl -O  http://download.redis.io/releases/redis-2.8.19.tar.gz && tar -zxf redis-2.8.19.tar.gz
RUN cd redis-2.8.19 && make
RUN cd / && find redis-2.8.19 -executable -type f -exec mv {} /bin/ \; && rm -rf redis-2.8.19 && apt-get clean

ADD . /

RUN go build back.go

ENTRYPOINT ["/boot.sh"]
