FROM centos:7

RUN yum install -y which git curl wget bzip2

# Install Node
RUN   \
  wget -O - https://nodejs.org/dist/v6.9.4/node-v6.9.4-linux-x64.tar.gz \
  | tar xzf - --strip-components=1 --exclude="README.md" --exclude="LICENSE" \
  --exclude="ChangeLog" -C "/usr/local"

VOLUME ["/src"]

RUN useradd -ms /bin/bash node
RUN chown -R node:node /src /opt /usr
ENV HOME /home/node

USER node

WORKDIR   /src

RUN npm i -g  yo bower grunt-cli gulp

CMD /bin/bash

