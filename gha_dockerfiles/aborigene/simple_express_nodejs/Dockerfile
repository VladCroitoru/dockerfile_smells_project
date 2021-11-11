FROM i386/node
RUN mkdir /app
COPY myExpress.js /app
COPY package.json /app
COPY package-lock.json /app
WORKDIR /app
RUN npm install
ENTRYPOINT ["node","myExpress.js"]