FROM node

WORKDIR /opt/docker_files/nestjs_cors

RUN /bin/sh -c "apt-get install bash"

COPY package*.json ./
RUN npm install -g npm && npm install
RUN npm i -g @nestjs/cli

COPY . .

EXPOSE 3000

CMD ["npm", "start"]