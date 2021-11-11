FROM ubuntu:14.04
RUN apt-get update && apt-get install -y build-essential
ADD ./mmap-problem.c /app/mmap-problem.c
ADD ./test.txt /app/test.txt
RUN gcc -o /app/mmap /app/mmap-problem.c
WORKDIR /app
CMD ["/app/mmap", "/app/test.txt"]
