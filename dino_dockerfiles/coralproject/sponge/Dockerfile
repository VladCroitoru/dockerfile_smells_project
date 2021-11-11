# Start from a Debian image with the latest version of Go installed
# and a workspace (GOPATH) configured at /go.
FROM golang:1.6
MAINTAINER Gabriela Rodriguez <gabriela@mozillafoundation.org>

# We are vendoring sponge
ENV GO15VENDOREXPERIMENT="1"

LABEL Name="Sponge" \
      Version="0.1" \
      Vendor="The Coral Project" \
      Description="ETL utility to extract, transform and load data into the Coral's schema." \
      Usage="docker run -v ./strategy.json:/usr/local/strategy.json --env-file ./env.list" \
      License="MIT"\
      Repository="Sponge" \
      Tag="Coral"

# Copy the local package files to the container's workspace.
COPY . /go/src/github.com/coralproject/sponge

# Build & Install
RUN cd /go/src/github.com/coralproject/sponge/cmd/sponge && go install

ENV PATH /go/bin:$PATH

ENTRYPOINT ["sponge"]

CMD ["import"]
