FROM node:14-slim
EXPOSE 8000

WORKDIR /app
COPY . ./

RUN npm ci && rm -rf node_modules/

CMD npm ci -s && CONTENT_PATH=/content npx gatsby develop -H 0.0.0.0
