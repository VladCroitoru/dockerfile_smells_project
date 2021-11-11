FROM node:14-alpine as reactBuild
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY /react/package.json /app/package.json
RUN npm install
RUN npm install axios
COPY ./react /app
RUN npm run build

FROM maven:3.8-jdk-11 AS springBootBuild

ADD ./app ./app
COPY --from=reactbuild /app/build /app/src/main/resources/static
WORKDIR /app

RUN mvn clean install -Dtest=!ImageManagerTest#GIVEN_ValidImage_WHEN_uploadAndInsertImage_THEN_returnImage+

FROM openjdk:11
COPY --from=springBootBuild /app/target/UBMarketplace.jar ./UBMarketplace.jar

#For local test only
#ENV PORT=8080
#ENV MONGODB_URL="mongodb://username:password@123.123.123.123:27017/"

EXPOSE $PORT

CMD java -Xmx512M -Xms400M -XX:+UseG1GC -XX:+AggressiveOpts -XX:+UseCompressedOops -jar UBMarketplace.jar --server.port=$PORT --spring.data.mongodb.uri=$MONGODB_URL