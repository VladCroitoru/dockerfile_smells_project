FROM node

COPY . .

RUN yarn
ENV PORT=80
ENTRYPOINT [ "node", "main.js" ]

EXPOSE 80