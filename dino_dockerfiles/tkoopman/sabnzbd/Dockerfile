FROM ubuntu:bionic as builder
  COPY build/packages.sh /root/build/
  RUN chmod +x /root/build/packages.sh && \
      mkdir -p /root/src /root/bin && \
      /root/build/packages.sh
  
  COPY build/nasm.sh /root/build/
  RUN chmod +x /root/build/nasm.sh && \
      /root/build/nasm.sh
  
  COPY build/aom.sh /root/build/
  RUN chmod +x /root/build/aom.sh && \
      /root/build/aom.sh
  
  COPY build/ffmpeg.sh /root/build/
  RUN chmod +x /root/build/ffmpeg.sh && \
      /root/build/ffmpeg.sh

FROM linuxserver/sabnzbd:latest
LABEL maintainer "T Koopman"

COPY --from=builder /root/bin/* /usr/bin/
COPY --from=builder /root/packages /root/packages
COPY ffmpegvalidator /scripts/ffmpegvalidator

RUN chmod +x /scripts/ffmpegvalidator && \
    apt-get update && \
    apt-get install --no-install-recommends -y `cat /root/packages` && \
    rm -f /root/packages && \
    rm -rf /var/lib/apt/lists/* && \
    /usr/bin/ffmpeg -version
