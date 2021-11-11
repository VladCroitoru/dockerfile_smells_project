FROM node:14.17-alpine
WORKDIR /usr/src/knipper
COPY . .
RUN npm install --production
RUN npm run build
EXPOSE 3000
CMD ["npm", "run" ,"start" ]
