FROM node:10
WORKDIR /app
COPY package.json package.json
COPY package-lock.json package-lock.json
COPY src src
COPY font.woff.enc font.woff.enc
RUN npm install --only=production
EXPOSE 80
CMD ["npm", "run", "decrypt-start"]
