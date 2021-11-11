# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang

# Copy the local package files to the container's workspace.
ADD . /go/src/github.com/ninetwentyfour/go-imago

# Download and install wkhtmltopdf
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y fontconfig libjpeg62-turbo xfonts-base xfonts-75dpi libx11-6 libxext6 libxrender1
ADD http://deis-deps.s3.amazonaws.com/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb /tmp/

# Build the outyet command inside the container.
# (You may fetch or manage dependencies here,
# either manually or with a tool like "godep".)
RUN dpkg -i /tmp/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb &&\
  go get github.com/gorilla/mux &&\
  go get github.com/ninetwentyfour/go-wkhtmltoimage &&\
  go get github.com/zenazn/goji/graceful &&\
  go get gopkg.in/amz.v1/s3 &&\
  go get github.com/garyburd/redigo/redis &&\
  go get github.com/nfnt/resize &&\
  go get github.com/yvasiyarov/gorelic &&\
  go get github.com/yvasiyarov/newrelic_platform_go &&\
  go get github.com/yvasiyarov/go-metrics &&\
  go install github.com/ninetwentyfour/go-imago &&\
  rm -rf /go/src/ &&\
  rm /tmp/wkhtmltox-0.12.2.1_linux-jessie-amd64.deb

# Run the outyet command by default when the container starts.
ENTRYPOINT /go/bin/go-imago

# Document that the service listens on port 6001.
EXPOSE 6001
