FROM nodesource/nsolid

WORKDIR /usr/src

COPY . . 

RUN npm install

EXPOSE 3001

CMD ["nsolid", "app/index.js"]