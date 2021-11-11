FROM debian:stretch
LABEL MAINTAINER="Sylvain Lamontagne <sylvain.lamontagne@gmail.com>"

RUN apt-get update && \
    apt-get --no-install-recommends install -y wget libyaml-dev python3-minimal python3-pip python3-dev python3-setuptools python3-yaml python3-wheel cron && \
    apt-get autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install awscli

ADD start.sh /start.sh
RUN chmod +x /start.sh
ADD snapshot.sh /snapshot.sh
RUN chmod +x /snapshot.sh

RUN mkdir /root/.aws

ENTRYPOINT ["/start.sh"]
CMD [""]
