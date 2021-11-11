FROM lucaderi/ntopng-docker:latest

ADD redis.conf /etc/redis/redis.conf

ADD server /server

CMD ["/bin/bash","/server"]
