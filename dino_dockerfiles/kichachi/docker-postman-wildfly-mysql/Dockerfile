FROM cjkas/maven-oracle-jdk

RUN useradd -m -g docker docker && echo "docker:docker" | chpasswd && adduser docker sudo

RUN sed -i.bkp -e \
      's/%sudo\s\+ALL=(ALL\(:ALL\)\?)\s\+ALL/%sudo ALL=NOPASSWD:ALL/g' \
      /etc/sudoers

RUN apt-get update

RUN apt-get install -y mysql-server gnupg2 
RUN wget -q https://deb.nodesource.com/setup_6.x && chmod +x setup_6.x && ./setup_6.x
RUN apt-get install -y nodejs build-essential libssl-dev
RUN npm install -g newman

RUN node -v
RUN npm -v
RUN newman -v
RUN rm -fr /var/lib/apt/lists/*

USER docker

WORKDIR /tmp
ADD entrypoint.sh	/tmp/entrypoint.sh
CMD [ "/bin/bash", "/tmp/entrypoint.sh"]