# build environment
FROM node:12.2.0-alpine as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app/package.json
RUN npm install --only=production
RUN npm install react-scripts@3.0.1 -g --only=production
RUN ls -a


#introduced
#FROM node:12.2.0-alpine as build2
FROM build as build2
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
#COPY --from=build /app/node_modules/.bin /app/node_modules/.bin
#original
#COPY --from=build /app/package.json /app/package.json
#COPY --from=build /app/package-lock.json /app/package-lock.json
#COPY --from=build /app/node_modules/react-scripts /app/node_modules/eact-scripts
COPY . /app
#COPY --from=build /app/node_modules /app/node_modules
RUN npm run build

# production environment
FROM nginx:1.16.0-alpine
COPY --from=build2 /app/build /usr/share/nginx/html
RUN cat /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d/nginx.conf
EXPOSE 80
#EXPOSE 443
CMD ["nginx", "-g", "daemon off;"]