FROM mysql:5.7.12

RUN useradd -r restorer

USER restorer

COPY entrypoint.sh /tmp

ENTRYPOINT ["/tmp/entrypoint.sh"]
