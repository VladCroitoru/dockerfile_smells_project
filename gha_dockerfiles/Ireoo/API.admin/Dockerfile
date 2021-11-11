FROM node
RUN mkdir -p /app
WORKDIR /app

ENV PORT=80

COPY . /app

RUN npm install
RUN npm run build

EXPOSE 80

CMD ["npm", "start"]
