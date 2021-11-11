# DOCKER VERSION 1.8.2

FROM python

MAINTAINER Tim "XBigTK13X" Kretschmer (tim@simplepathstudios.com)

ENV OLAVA_ENV="production"

ADD ./ /root/olava

WORKDIR /root/olava

RUN chmod +x script/app/*.sh

WORKDIR /root/olava

RUN script/app/install.sh

ENTRYPOINT ["/bin/bash","-c"]

CMD ["script/app/start.sh"]