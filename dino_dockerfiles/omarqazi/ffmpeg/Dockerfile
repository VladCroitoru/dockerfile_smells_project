FROM          golang:latest
MAINTAINER    Omar Qazi <omar@smick.co>
RUN apt-get update
RUN apt-get -y --force-yes dist-upgrade
RUN apt-get install -y --force-yes ffmpeg
RUN apt-get install -y python-pip
RUN pip install awscli
RUN pip install youtube-dl
ENTRYPOINT ["ffmpeg", "--help"]
