FROM totobgycs/archdev
MAINTAINER totobgycs

USER build
WORKDIR /home/build

RUN yaourt -Syy ; \
  yaourt -S --noconfirm --aur jre

RUN yaourt -S --noconfirm unzip; \
  wget https://bitbucket.org/JeanLucPicard/nxt/downloads/nxt-client-1.11.5.zip; \
  unzip nxt-client-1.11.5.zip

WORKDIR /home/build/nxt
VOLUME /home/build/nxt/nxt_db
EXPOSE 7876
ENTRYPOINT ./run.sh
