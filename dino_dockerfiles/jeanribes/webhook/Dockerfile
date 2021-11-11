FROM python:2.7.15

COPY docker-hook /webhook
COPY deploy.sh /deploy.sh
COPY init.sh /init.sh
RUN chmod a+x /init.sh;chmod a+x /deploy.sh; pip install requests
#RUN apt update && apt install git
EXPOSE 80
VOLUME /repo
CMD /init.sh
