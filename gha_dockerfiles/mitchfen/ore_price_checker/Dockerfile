# Build environment
FROM node:alpine as build
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY . .
RUN npm install && npm run build

# Execution environment
FROM node:alpine
WORKDIR /app
COPY --from=build /app/build /app/build
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json .
RUN npm install -g npm@latest && npm install --production
ENTRYPOINT ["npm", "run", "check"]
CMD ["jita"]
