FROM redborder/dev-containers:golang

RUN yum install -y libpcap-devel

WORKDIR /app

RUN go get github.com/Masterminds/glide
RUN go get github.com/Bigomby/gopiper/...

RUN go get github.com/redBorder/gopiper-components/...; \
  cd /go/src/github.com/redBorder/gopiper-components; \
  go get; \
  make; \
  mv build/*.so /app/

RUN cd /go/src/github.com/Bigomby/gopiper; \
  make install

COPY udpreplay.lua /app/udpreplay.lua

CMD gopiper --pipe udpreplay.lua
