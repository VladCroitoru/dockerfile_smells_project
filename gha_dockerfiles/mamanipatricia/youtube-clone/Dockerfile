# Stage 1
FROM node:12-alpine AS dev
LABEL stage="intermediate"
WORKDIR /website
COPY . .
RUN yarn
EXPOSE 3000
CMD ["yarn", "start", "--host=0.0.0.0", "--port=3000"]

FROM dev AS builder
LABEL stage="intermediate"
RUN yarn build

# Stage 2 - the production environment
FROM nginx:stable-alpine AS prod
ADD ./nginx /etc/nginx/conf.d/
COPY --from=builder /website/build/ /usr/share/nginx/html/
EXPOSE 80