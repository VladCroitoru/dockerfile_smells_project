# syntax=docker/dockerfile:1


# FROM nginx
# COPY public /usr/share/nginx/html

# docker run -it -v ${pwd}:/root -w=/root --entrypoint /bin/bash ubuntu:latest
# docker run --name referendum-server -d -p 3000:80 referendum-server

FROM node:latest
# ENV NODE_ENV=production
WORKDIR /app
COPY ["package.json", "yarn.lock", "./"]

# RUN npm install --production
RUN yarn install
# COPY . .
# CMD yarn dev

CMD /bin/bash

# build image
# docker build --tag referendum-server-base .

# run image in dev mode (powershell)
# 
# docker run -dp 3000:3000 `
#   --name server `
#   -w /app -v "$(pwd):/app" `
#   --network referendum `
#   -e MYSQL_HOST=mysql `
#   -e MYSQL_USER=root `
#   -e MYSQL_PASSWORD=secret `
#   -e MYSQL_DB=referendum `
#   node:latest `
#   sh -c "yarn run dev"

# log
# docker logs -f <container-id>

# docker container prune


# docker network create referendum

# run db container
#
# docker run -d `
#      --name mysql `
#      --network referendum --network-alias mysql `
#      -v referendum-mysql-data:/var/lib/mysql `
#      -e MYSQL_ROOT_PASSWORD=secret `
#      -e MYSQL_DATABASE=referendum `
#      mysql:latest

# execute in docker shell
#
# docker exec -it <mysql-container-id> mysql -u root -p

# docker run -it --network referendum nicolaka/netshoot