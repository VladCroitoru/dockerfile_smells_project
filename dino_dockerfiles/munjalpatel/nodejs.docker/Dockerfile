FROM google/nodejs

RUN echo "alias ls='ls --color=auto'" >> /root/.bashrc
RUN echo "alias ll='ls --color=auto -l'" >> /root/.bashrc
RUN echo "alias l='ls --color=auto -lA'" >> /root/.bashrc
RUN echo "alias c='clear'" >> /root/.bashrc
  
RUN npm install -g express nodemon

ONBUILD ADD ./src /app
ONBUILD WORKDIR /app
ONBUILD RUN npm install
ONBUILD CMD node server.js

EXPOSE 4000
