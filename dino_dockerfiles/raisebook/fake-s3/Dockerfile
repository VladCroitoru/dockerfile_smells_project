FROM debian:jessie
MAINTAINER Raisebook <engineering@raisebook.com>

ENV DEBIAN_FRONTEND noninteractive

# install Ruby
RUN apt-get update && apt-get install -yqq ruby rubygems-integration build-essential git

# install fake-s3
RUN mkdir /fakes3
WORKDIR /fakes3
COPY . /fakes3/

RUN gem build fakes3.gemspec
RUN gem install ./fakes3-0.2.4.gem

# run fake-s3
RUN mkdir -p /fakes3_root
ENTRYPOINT ["/usr/local/bin/fakes3"]
CMD ["-r",  "/fakes3_root", "-p",  "4569"]
EXPOSE 4569
