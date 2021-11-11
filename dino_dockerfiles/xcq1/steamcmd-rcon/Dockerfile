FROM xcq1/steamcmd
LABEL maintainer="mail@tobiaskuhn.de"

ENV RCON_HOST "localhost"
ENV RCON_PORT "27015"
ENV RCON_PASSWORD ""
ENV RCON_HEALTH_COMMAND ""
ENV RCON_HEALTH_REGEXP ""

USER root
RUN apt update && \
	apt install -y python && \
	apt clean

ADD SourceRcon.py /home/steam/rcon/SourceRcon.py
ADD healthcheck.py /home/steam/rcon/healthcheck.py
ADD healthcheck.sh /home/steam/rcon/healthcheck.sh

HEALTHCHECK --interval=1m --retries=5 CMD /home/steam/rcon/healthcheck.sh

USER steam
