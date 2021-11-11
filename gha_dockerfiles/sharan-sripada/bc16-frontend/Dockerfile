# FROM node:10-alpine as baseimage

# COPY ["package.json","/."]
# RUN npm install 
# RUN npm install react-scripts@3.0.1 -g
# RUN mkdir /app 
# RUN mv ./node_modules ./app    
# WORKDIR /app 
# COPY . . 
# EXPOSE 8080
# RUN npm run build-prod



# FROM nginx:alpine
# COPY --from=baseimage /app/dist /usr/share/nginx/html
# RUN rm /etc/nginx/conf.d/default.conf
# COPY ./nginx.conf /etc/nginx/conf.d/default.conf
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]


FROM node:10-alpine as builder
COPY package.json  ./
RUN npm install --silent 
RUN npm install react-scripts@3.0.1 -g
RUN mkdir /app && mv ./node_modules ./app
WORKDIR /app
COPY . .
RUN npm run build-dev --silent




FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=builder /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY ./nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]