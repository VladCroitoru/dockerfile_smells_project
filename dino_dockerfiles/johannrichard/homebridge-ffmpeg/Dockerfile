FROM oznu/homebridge:latest

# Install latest ffmpeg 
RUN apk add --no-cache ffmpeg

# Install homebridge-camera-ffmpeg
RUN yarn add homebridge-camera-ffmpeg

WORKDIR /homebridge
VOLUME /homebridge

ENV S6_KEEP_ENV=1
