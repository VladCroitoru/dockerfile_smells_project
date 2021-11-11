FROM node:12.6-alpine as npmbuilder
WORKDIR /root/app
COPY app/package.json .
RUN yarn install --frozen-lockfile 
COPY app/ .
RUN yarn run build

FROM golang:alpine as gobuilder
WORKDIR /go/src/github.com/setecrs/imager
COPY . .
RUN CGO_ENABLED=0 go build -o /go/bin/imager .
WORKDIR /go/src/github.com/setecrs/imager/notify
RUN CGO_ENABLED=0 go build -o /go/bin/notify .

FROM alpine:edge
ENV GRAPHQL_URL http://wekan-hooks-noauth
ENV UDEV_LISTEN localhost:8080
ENV LISTEN 0.0.0.0:80
EXPOSE 80

RUN apk add --no-cache \
      git \
      smartmontools \
      eudev \
      coreutils \
      bash \
      tmux \
      hdparm \
      ddrescue

COPY --from=gobuilder /go/bin/imager /root/imager
COPY --from=gobuilder /go/bin/notify /root/notify
COPY --from=npmbuilder /root/app/build /root/app/build

COPY entrypoint.sh /
ENTRYPOINT [ "/entrypoint.sh" ]

WORKDIR /root/
CMD ./imager
