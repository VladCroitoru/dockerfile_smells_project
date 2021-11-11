FROM ruby:2.3.1-onbuild
MAINTAINER Peter Ericson <pdericson@gmail.com>

# https://github.com/Yelp/dumb-init
RUN curl -fLsS -o /usr/local/bin/dumb-init https://github.com/Yelp/dumb-init/releases/download/v1.0.2/dumb-init_1.0.2_amd64 && \
chmod +x /usr/local/bin/dumb-init

ENTRYPOINT ["/usr/local/bin/dumb-init"]

CMD ["riemann-mesos"]
