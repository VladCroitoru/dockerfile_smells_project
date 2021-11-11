FROM golang:1.4
MAINTAINER Vojtech Bartos <hi@vojtech.me>

# application in release mode
ENV GIN_MODE release

RUN mkdir -p /go/src/dicewa.re
COPY . /go/src/dicewa.re
WORKDIR /go/src/dicewa.re

# nodejs installation for frontend
RUN \
  apt-get install -y curl && \
  curl -sL https://deb.nodesource.com/setup_4.x | bash - && \
  apt-get install -y nodejs

# go installation for backend
RUN go-wrapper download
RUN go-wrapper install

# installing dependencies
RUN npm install
RUN npm run build

CMD ["go-wrapper", "run", "start"]

EXPOSE 8000
