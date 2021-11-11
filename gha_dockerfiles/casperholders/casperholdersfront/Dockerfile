FROM node:lts as build-stage
ARG mode
WORKDIR /app
COPY package*.json ./
RUN yarn install
COPY ./ .
RUN yarn build-${mode}

FROM nginx as production-stage
RUN mkdir /app
COPY --from=build-stage /app/dist /app
COPY nginx.conf /etc/nginx/nginx.conf