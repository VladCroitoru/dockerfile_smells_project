FROM maxc0c0s/cmangos-classic-base

ENV STARTUP_SCRIPTS_DIR=/startup-scripts.d
ENV LOCAL_BIN=/usr/local/bin

RUN useradd -r cmangos

RUN mkdir -p $STARTUP_SCRIPTS_DIR
RUN chown cmangos:cmangos $STARTUP_SCRIPTS_DIR
RUN mkdir -p $LOCAL_BIN/cmangos
RUN chown cmangos:cmangos $LOCAL_BIN/cmangos

USER cmangos

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
