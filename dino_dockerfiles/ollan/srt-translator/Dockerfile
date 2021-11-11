FROM python:2-slim
MAINTAINER Johan Axfors <johan@axfors.se>

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \ 
    apt-get -y install \
                git \
		inotify-tools \
		file \
		bash && \
	apt-get autoremove && \
	apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/apt/archive/*.deb
    
RUN pip install \ 
   goslate \
   requests

ADD ./run.sh /run.sh
RUN chmod 755 /*.sh

VOLUME /app /srt
CMD ["/run.sh"]
