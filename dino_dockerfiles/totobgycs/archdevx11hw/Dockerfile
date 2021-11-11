FROM totobgycs/archdevx11
MAINTAINER totobgycs

ENV TERM xterm
RUN yaourt -Syy ; \
   yaourt -S --aur --noconfirm xterm  ; \
   yes | yaourt -Scc

WORKDIR /home/guiuser
USER guiuser
CMD ["xterm"]

