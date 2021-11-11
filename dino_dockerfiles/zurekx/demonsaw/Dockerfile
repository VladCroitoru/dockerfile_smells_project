FROM debian:8.6

RUN apt-get update && apt-get upgrade -y
RUN apt-get install python-gst0.10 \
            gstreamer0.10-plugins-good \
            gstreamer0.10-plugins-ugly -y
RUN apt-get install wget -y
RUN mkdir demonsaw
WORKDIR /root/demonsaw
RUN wget http://demonsaw.com/download/3.1.0/demonsaw_debian_64.tar.gz
RUN tar xzf demonsaw_debian_64.tar.gz
RUN mkdir config
ADD demonsaw.toml /root/demonsaw/config/
ENTRYPOINT [ "./demonsaw_cli", "config/demonsaw.toml"]
