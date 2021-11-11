FROM ubuntu:14.10
MAINTAINER sanders liu <sandersliu@hotmail.com>
ADD . /build
RUN chmod 750 /build/prepare.sh && \
chmod 750 /build/system_services.sh && \
chmod 750 /build/utilities.sh && \
chmod 750 /build/cleanup.sh
RUN /build/prepare.sh && \
/build/system_services.sh && \
/build/utilities.sh && \
/build/cleanup.sh
CMD ["/sbin/my_init"]
