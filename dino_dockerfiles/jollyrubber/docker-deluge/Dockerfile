FROM ubuntu

ENV DELUGE_CONFIG_DIR /config
ENV DELUGE_DL_DIR /downloads
ADD entrypoint.sh /entrypoint.sh

RUN apt-get update && \
    apt-get install -y \
                    --no-install-recommends \
                    deluged \
                    deluge-webui \
                    ffmpeg && \
    apt-get clean && \
    chmod +x entrypoint.sh

EXPOSE 8112
VOLUME $DELUGE_CONFIG_DIR $DELUGE_DL_DIR
ENTRYPOINT ["./entrypoint.sh"]