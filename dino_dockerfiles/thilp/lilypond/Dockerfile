FROM opensuse

ENV LILYPOND_SCRIPT=lilypond-2.19.65-1.linux-64.sh
ENV LILYPOND_URL=http://download.linuxaudio.org/lilypond/binaries/linux-64/$LILYPOND_SCRIPT

RUN zypper -n install curl tar \
    && zypper -n clean \
    && curl -Lo $LILYPOND_SCRIPT $LILYPOND_URL \
    && chmod +x $LILYPOND_SCRIPT

RUN ./$LILYPOND_SCRIPT

WORKDIR /root

CMD ["/usr/local/bin/lilypond"]