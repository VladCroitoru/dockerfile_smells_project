FROM node:lts as opencv4nodejsBuilder
LABEL author="Andreas Sehr"
WORKDIR /app

ENV NODE_OPENCV_VERSION 5.6.0
ENV DEST_DIR ./node_modules/opencv-build/opencv/build/

RUN apt-get update && apt-get install -y --no-install-recommends \
   cmake \
   pkg-config && \
   # Cleaning up
  apt autoremove -y && \
  rm -rf /var/lib/apt/lists/* 
RUN npm init -y && \
  # Build
  npm install --save opencv4nodejs@$NODE_OPENCV_VERSION
RUN find / -name "libopencv_core*"  
  # Cleaning up (saves over 1Gb)
RUN du -hs . && du -hs ${DEST_DIR} && \
  find ${DEST_DIR}/* ! -name 'lib64' ! -name 'lib' -type d -exec rm -rf {} + && \
  find ${DEST_DIR} -type f -maxdepth 1 -exec rm -rf {} + && \
  du -hs . && du -hs ${DEST_DIR}
RUN find / -name "libopencv_core*"  

FROM node:lts

# ENV OPENCV_VERSION 4.0.1
ENV NODE_OPENCV_VERSION 5.6.0
ENV STORAGE_DIR /mnt/sorted/
ENV CACHE_DIR /mnt/cache/
ENV SERVER_DIR /app
ENV CLIENT_DIR /app/client

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
  libimage-exiftool-perl \
  libvips-dev \
  ffmpeg \
  libgtk2.0-dev \
  libavcodec-dev \
  libavformat-dev \
  libswscale-dev && \
# Cleaning up
  apt autoremove -y && \
  rm -rf /var/lib/apt/lists/* 

COPY --from=opencv4nodejsBuilder /app $SERVER_DIR/

# Create app directories
RUN  mkdir -p $STORAGE_DIR $CACHE_DIR $CLIENT_DIR
