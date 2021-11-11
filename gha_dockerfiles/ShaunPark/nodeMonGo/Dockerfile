FROM coolage/node-mon-go-base AS build

# RUN apk update && apk add git && apk add curl

WORKDIR /go/src/github.com/ShaunPark/nodeMonGo
# COPY go.mod . 
# COPY go.sum . 
# RUN go mod vendor

COPY . .

RUN go build -o /nodeMonGo .

FROM alpine:3.14
ADD zoneinfo.zip /
ENV ZONEINFO /zoneinfo.zip
RUN apk update && apk add ca-certificates
RUN apk --no-cache add tzdata && \
        cp /usr/share/zoneinfo/Asia/Seoul /etc/localtime && \
        echo "Asia/Seoul" > /etc/timezone
RUN addgroup -S user && adduser -S user -G user
USER user
COPY --from=build /nodeMonGo /nodeMonGo
