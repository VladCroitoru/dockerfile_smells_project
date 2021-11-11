FROM radial/busyboxplus:curl
COPY scripts/* /usr/local/bin/
RUN /usr/local/bin/fetch-templates.sh
ENTRYPOINT ["/usr/local/bin/stream-templates.sh"]
