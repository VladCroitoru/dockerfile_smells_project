FROM golang:1.8.3

ADD . /app
RUN cd /app && make
RUN mkdir /cache/

EXPOSE 80
CMD ["/app/app", "--cache-path", "/cache/"]
