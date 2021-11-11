FROM alpine
MAINTAINER  Westerus <westerus@gmail.com>
LABEL Description="Run envsubst environment variables" \
      Version="0.1.0"

ARG PKG_FLAGS_COMMON="-S"
ARG PKG_FLAGS_PERSISTANT="${PKG_FLAGS_COMMON} --noconfirm --force"
ARG PKG_FLAGS_DEV="${PKG_FLAGS_COMMON} --debug"
ARG PKGUPDATE="yaourt ${PKG_FLAGS_COMMON} -y"
ARG PKGUPGRADE="yaourt ${PKG_FLAGS_PERSISTANT} -y -u -q --aur"
ARG PKGCLEAN="yaourt ${PKG_FLAGS_PERSISTANT} -cc"
ARG DELTEMP="rm -rf /var/tmp/* /tmp/*"
ARG PKGINSTALL="yaourt ${PKG_FLAGS_PERSISTANT}"
ARG PKGREMOVE="yaourt -R -q --force --noconfirm"
ARG TERM="xterm"

COPY /rootfs/entry-point.sh /

RUN $PKGUPDATE \
  && $PKGUPGRADE \
  && $PKGINSTALL ca-certificates mutt \
  && $DELTEMP

ENTRYPOINT ["/entry-point.sh"]
CMD ["mutt", "-h"]
