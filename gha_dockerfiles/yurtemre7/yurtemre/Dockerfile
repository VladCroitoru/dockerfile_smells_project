FROM node
EXPOSE 80
COPY package.json package.json
RUN npm i
COPY . .
RUN npm run build
ENTRYPOINT ["npm","run","start"]
