FROM debian:stretch

LABEL maintainer Vincent RAVERA <ravera.vincent@gmail.com>

RUN apt-get update

WORKDIR /mnt/

RUN apt-get install -y git ffmpeg python-pip curl

# Install youtube-dl cmd

RUN curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
RUN chmod a+rx /usr/local/bin/youtube-dl
RUN /usr/local/bin/youtube-dl -U


# Install youtube-dl lib

RUN apt-get install -y python-pip

RUN pip install --upgrade youtube-dl



EXPOSE 8888

CMD /bin/bash
