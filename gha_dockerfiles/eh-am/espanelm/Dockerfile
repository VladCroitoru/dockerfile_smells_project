FROM node:latest AS builder
WORKDIR /app
COPY . /app
RUN npm install && npm run build


FROM node:alpine
RUN apk add --update python3 py-pip jq curl
RUN pip install awscli

WORKDIR /app
COPY docker-entrypoint.sh /app
RUN chmod +x docker-entrypoint.sh
COPY --from=builder /app/dist /app
COPY --from=builder /app/node_modules /app/node_modules

ENTRYPOINT ["sh", "docker-entrypoint.sh"]
