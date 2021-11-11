FROM node:5
ADD ./docker-npm-install.sh /docker-npm-install.sh

ADD ./sources.list /etc/apt/sources.list

RUN git clone https://github.com/wikimedia/parsoid && cd parsoid && git checkout v0.5.2 && rm -Rf .git/

WORKDIR parsoid

RUN /docker-npm-install.sh

EXPOSE 8000

ADD ./kickstart.sh /
RUN chmod +x /kickstart.sh
CMD /kickstart.sh
