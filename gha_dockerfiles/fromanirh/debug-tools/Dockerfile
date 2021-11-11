FROM registry.access.redhat.com/ubi8/ubi-minimal:latest
COPY _output /usr/local/bin
COPY run.sh /run.sh
COPY help.sh /help.sh
# no tool is more important than others
ENTRYPOINT ["/run.sh"]
CMD ["/help.sh"]
