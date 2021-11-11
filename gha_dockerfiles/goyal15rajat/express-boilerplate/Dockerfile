

FROM mhart/alpine-node:16 as base
ARG ENV
WORKDIR /app
COPY package*.json ./
RUN if [ "$ENV" = "prod" ] || [ "$ENV" = "PROD" ] || [ "$ENV" = "PRODUCTION" ] || [ "$ENV" = "production" ]; \
	then npm ci --prod; \
	else npm i; \
	fi
FROM mhart/alpine-node:16
WORKDIR /app
COPY --from=base /app /app
COPY . .
RUN chmod +x ./start.sh
