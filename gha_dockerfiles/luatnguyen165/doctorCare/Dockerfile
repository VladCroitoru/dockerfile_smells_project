FROM node:13-alpine

WORKDIR /app

COPY . .

EXPOSE 3000

RUN yarn install

# Development
CMD ["npm",'yarn', "start",'dev']


# # Production
# RUN npm install -g pm2
# CMD ["pm2-runtime", "ecosystem.config.js", "--env", "production"]