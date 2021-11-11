FROM golang:alpine as build

RUN addgroup -S -g 500 recursivecall         && \
    adduser -S -u 500 -G recursivecall recursivecall   && \
    mkdir -p $GOPATH/src/recursivecall

WORKDIR $GOPATH/src/recursivecall

COPY . ./

RUN CGO_ENABLED=0 go build -installsuffix cgo -ldflags '-w -s' -o recursivecall

###################################

FROM scratch

COPY --from=build /go/src/recursivecall/recursivecall /
COPY --from=build /etc/passwd /etc/group /etc/

EXPOSE 3000

USER recursivecall:recursivecall

ENTRYPOINT ["./recursivecall"]
