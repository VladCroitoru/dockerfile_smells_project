# iron/go:dev is the alpine image with the go tools added

FROM golang:1.14.2
WORKDIR /app

# Set an env var that matches your github repo name, replace treeder/dockergo here with your repo name
# Add the source code:

ADD /dist /app/dist
COPY server.go /app

RUN git config --global http.sslVerify false
RUN go mod init mfy/server
RUN go mod tidy 

# Build it:

RUN go build
EXPOSE 5000


ENTRYPOINT ["./server"]