FROM busybox:1.26.2-glibc
MAINTAINER Opryshko Alexandr <sclif13@gmail.com>

COPY lib/* /lib/
RUN ln -sf /lib/libpthread-2.19.so /lib/libpthread.so.0
ADD https://busybox.net/downloads/binaries/ssl_helper-x86_64 /bin/ssl_helper
RUN chmod 755 /bin/ssl_helper