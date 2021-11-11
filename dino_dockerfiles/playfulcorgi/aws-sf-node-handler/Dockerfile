FROM node:8.7
WORKDIR /logic
COPY * ./
COPY source ./source
COPY app /app
RUN npm install
RUN npm run build
ENTRYPOINT npm run start