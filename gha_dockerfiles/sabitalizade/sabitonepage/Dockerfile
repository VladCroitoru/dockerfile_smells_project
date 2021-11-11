FROM node:14-alpine 

WORKDIR /
COPY . .

# RUN npm install
RUN npm i
RUN npm run build
RUN npm install -g serve


CMD serve -s -l 3000 build/