
# Nginx
#
# VERSION               0.0.1

FROM ubuntu
LABEL Description="This image is used to start the foobar executable" Vendor="ACME Products" Version="1.0"

EXPOSE 8888
EXPOSE 8080

RUN apt-get update && apt-get install -y golang git
WORKDIR /root
ENV GOPATH=/root/go

RUN git clone https://github.com/YoungApple/wasoso.xyz.git
RUN go get github.com/gin-gonic/gin
RUN cd wasoso.xyz

CMD ["go", "run", "main.go"]
