FROM phusion/baseimage:0.9.17
CMD ["/sbin/my_init"]

COPY container /builder/
RUN /builder/setup.sh

EXPOSE 22
VOLUME ["/data"]
