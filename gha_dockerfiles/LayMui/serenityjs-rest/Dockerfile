FROM timbru31/java-node

RUN mkdir /app/
WORKDIR /app
ADD . .

RUN npm install 

CMD [ "npm", "test"]

#RUN yarn report