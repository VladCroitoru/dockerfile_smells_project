FROM ubuntu:18.04 AS base
LABEL maintainer="Micheal Waltz <docker@ecliptik.com>"

#Setup basic environment
ENV DEBIAN_FRONTEND=noninteractive \
    DOOMSDAY_DEB=doomsday_2.2.2_amd64.deb \
    DOOMSDAY_URL=https://files.dengine.net/archive/ \
    DOOM_WAD=doom1.wad \
    DOOM_URL=http://distro.ibiblio.org/pub/linux/distributions/slitaz/sources/packages/d/

#DIR
WORKDIR /app

#Download Doomsday and install
RUN apt-get update && apt-get install -y --no-install-recommends \
      wget \
      ca-certificates \
      libqt5gui5 \
      libqt5x11extras5 \
      libsdl2-mixer-2.0-0 \
      libxrandr2 \
      libxxf86vm1 \
      libfluidsynth1 \
      libqt5opengl5 \
      libminizip1

#Download shareware doom1 wad
RUN wget $DOOM_URL/$DOOM_WAD -O ./$DOOM_WAD

#Build image
FROM base AS build
RUN wget $DOOMSDAY_URL/$DOOMSDAY_DEB -O /tmp/$DOOMSDAY_DEB

RUN dpkg --install /tmp/$DOOMSDAY_DEB

#Runtime image
FROM base AS run

#Copy files
COPY --from=build /usr /usr
COPY . .

#Doomsday port
EXPOSE 13209

#Run doomsday-server
ENTRYPOINT [ "doomsday-server" ]
CMD [ "--version" ]
