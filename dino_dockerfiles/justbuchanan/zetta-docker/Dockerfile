FROM justbuchanan/docker-archlinux
MAINTAINER Justin Buchanan <justbuchanan@gmail.com>

RUN pacman -Sy --noconfirm nodejs yarn git
RUN pacman -Scc --noconfirm

RUN mkdir zettajs
WORKDIR zettajs
RUN yarn init -y
RUN yarn add zetta
COPY server.js ./

EXPOSE 3001
CMD ["node", "server"]
