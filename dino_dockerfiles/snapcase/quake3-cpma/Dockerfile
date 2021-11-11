FROM jberrenberg/quake3:latest

LABEL maintainer "snapcase"

RUN \
  wget https://playmorepromode.org/files/latest/cpma-1.50-nomaps.zip -O /tmp/cpma-1.50-nomaps.zip && \
  unzip /tmp/cpma-1.50-nomaps.zip -d ~/ioquake3 && \
  rm /tmp/cpma-1.50-nomaps.zip && \
  wget https://playmorepromode.org/files/cpma-mappack-full.zip -O /tmp/cpma-mappack-full.zip  && \
  unzip /tmp/cpma-mappack-full.zip  -d ~/ioquake3/baseq3 && \
  rm /tmp/cpma-mappack-full.zip

ENTRYPOINT ["/home/ioq3srv/ioquake3/ioq3ded.x86_64", "+set", "dedicated", "2", "+set", "fs_game", "cpma"]
