FROM justbuchanan/docker-archlinux
MAINTAINER Justin Buchanan <justbuchanan@gmail.com>

# install required packages
RUN pacman -S --noconfirm nodejs npm
RUN npm install -g gulp
RUN pacman -S --noconfirm git

# setup zetta-browser from github repo
RUN git clone git://github.com/zettajs/zetta-browser
WORKDIR zetta-browser
RUN npm install

# run server on port 3001
EXPOSE 3001
ENV PORT 3001
CMD ["gulp"]

