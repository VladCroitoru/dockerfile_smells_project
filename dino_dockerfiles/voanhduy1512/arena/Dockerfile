FROM node:8.1.2

EXPOSE 4567

RUN mkdir -p /opt/arena
WORKDIR /opt/arena
COPY package.json /opt/arena
COPY yarn.lock /opt/arena
RUN yarn --production

COPY . /opt/arena/

CMD ["yarn", "start"]

RUN chmod -R 775 /opt/arena/
RUN chgrp -R 0 /opt/arena/ 
