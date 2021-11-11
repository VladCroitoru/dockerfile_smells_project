FROM google/cloud-sdk:171.0.0-alpine
MAINTAINER Arik Kfir <arik@infolinks.com>
COPY docker-login.sh /usr/local/bin/
RUN chmod a+x /usr/local/bin/docker-login.sh
ENTRYPOINT ["/usr/local/bin/docker-login.sh"]
