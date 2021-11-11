FROM node:12.0-slim
COPY . .
RUN npm install
CMD [ "node", "gateway.js" ]

# docker build -t gateway .
# docker run --env-file ./.env -p 80:80 gateway