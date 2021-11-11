FROM ubuntu:14.04
RUN apt-get update && \
    apt-get install -y curl vim

ENTRYPOINT ["ping"]
CMD ["-c", "25", "localhost"]
