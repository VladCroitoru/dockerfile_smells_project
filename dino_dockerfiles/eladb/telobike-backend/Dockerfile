FROM node
COPY package.json /opt/telobike/
WORKDIR /opt/telobike
RUN npm install
EXPOSE 5000

COPY . /opt/telobike
ENTRYPOINT npm start
