FROM quay.io/mocaccino/micro

ENV USER=root
ENV TMPDIR=/tmp
RUN luet install -y repository/mocaccino-extra-stable repository/mocaccino-musl-universe-stable repository/mocaccino-os-commons-stable

RUN rm -rf /var/cache/luet/packages/ /var/cache/luet/repos/

ENTRYPOINT ["/bin/sh"]
