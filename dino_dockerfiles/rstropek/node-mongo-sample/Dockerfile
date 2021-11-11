FROM node:12 AS build
WORKDIR /app
COPY . .
RUN npm install && npm run build

FROM node:12-alpine
WORKDIR /app/dist
COPY --from=build /app/dist ./
RUN npm install --production
ENV MONGO_URL=mongodb://mongo-server/member-management
ENV port=80
EXPOSE 80
CMD ["node", "./server.js"]
