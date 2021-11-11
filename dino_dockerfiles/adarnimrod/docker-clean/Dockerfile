FROM docker:20.10 as docker
RUN wget https://git.shore.co.il/nimrod/rcfiles/-/raw/master/Documents/bin/_docker-clean -O /usr/local/bin/docker-clean && \
    chmod 755 /usr/local/bin/docker-clean
ENTRYPOINT ["/usr/local/bin/docker-clean"]
