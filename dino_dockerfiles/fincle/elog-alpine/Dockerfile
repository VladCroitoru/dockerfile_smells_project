FROM alpine:latest

MAINTAINER Andrew Wade <awade@ligo.caltech.edu>

# Set the working directory to /app
WORKDIR /builddir

# Copy the current directory contents into the container at /app
ADD . /builddir

# Make port 80 available to the world outside this container
EXPOSE 8080

RUN apk update -q && \
    apk add --no-cache openssl-dev imagemagick && \
    apk add --no-cache --virtual .build-deps build-base git && \
    git clone https://bitbucket.org/ritt/elog --recursive && \
    cd /builddir/elog && \
    make && \
    make install && \
    apk del .build-deps && \
    rm -r /builddir/elog/

# Adding users and config files from build folder
COPY ./elogd.cfg /usr/local/elog/elogd.cfg

# This block only modifies permissions for non-mounted versions
RUN adduser -S -g elog elog && \
    addgroup -S elog && \
    cd /usr/local/elog/ && \
    chown elog:elog elogd.cfg && \
    chown -R elog:elog logbooks

CMD ["/usr/local/sbin/elogd", "-p", "8080", "-c", "/home/elogd.cfg"]
