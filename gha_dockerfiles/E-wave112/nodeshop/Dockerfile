from node:15-alpine3.10 as prod

WORKDIR /app

COPY package*.json ./

RUN npm install

ENV NODE_ENV=production


EXPOSE 3000

COPY  . .

CMD ["npm","run","start" ]


# DEV DOCKERFILE
# from prod as dev

# ENV NODE_ENV=development

# RUN npm install -g nodemon

# RUN npm install --only=dev

# EXPOSE 3000


# CMD ["npm","run","dev"]
