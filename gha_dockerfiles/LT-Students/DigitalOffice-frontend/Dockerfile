FROM node:14-alpine as builder

RUN mkdir /app
WORKDIR /app

COPY package.json package-lock.json ./

RUN npm install

COPY . .

RUN grep -rl "https://84.201.146.123:9817/api" . | xargs sed -i 's#https://84.201.146.123:9817/api#https://auth.ltdo.xyz#g'
RUN grep -rl "http://ltdo.xyz:9818" . | xargs sed -i 's#http://ltdo.xyz:9818#https://auth.ltdo.xyz#g'
RUN grep -rl "http://ltdo.xyz:9804" . | xargs sed -i 's#http://ltdo.xyz:9804#https://project.ltdo.xyz#g'
RUN grep -rl "http://ltdo.xyz:9806" . | xargs sed -i 's#http://ltdo.xyz:9806#https://time.ltdo.xyz#g'
RUN grep -rl "http://ltdo.xyz:9802" . | xargs sed -i 's#http://ltdo.xyz:9802#https://user.ltdo.xyz#g'
RUN grep -rl "http://ltdo.xyz:9816" . | xargs sed -i 's#http://ltdo.xyz:9816#https://company.ltdo.xyz#g'

RUN npm run build --prod --aot --outputHashing=all

FROM nginx:alpine
COPY --from=builder /app/dist/DigitalOffice-frontend /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
