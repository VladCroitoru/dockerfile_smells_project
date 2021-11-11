FROM python:2

RUN pip install cheetah

RUN groupadd -r -g 1666 torrent && \
    useradd --no-log-init --no-user-group --system --uid 1666 -g torrent torrent && \
		mkdir -p /home/torrent && \
		chown torrent:torrent /home/torrent
USER torrent 
WORKDIR /home/torrent
RUN git clone --depth 1 https://github.com/SickRage/SickRage.git torrent

VOLUME state
EXPOSE 8081
ENTRYPOINT python2 ./torrent/SickBeard.py --datadir=./state

