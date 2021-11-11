FROM ubuntu:16.04

RUN apt-get update && apt-get install -y software-properties-common python-software-properties
RUN add-apt-repository -y ppa:stebbins/handbrake-releases
RUN apt-get update && apt-get install -y make git mkvtoolnix handbrake-cli mplayer ffmpeg mp4v2-utils linux-headers-generic build-essential dkms ruby ruby-dev
RUN gem install video_transcoding

RUN mkdir /src/
WORKDIR /src

COPY transcoder.py /src/
RUN chmod +x transcoder.py
ENTRYPOINT ["python", "transcoder.py"]
