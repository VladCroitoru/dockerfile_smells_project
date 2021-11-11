FROM dduportal/docker-compose
MAINTAINER thibault.coupin@ign.fr

RUN mkdir /kavarok4
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/kavarok4
ENV APP_NAME=kavarok4

ENTRYPOINT ["/bin/bash"]
CMD ["up"]

ADD scripts /kavarok4/
RUN chmod +x /kavarok4/*
