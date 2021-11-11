FROM debian:jessie

RUN apt-get update \
  && apt-get install -y \
     gcc make libncurses5-dev git \
     libmad0-dev \
     libmp4v2-dev \
     libwavpack-dev \
     libflac-dev \
     libvorbis-dev \
     libpulse-dev \
     alsa-utils libasound2-dev

RUN git clone https://github.com/cmus/cmus.git /usr/src/cmus

RUN cd /usr/src/cmus \
  && ./configure \
  && make \
  && make install

ENV HOME /home/user
RUN useradd --create-home --home-dir $HOME user \
  && mkdir -p $HOME/.config/cmus \
  && chown -R user:user $HOME

USER user
WORKDIR $HOME
ENV USERNAME user
CMD ["cmus"]
