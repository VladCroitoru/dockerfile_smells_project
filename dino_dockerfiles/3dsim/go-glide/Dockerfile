FROM golang:1.9

ENV GLIDE_VERSION v0.12.3

# Install glide
WORKDIR $GOPATH/src/github.com/Masterminds
RUN git clone https://github.com/Masterminds/glide.git
RUN cd glide && git checkout $GLIDE_VERSION && make bootstrap-dist && make install
WORKDIR $GOPATH
