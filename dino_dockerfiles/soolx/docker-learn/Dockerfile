 FROM node:8.10.0
 ADD . /app/
 WORKDIR /app
 RUN npm install
 RUN npm rebuild node-sass --force
 ENV HOST 0.0.0.0
 ENV PORT 3000
 EXPOSE 3000
 CMD ["npm", "start"]