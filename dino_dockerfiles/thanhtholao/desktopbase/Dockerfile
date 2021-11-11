FROM debian:jessie
ADD install.sh /install.sh
RUN /install.sh 
ENTRYPOINT ["/usr/bin/supervisord", "-n"]
#RUN /usr/bin/supervisord -n
RUN apt-get purge leafpad
RUN rm -rf /tmp/* /var/lib/apt/lists/*
