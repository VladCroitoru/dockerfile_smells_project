FROM alpine:3.4

MAINTAINER kevin, https://github.com/thekevinchi/joinbot

# Install Dependencies
RUN apk update \
 && apk add python3-dev ca-certificates gcc make linux-headers musl-dev ffmpeg libffi-dev

# Add project source
ADD . /usr/src/MusicBot
WORKDIR /usr/src/MusicBot

# Create volume for mapping the config
VOLUME /usr/src/MusicBot/config
VOLUME /usr/src/MusicBot/audio_cache
VOLUME /usr/src/MusicBot/data
VOLUME /usr/src/MusicBot/logs


# Install pip dependencies
RUN pip3 install -r requirements.txt

CMD python3.5 run.py
