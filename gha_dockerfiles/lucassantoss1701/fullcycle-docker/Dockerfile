FROM golang:1.16-alpine as builder

WORKDIR /

COPY . /
RUN go build

FROM scratch
WORKDIR /

COPY --from=builder goChallenge / 

CMD [ "./goChallenge"]

