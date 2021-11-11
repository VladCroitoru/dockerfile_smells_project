#> Continuovel - Engine for White Aldus (realtime serial novel)
#? https://github.com/passcod/continuovel
FROM passcod/archlinux
MAINTAINER Félix Saparelli me@passcod.name

RUN pacman -S --noconfirm nodejs;\
  pacman -Scc --noconfirm;\
  rm -rf /var/cache/pacman/pkg/*

ADD . /app
WORKDIR /app
RUN npm install

ENV PORT 80
ENV SOCKET_PORT 42001
EXPOSE 80
CMD ["/usr/bin/npm", "start"]
