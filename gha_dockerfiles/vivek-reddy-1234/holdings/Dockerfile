# Step 1 ->

FROM node:16.6-alpine as build-step
RUN mkdir /app
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /app
RUN npm install
COPY . /app
RUN npm run build

# Stage 2 ->

FROM nginx:1.17.1-alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=build-step /app/build /usr/share/nginx/wealthapp