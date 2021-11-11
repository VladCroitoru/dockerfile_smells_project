FROM ubuntu:16.04
ENV DEBIAN_FRONTEND noninteractive

USER root

RUN apt-get -y update && apt-get -y upgrade 
RUN apt-get install -y python
RUN apt-get install -y apache2-utils
RUN apt-get install -y curl
RUN curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
RUN python get-pip.py

RUN pip install radicale

RUN mkdir -p /home/radicale/.config
RUN mkdir -p /data/radicale
RUN ln -s /data/radicale /home/radicale/.config/radicale
RUN useradd -s /bin/false radicale

RUN chown -R radicale /data/radicale/
RUN chown -R radicale /home/radicale/.config

EXPOSE 5232 

VOLUME ["/data/radicale"]

ENV HOME /home/radicale
USER radicale
WORKDIR /home/radicale

CMD ["radicale"]

USER root
