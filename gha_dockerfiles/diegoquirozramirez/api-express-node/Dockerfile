FROM node:12.14.1-alpine

# create destination directory
USER root
RUN mkdir -p /usr/src/ms-mdp-js
WORKDIR /usr/src/ms-mdp-js

# copy and archivos
COPY . /usr/src/ms-mdp-js

# instalar las dependencias
RUN npm install

# instalar nodemon o pm2 
RUN npm install nodemon -g

#expone el puerto
EXPOSE 3000

# comando para levantar microservicio
CMD ["nodemon", "src/app.js"]