FROM golang:1.14 as builder

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt update -y && \
    apt -y install git && \
    go get -u github.com/golang/dep/cmd/dep

COPY src/github.com/fredleger/CocoTelegramParrotBot /go/src/CocoTelegramParrotBot

WORKDIR /go/src/CocoTelegramParrotBot

RUN CGO_ENABLED=0 GOOS=linux go build \
    -i -v -a -installsuffix cgo -gcflags "all=-N -l" \
    -o CocoTelegramParrotBot .

# # adds delve
# RUN go get github.com/derekparker/delve/cmd/dlv && \
#     cd /go/src/github.com/derekparker/delve/cmd/dlv && \
#     CGO_ENABLED=0 GOOS=linux go build \
#         -i -v -a -installsuffix cgo -gcflags "all=-N -l" \
#         -o dlv

# The final image
FROM alpine:3.8

LABEL maintainer="contact@webofmars.com"

# libc6-compat is used when debugging with delve
RUN apk add --no-cache libc6-compat tzdata ca-certificates curl

ENV TG_TOKEN ""

#COPY --from=builder /go/src/CocoTelegramParrotBot/dlv /usr/local/bin/
COPY --from=builder /go/src/CocoTelegramParrotBot/CocoTelegramParrotBot /usr/local/bin/

ENTRYPOINT ["/usr/local/bin/CocoTelegramParrotBot"]