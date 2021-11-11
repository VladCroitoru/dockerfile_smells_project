FROM node:16-alpine

EXPOSE 4500/tcp
RUN mkdir -p /app
WORKDIR /app
ADD ./ /app
RUN npm install
ENV NODE_ENV=production
CMD node /app/app.js