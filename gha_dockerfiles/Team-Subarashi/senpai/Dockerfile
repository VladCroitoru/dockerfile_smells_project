# Stage 0 - Build frontend
FROM node:14.17.0 as Build


WORKDIR /app

COPY package*.json ./
RUN npm install
COPY . .

ENV NODE_OPTIONS=--max_old_space_size=4000
RUN npm run build

CMD ["npm", "run", "start"]