FROM gcc:latest
MAINTAINER Runcy Oommen Version: 0.1

COPY hello.c /usr/local
WORKDIR /usr/local

RUN gcc -o hello hello.c
CMD ["./hello"]
