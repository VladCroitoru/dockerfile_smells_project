FROM node:8
LABEL maintainer "William Hilton <wmhilton@gmail.com>"
WORKDIR /srv
COPY . .
RUN npm install -g serve
EXPOSE 80
CMD PORT=80 serve

