FROM debian:stretch-slim
MAINTAINER Jose Peleteiro <jose@peleteiro.net>

ENV DEBIAN_FRONTEND noninteractive

ENV PORT=4569
ENV HTTPS_CERT_PATH==/srv/cert/fakes3.crt
ENV HTTPS_KEY_PATH==/srv/cert/fakes3.key

# install Ruby
RUN apt-get update && apt-get install -yqq dumb-init ruby rubygems-integration

# install fake-s3
RUN gem install fakes3 -v 1.2.1

# run fake-s3
RUN mkdir -p /srv/fakes3

# run
ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["sh", "-c", "/usr/local/bin/fakes3 -r /srv/fakes3 -p $PORT --sslcert=$HTTPS_CERT_PATH --sslkey=$HTTPS_KEY_PATH"]