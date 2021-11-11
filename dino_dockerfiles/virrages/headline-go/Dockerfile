FROM golang:1.7

COPY . /headline
WORKDIR /headline

RUN go get && go install && headline-go &

EXPOSE 80:8080
