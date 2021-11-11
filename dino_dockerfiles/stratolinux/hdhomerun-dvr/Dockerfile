# Use stratolinux/baseimage-docker
FROM stratolinux/baseimage-docker:0.9.19

# ports needed
EXPOSE 5004
VOLUME ["/recordings"]

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

COPY hdhomerun_record_linux_20161206beta1 /root/
RUN  mv /root/hdhomerun_record_linux_20161206beta1 /root/hdhomerun_record_linux && \
     chmod +x /root/hdhomerun_record_linux

COPY etc/ /etc/

RUN find /etc/service -name run -exec chmod +x {} \;
RUN chmod +x /etc/my_init.d/setup_app

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
