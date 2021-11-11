FROM dockercore/gcc

MAINTAINER gmolto@dsic.upv.es

COPY . /usr/src/synthalloc

WORKDIR /usr/src/synthalloc

RUN gcc -o synthetic-alloc synthetic-alloc.c -lpthread

CMD ["./synthetic-alloc"]
