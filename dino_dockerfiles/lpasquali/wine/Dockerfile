FROM debian:stable-slim

MAINTAINER Luca Pasquali <lpasquali@gmail.com>

RUN addgroup --system psilocybe \
    && adduser \
    --home /home/semilanceata \
    --disabled-password \
    --shell /bin/bash \
    --gecos "user for running things under wine" \
    --ingroup psilocybe \
    --quiet \
    semilanceata
RUN adduser semilanceata sudo
RUN adduser semilanceata users
RUN echo "semilanceata:psilocybe" | chpasswd

RUN dpkg --add-architecture i386 \
    && apt-get update \
    && apt-get upgrade -y \
    && apt-get install -y sudo curl unzip ca-certificates wget rename procps \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y xauth \
    && apt-get install -y x11-apps wine wine32 \
    && rm -rf /var/lib/apt/lists/*


#RUN curl -SL "https://raw.githubusercontent.com/Winetricks/winetricks/master/src/winetricks" -o /usr/local/bin/winetricks
#RUN chmod +x /usr/local/bin/winetricks

USER semilanceata
ENV HOME /home/semilanceata
ENV WINEPREFIX /home/semilanceata/.wine
ENV WINEARCH win32
WORKDIR /home/semilanceata


USER root
COPY waitonprocess.sh /scripts/
RUN chmod +x /scripts/waitonprocess.sh 
RUN rm -rf /usr/share/man \
    && rm -rf /usr/share/doc

# Install .NET Framework 4.0
USER semilanceata
RUN wine wineboot --init \
        && /scripts/waitonprocess.sh wineserver \
        && winetricks --unattended dotnet40 dotnet_verifier \
        && /scripts/waitonprocess.sh wineserver
