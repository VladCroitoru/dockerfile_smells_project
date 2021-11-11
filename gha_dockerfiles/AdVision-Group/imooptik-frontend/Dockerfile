FROM node:14 as BUILDER

WORKDIR /app

COPY package.json .
RUN npm install

ADD . .

RUN npm run build

# EXPOSE 3000
# CMD ["npm", "start"]

FROM nginx:stable-alpine

WORKDIR /app

COPY --from=BUILDER /app/build /usr/share/nginx/html
# VOLUME [ "/build" ]

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]