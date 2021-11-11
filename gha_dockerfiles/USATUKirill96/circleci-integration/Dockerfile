FROM mcr.microsoft.com/playwright:v1.15.0-focal

WORKDIR /usr/src/app

COPY . .

RUN npm install

RUN npx playwright install

CMD ["npx", "playwright", "test"]
