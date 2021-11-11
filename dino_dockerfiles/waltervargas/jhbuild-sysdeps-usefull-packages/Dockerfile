FROM waltervargas/jhbuild:debian
LABEL maintainer "waltervargas@linux.com"

ENV MODULES adwaita-icon-theme dconf glib-networking gvfs libcanberra

RUN $HOME/.local/bin/jhbuild build $MODULES