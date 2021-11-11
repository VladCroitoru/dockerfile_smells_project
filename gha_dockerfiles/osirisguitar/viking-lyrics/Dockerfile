FROM crisbal/torch-rnn:base

RUN curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
RUN sudo apt-get install build-essential
RUN sudo apt-get install -y --force-yes nodejs

VOLUME /root/torch-rnn/cv

COPY ./lib/ /app/lib/
COPY crawler/lyrics/corpii/viking2.txt /app/lyrics/
COPY package.json /app/
COPY package-lock.json /app/

WORKDIR /app

RUN npm install --production
RUN npm i -g nodemon

EXPOSE 8899

ENV TERM xterm-256color

CMD nodemon lib/index.js