FROM node:14-alpine As development
 
WORKDIR /app
 
COPY package*.json ./
 
RUN npm install
 
COPY . .
 
RUN npm run build
 
FROM node:14-alpine as production
 
ARG NODE_ENV=production
ENV NODE_ENV=${NODE_ENV}
 
WORKDIR /app
 
COPY package*.json ./

RUN npm ci
 
COPY . .
 
COPY --from=development /app/dist ./dist
 
CMD ["npm", "run", "start"]