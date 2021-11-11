FROM debian:stable-slim

# Allows passing in a different script name, if desired.
ENV LIQUIDSOAP_SCRIPT /etc/liquidsoap/liquidsoap.liq

# Add package repo
RUN echo "deb http://deb.debian.org/debian stable main contrib non-free" > /etc/apt/sources.list

# Set up dependencies
RUN apt-get -y update && \
  apt-get -y install \
    dnsutils \
    telnet \
    build-essential \
    wget \
    curl \
    telnet \
    libmad0-dev \
    libshout3-dev \
    libvorbis-dev \
    libfdk-aac-dev \
    libid3tag0-dev \
    libmad0-dev \
    libshout3-dev \
    libasound2-dev \
    libpcre3-dev \
    libmp3lame-dev \
    libogg-dev \
    libtag1-dev \
    libssl-dev \
    libtool \
    libflac-dev \
    libogg-dev \
    libsamplerate-dev \
    libavutil-dev \
    libopus-dev \
    autotools-dev \
    autoconf \
    automake \
    ocaml-nox \
    opam \
    m4

# Set up filesystem and user
USER root
RUN useradd -m liquidsoap
RUN mkdir /var/log/liquidsoap
RUN chown -R liquidsoap:liquidsoap /var/log/liquidsoap
RUN chmod 766 /var/log/liquidsoap
RUN mkdir /etc/liquidsoap && chmod -R 755 /etc/liquidsoap

# Switch over so we can install OPAM
USER liquidsoap

# Initialize OPAM and install Liquidsoap and asssociated packages
RUN echo n | opam init
RUN opam update
RUN eval `opam config env`
RUN echo y | opam install ssl opus cry flac inotify lame mad ogg fdkaac samplerate taglib vorbis xmlplaylist liquidsoap

# Expose ports for harbor connections and telnet server, respectively
EXPOSE 8080
EXPOSE 8011

# Start Liquidsoap with a path to the script defined in the variable
ENTRYPOINT /home/liquidsoap/.opam/system/bin/liquidsoap $LIQUIDSOAP_SCRIPT
