FROM node

SHELL ["/bin/bash", "-c"]

WORKDIR /api

COPY . .

RUN chmod -R 755 .

RUN npm i -g npm

RUN yarn

CMD ./start_script.sh
