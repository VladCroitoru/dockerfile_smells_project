FROM node

WORKDIR /app

COPY . .

RUN npm ci

ENV PORT 3000

EXPOSE $PORT

CMD ["node", "dist/main.js"]