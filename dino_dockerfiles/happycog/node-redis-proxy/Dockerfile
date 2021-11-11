FROM node
RUN mkdir /src

ADD index.js /src/index.js
ADD package.json /src/package.json

RUN cd /src && npm install
EXPOSE 26542

CMD ["node", "/src/index.js"]
