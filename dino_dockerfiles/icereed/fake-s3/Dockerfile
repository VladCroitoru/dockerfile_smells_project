FROM debian:jessie
MAINTAINER Larry Howard <larry.howard@vanderbilt.edu>

ENV DEBIAN_FRONTEND noninteractive

# install Ruby
RUN apt-get update && apt-get install -yqq ruby rubygems-integration

# install fake-s3
RUN gem install fakes3 -v 0.2.5

# run fake-s3
ENV HTTP_PORT 4569
RUN mkdir -p /fakes3_root && chmod 0777 /fakes3_root
VOLUME /fakes3_root
ENTRYPOINT ["/usr/local/bin/fakes3"]
CMD ["-r",  "/fakes3_root", "-p",  "${HTTP_PORT}"]
EXPOSE 4569
