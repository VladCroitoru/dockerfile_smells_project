FROM docker:rc-dind
WORKDIR /usr/local/bin/
RUN rm /usr/local/bin/dockerd-entrypoint.sh
COPY dockerd-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/dockerd-entrypoint.sh
ENTRYPOINT ["dockerd-entrypoint.sh"]
CMD []
