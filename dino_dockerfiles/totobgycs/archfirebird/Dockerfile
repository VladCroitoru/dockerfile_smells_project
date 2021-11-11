FROM totobgycs/archdev
MAINTAINER totobgycs

USER build
ENV TERM xterm
ENV VISUAL nano
RUN yaourt -S --noconfirm icu libedit ; \
  yaourt -S --aur --noconfirm firebird-superserver; \
  yes | yaourt -Scc
USER root
RUN  rm -r /usr/share/doc/firebird /etc/firebird/firebird.conf ;\
  mkdir /tmp/firebird ;\
  mkdir /database ;\
  echo "DatabaseAccess=Restrict /database" >> /etc/firebird/firebird.conf ;\
  echo "TempDirectories = /tmp/firebird" >> /etc/firebird/firebird.conf
VOLUME ["/database", "/tmp/firebird"]
EXPOSE 3050/tcp
ENTRYPOINT /usr/lib/firebird/bin/fbguard
