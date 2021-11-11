FROM buildpack-deps:jessie

RUN apt-get update && \
    apt-get install -y \
            locales \
            less \
            octave-control \
            octave-image \
            octave-io \
            octave-optim \
            octave-signal \
            octave-statistics \
            gnuplot \
            ghostscript \
            --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

RUN echo "ja_JP.UTF-8 UTF-8" > /etc/locale.gen \
    && locale-gen \
    && update-locale LANG=ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:en
ENV LC_ALL ja_JP.UTF-8

ADD ./resources/_octaverc /root/.octaverc

WORKDIR /var/octave

CMD ["bash"]

