FROM golang

RUN apt-get update && apt-get dist-upgrade -y && apt-get install --no-install-recommends -y npm
RUN npm install -g bower
RUN ln -s /usr/bin/nodejs /usr/local/bin/node

COPY . /go/src/github.com/holizz/imagedb
WORKDIR /go/src/github.com/holizz/imagedb

RUN bower --allow-root install
RUN go get .

CMD ["imagedb"]
