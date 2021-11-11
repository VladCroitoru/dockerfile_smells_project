FROM node:latest
WORKDIR /dspfront
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build
EXPOSE 5001
CMD ["npm", "run", "serve", "--", "--port", "5001", "--host", "dspfront"]
