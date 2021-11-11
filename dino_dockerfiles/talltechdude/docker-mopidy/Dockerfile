FROM ubuntu:16.04

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y --force-yes \
        build-essential \
        gettext \
        gir1.2-gstreamer-1.0 \
        gir1.2-gst-plugins-base-1.0 \
        git \
        gstreamer1.0-alsa \
        gstreamer1.0-libav \
        gstreamer1.0-plugins-good \
        gstreamer1.0-plugins-ugly \
        gstreamer1.0-tools \
        libasound2-dev \
        libssl-dev \
        libcurl4-gnutls-dev \
        libexpat1-dev \
        python2.7-dev \
        python-pip \
        python-gst-1.0 \
        unzip \
        alsa-utils \
        wget
RUN pip install -U  Mopidy
RUN pip install -U Mopidy-ALSAMixer

RUN wget -q -O - http://apt.mopidy.com/mopidy.gpg | apt-key add -
RUN echo "deb http://apt.mopidy.com/ stable main contrib non-free" > /etc/apt/sources.list.d/mopidy.list
RUN echo "deb-src http://apt.mopidy.com/ stable main contrib non-free" >> /etc/apt/sources.list.d/mopidy.list
RUN apt-get install -y --force-yes apt-transport-https
RUN apt-get update && \
    apt-get install -y libspotify12 libspotify-dev \
    libffi-dev libffi6
RUN pip install Mopidy-Mobile
RUN pip install Mopidy-MusicBox-Webclient

RUN git clone https://github.com/BlackLight/mopidy-spotify.git
RUN cd mopidy-spotify && git checkout fix/incompatible_playlists
RUN cd mopidy-spotify && python setup.py build install
RUN pip install Mopidy-Spotify-Web

COPY root /
EXPOSE 6680 6600
CMD ["/usr/local/bin/mopidy"]
