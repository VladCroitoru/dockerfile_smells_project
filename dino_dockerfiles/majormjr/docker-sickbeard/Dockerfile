FROM alpine

RUN apk add --update python git wget
WORKDIR /tmp
RUN wget http://pypi.python.org/packages/source/C/Cheetah/Cheetah-2.4.4.tar.gz
RUN tar -zxvf Cheetah-2.4.4.tar.gz && cd Cheetah-2.4.4 && python setup.py install

COPY docker-entrypoint.sh /
RUN chmod 775 /docker-entrypoint.sh

VOLUME /sickbeard
VOLUME /video_downloads

EXPOSE 8081

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["/docker-entrypoint.sh"]
