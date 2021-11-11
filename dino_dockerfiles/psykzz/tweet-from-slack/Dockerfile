FROM node

COPY app /var/app
COPY Procfile /var/app

WORKDIR /var/app
RUN npm install

EXPOSE 3000

CMD node /var/app/app.js