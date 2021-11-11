FROM hhcordero/docker-jmeter-server

MAINTAINER Hector Cordero <hhcordero@gmail.com>

ENV TEST_DIR default
ENV TEST_PLAN test-plan
ENV REMOTE_HOSTS 127.0.0.1

COPY load_tests /
COPY docker-entrypoint.sh /

ENTRYPOINT ["/docker-entrypoint.sh"]
