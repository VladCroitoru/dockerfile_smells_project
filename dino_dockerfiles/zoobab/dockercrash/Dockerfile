FROM alpine
RUN apk update
RUN apk add build-base
COPY loop.c /root/
WORKDIR /root/
RUN gcc -o loop loop.c
RUN chmod +x /root/loop
CMD ["/root/loop"]
