FROM node:14-alpine

# OS deps
RUN apk add --no-cache ffmpeg

# app
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build
CMD ["npm", "start"]