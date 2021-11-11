FROM node:4.2.4

WORKDIR /usr/src/app

COPY package.json /usr/src/app/
RUN npm install > /dev/null

COPY . /usr/src/app/

EXPOSE 3000

ENTRYPOINT ["npm"]
CMD ["start"]
