FROM python:2.7

EXPOSE 80

WORKDIR /home
ADD server.sh /home/server.sh
RUN chmod +x /home/server.sh

CMD /home/server.sh