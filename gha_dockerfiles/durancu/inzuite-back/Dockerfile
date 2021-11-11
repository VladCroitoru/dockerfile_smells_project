# Set nginx base image
FROM node:14
LABEL maintainer="Liuver Duran"
WORKDIR  /app
COPY  ./dist ./dist
COPY package.json .
RUN  npm install --production
EXPOSE 5000
CMD ["node", "dist/main"]
