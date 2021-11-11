FROM debian
RUN echo "deb http://http.debian.net/debian wheezy         main contrib non-free" > /etc/apt/sources.list
RUN echo "deb http://http.debian.net/debian wheezy-updates main contrib non-free" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y python ssh rsync
COPY ./run.sh /usr/bin/run
RUN chmod +x /usr/bin/run

VOLUME /data
EXPOSE 8000
CMD /usr/bin/run 
