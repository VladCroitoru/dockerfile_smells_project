FROM node:9
COPY . .
RUN npm install
RUN npm run ionic:build -- --prod
#hack becasue the paths are wrong
RUN cp -r www/assets www/build/assets

FROM nginx 
COPY --from=0 www /usr/share/nginx/html
EXPOSE 80