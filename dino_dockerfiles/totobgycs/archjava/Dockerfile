FROM totobgycs/archdevx11
MAINTAINER totobgycs

ENV TERM xterm
RUN yaourt -Syy ; \
   yaourt -S --aur --noconfirm jdk  ; \
   yaourt -S --noconfirm eclipse-java maven ; \
   yes | yaourt -Scc

WORKDIR /home/guiuser
USER guiuser
RUN  mkdir workspace
VOLUME /home/guiuser/workspace
CMD ["eclipse"]

