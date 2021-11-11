FROM node:14
WORKDIR /usr/src
COPY . ./
EXPOSE 8000
RUN npm install --platform=linux
RUN rm -rf node_modules/sharp
RUN npm install --arch=x64 --platform=linux sharp
