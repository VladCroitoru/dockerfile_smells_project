FROM golang as builder
WORKDIR /go/src/github.com/jakubknejzlik/go-docker-workflow
COPY . .
RUN go get ./... 
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /tmp/app .

FROM docker

WORKDIR /app

COPY --from=builder /tmp/app /usr/local/bin/app

ENV TIMEZONE UTC
# RUN apk --update add docker

# https://serverfault.com/questions/772227/chmod-not-working-correctly-in-docker
RUN chmod +x /usr/local/bin/app

RUN apk add --update tzdata
# RUN curl -fsSL https://get.docker.com/ | sh


ENTRYPOINT []
CMD [ "app", "start" ]