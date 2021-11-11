FROM node:15

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY ./ ./

RUN npx prisma generate

RUN npm run build

# RUN mv prisma build/
# COPY .env ./build/

ENV PORT=5000

EXPOSE ${PORT}

CMD node build/server.js