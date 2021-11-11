FROM node:0.10

ENV user node
RUN groupadd --system $user && useradd --system --create-home --gid $user $user

RUN \
  apt-get update && \
  apt-get install -y ruby ruby-dev nasm && \
  rm -rf /var/lib/apt/lists/*

RUN gem install compass

# COPY . /home/$user/
WORKDIR /home/$user
RUN git init
RUN git remote add origin https://github.com/dgoradia/tiktok
RUN git fetch
RUN git checkout -t origin/master
RUN chown $user --recursive .

RUN npm install -g bower grunt-cli

USER $user
RUN npm install

EXPOSE 8080
CMD ["npm", "start"]
