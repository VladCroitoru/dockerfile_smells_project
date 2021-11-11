FROM node
FROM mcr.microsoft.com/playwright:focal

WORKDIR /app

COPY package-lock.json /app
COPY package.json /app

RUN npm ci

RUN npx playwright install

COPY . .

CMD ["npm", "test"]

