FROM node

COPY package.json .
COPY yarn.lock .
RUN yarn install

COPY . .

EXPOSE 8080
CMD ["npm", "start"]
