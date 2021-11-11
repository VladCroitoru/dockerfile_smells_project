FROM golang:1.9-alpine3.7
ENV TERM=xterm
ENV GOTTY_PERMIT_WRITE=true
EXPOSE 8080
RUN apk add --update nodejs git tmux
RUN go get github.com/yudai/gotty
ADD . /with-gotty
WORKDIR /with-gotty
ENTRYPOINT ["node", "index.js"]
CMD ["top"]
