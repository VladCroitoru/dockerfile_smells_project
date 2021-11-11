From danishabdullah/micro-jupyter:latest

ENV GOPATH /go
ENV PATH $GOPATH/bin:$PATH
RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >> /etc/apk/repositories \
  && echo '@community http://nl.alpinelinux.org/alpine/edge/community' >> /etc/apk/repositories \
  && apk update && apk upgrade \
  && apk add curl make git bzr mercurial go@community zeromq-dev \
  && rm -rf /var/cache/apk/* \
  && mkdir -p "$GOPATH/src" "$GOPATH/bin" \
  && chmod -R 777 "$GOPATH"

# install gophernotes
RUN go get golang.org/x/tools/cmd/goimports \
 && go get -tags zmq_4_x github.com/gophergala2016/gophernotes \
 && mkdir -p ~/.ipython/kernels/gophernotes \
 && cp -r $GOPATH/src/github.com/gophergala2016/gophernotes/kernel/* ~/.ipython/kernels/gophernotes

EXPOSE 8888
CMD ["jupyter", "notebook"]