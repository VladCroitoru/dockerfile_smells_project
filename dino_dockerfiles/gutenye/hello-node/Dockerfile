FROM gutenye/node

COPY package.json /app
RUN npm install
COPY . /app

EXPOSE 80
CMD ["node", "app.js"]
