#   docker run -p 80:80 -e AV_MONGO_URL=mongodb://localhost/ava -t antonikonovalov/avatars

FROM google/golang
ENV AV_HTTP 0.0.0.0:80

ADD . /gopath/src/github.com/antonikonovalov/avatars
WORKDIR /gopath/src/github.com/antonikonovalov/avatars
RUN make

EXPOSE 80
ENTRYPOINT ["/gopath/src/github.com/antonikonovalov/avatars/avatars"]
