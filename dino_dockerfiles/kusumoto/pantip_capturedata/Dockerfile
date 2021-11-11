
FROM node:5

COPY . /app/pantip-ws

WORKDIR /app/pantip-ws

RUN npm install

COPY docker-entrypoint.sh /app/pantip-ws/entrypoint.sh

RUN chmod 777 entrypoint.sh

ENTRYPOINT ["/app/pantip-ws/entrypoint.sh"]

EXPOSE 8080

CMD npm start
