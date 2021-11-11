FROM node:16.4.2-alpine3.12
LABEL maintainer "Nathan Murillo <nathanmurillodeoliveira@gmail.com>"
WORKDIR /usr/app
COPY . ./
RUN npm i
RUN npm run build
CMD ["npm", "run", "start"]