FROM mcr.microsoft.com/playwright:focal

WORKDIR /app

COPY package.json package-lock.json ./
COPY src/ ./src
RUN mkdir -p ./docs
RUN npm ci --ignore-scripts
