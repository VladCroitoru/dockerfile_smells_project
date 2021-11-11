FROM ubuntu

# Major dependencies
RUN apt-get -y update && \
apt-get -y install python3 espeak gstreamer1.0-tools python3-pip mongodb

# pyzmq (from requirements.txt) dependency
RUN apt-get -y install libzmq5 \
# provides rtpL16pay plugin
gstreamer1.0-plugins-good \
# provides audioparse plugin
gstreamer1.0-plugins-bad \
# chatterbot (from requirements.txt) dependencies
pandoc git

ADD . /app
WORKDIR /app

RUN pip3 install -r requirements.txt && \
# Starts mongodb
mkdir -p /data/db && (mongod &) && ./scripts/wait-mongo.sh && \
# Creates wav_sink/audio_pipe fifo and populates mongodb
python3 mysetup.py && \
# Stops mongodb
printf 'use admin\ndb.shutdownServer()' | mongo

# IP address to stream audio to. May need to override on runtime. E.g.:
# docker run -it --rm -e STREAM_TARGET=192.168.0.16 gaboose/talkbots
ENV STREAM_TARGET 172.17.0.1

# chatter.py parameter. Output a random line every this many seconds.
# Override with -e BREAKOUT_SECONDS=60
ENV BREAKOUT_SECONDS 300

CMD mongod & ./scripts/wait-mongo.sh && (python3 chatter.py ${BREAKOUT_SECONDS} & python3 wav_pump.py & ./gst-pipeline.sh)
