FROM golang:1.7

LABEL maintainer "Salman Ahmed <salman.great@gmail.com>"

# Install all tools required to build the `proton c` library
RUN apt-get update && apt-get install -y \
	cmake \
	cmake-curses-gui \
	uuid-dev \
	libssl-dev \
	libsasl2-2 \
	libsasl2-dev \
	libsasl2-modules \
	bsdtar

ENV QPID_PROTON_DOWNLOAD_URL https://github.com/apache/qpid-proton/archive/master.zip

# Make the build directory
RUN mkdir -p /qpid-proton/build

# Go to the `qpid-proton` directory where we will download the zip file
WORKDIR /qpid-proton

# Download the `qpid-proton` zip and extract all the contents and delete the zip
RUN curl -fsSL "$QPID_PROTON_DOWNLOAD_URL" -o /qpid-proton/qpid-proton.zip \
	&& bsdtar -xf /qpid-proton/qpid-proton.zip -s'|[^/]*/||' \
	&& rm /qpid-proton/qpid-proton.zip

# Go to build directory
WORKDIR /qpid-proton/build

# Build the qpid-proton (C language) library (and then delete `/qpid-proton` directory)
RUN cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DSYSINSTALL_BINDINGS=ON \
	&& make all \
	&& make install \
	&& rm -rf /qpid-proton

# Download Go `qpid.apache.org/amqp` and `qpid.apache.org/electron` packages
RUN go-wrapper download \
	qpid.apache.org/amqp \
	qpid.apache.org/electron

# Copy application to the container
COPY app /go/src/app

# Change working directory back to it's original
WORKDIR /go/src/app