FROM beevelop/ionic:latest
EXPOSE 4200
VOLUME /root/scop
WORKDIR /root/scop

RUN apt update
RUN apt install -y apt-utils curl git gnupg lsof nano software-properties-common unzip wget zsh

RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key C99B11DEB97541F0
RUN apt-add-repository https://cli.github.com/packages
RUN apt update
RUN apt install -y gh

RUN npm i -g npm
RUN npm i -g @angular/cli @nestjs/cli nx ts-node tsconfig-paths typeorm typescript
RUN git clone https://github.com/fabriquebeweb/scop.git /root/scop

RUN git clone -b docker --single-branch https://github.com/fabriquebeweb/scop.git /root/tmp
RUN for file in /root/tmp/.*; do mv $file /root; done
RUN rm -Rf /root/tmp
RUN chsh -s $(which zsh)
