FROM kenhv/kensurbot:debian

RUN set -ex \
    && git clone -b dev https://github.com/jayrfs/kidneybot /root/userbot \
    && chmod 777 /root/userbot

WORKDIR /root/userbot/

CMD ["python3", "-m", "userbot"]
