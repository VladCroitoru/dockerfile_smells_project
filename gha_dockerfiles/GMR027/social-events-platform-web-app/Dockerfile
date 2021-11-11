FROM node:14-alpine

ENV REACT_APP_API_URL={REACT_APP_API_URL}

WORKDIR /app
COPY . . 

RUN npm i --production
RUN ls
RUN /bin/sh server/prepare-index.sh

CMD ["node", "server/app.js"]
