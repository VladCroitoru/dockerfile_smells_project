FROM redis:3.2

RUN apt update
RUN apt install curl git -y

RUN curl https://dl.google.com/go/go1.10.linux-amd64.tar.gz -o /tmp/go1.10.linux-amd64.tar.gz
RUN tar -C /usr/local -xzf /tmp/go1.10.linux-amd64.tar.gz
RUN rm /tmp/go1.10.linux-amd64.tar.gz

RUN /usr/local/go/bin/go get github.com/go-redis/redis
RUN /usr/local/go/bin/go get google.golang.org/grpc
RUN /usr/local/go/bin/go get gopkg.in/yaml.v2
RUN /usr/local/go/bin/go get github.com/Sirupsen/logrus
RUN /usr/local/go/bin/go get github.com/fasthall/gochariots

COPY . /root/go/src/github.com/fasthall/redis-cache-for-lowgo
RUN /usr/local/go/bin/go install github.com/fasthall/redis-cache-for-lowgo
RUN ln -s /root/go/bin/redis-cache-for-lowgo /usr/local/bin/

COPY docker-entrypoint.sh /usr/local/bin/
COPY redis.conf /
CMD ["docker-entrypoint.sh"]

