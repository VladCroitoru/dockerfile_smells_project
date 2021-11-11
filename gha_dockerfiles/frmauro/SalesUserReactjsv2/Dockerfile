# Imagem de Origem
# pull official base image
FROM node:13.12.0-alpine as build

# set working directory
WORKDIR /app

# add `/app/node_modules/.bin` to $PATH
ENV PATH /app/node_modules/.bin:$PATH

# install app dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install 
RUN npm install react-scripts@3.4.3 -g 

# add app
COPY . ./
RUN npm run build

# start app
# CMD ["npm", "start"]

# production environment
FROM nginx:1.13
COPY --from=build /app/build/ /usr/share/nginx/html
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 3000
ENTRYPOINT ["nginx","-g","daemon off;"]
#CMD [“nginx”, “-g”, “daemon off;”]