FROM ubuntu:16.10

MAINTAINER tuxflo

RUN apt-get update && apt-get -y install build-essential unzip wget pdftk vim software-properties-common python-software-properties
RUN add-apt-repository ppa:alex-p/tesseract-ocr

RUN apt-get update && apt-get upgrade -y && apt-get install -y incron inotify-tools ocrmypdf tesseract-ocr tesseract-ocr-deu task-spooler

ADD ./mergepdf.sh /opt/mergepdf.sh
RUN chmod a+x /opt/mergepdf.sh
RUN echo "lockfile_dir = /srv/input" >> /etc/incron.conf

RUN adduser --disabled-password --gecos '' r && adduser r sudo && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
RUN echo r >> /etc/incron.allow
USER r

RUN cd /home/r && incrontab -l > mycron && echo '/srv/input IN_CREATE /opt/mergepdf.sh $#' >> mycron && incrontab mycron && rm mycron
USER root
COPY entrypoint.sh /
ENTRYPOINT ["/mergepdf.sh"]
CMD ["/usr/sbin/incrond","-n"]
