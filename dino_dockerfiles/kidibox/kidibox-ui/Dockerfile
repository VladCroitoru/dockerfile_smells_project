FROM node:6.9

COPY package.json /app/
WORKDIR /app

# improve npm install speed
RUN npm set progress=false
RUN npm install

ENV PORT 3000
ENV HOST 0.0.0.0
ENV NODE_ENV production

EXPOSE 3000

COPY . /app/
RUN npm run compile

CMD ["npm", "run", "start", "--silent"]
