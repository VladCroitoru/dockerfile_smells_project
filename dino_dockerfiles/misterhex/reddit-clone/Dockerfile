FROM openjdk:8
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs
WORKDIR /root
ADD backend backend
ADD frontend frontend
WORKDIR /root/frontend
RUN npm install
RUN export NODE_ENV=production && npm run build
WORKDIR /root
RUN mkdir -p ./backend/src/main/resources/public/
RUN mv ./frontend/dist/* ./backend/src/main/resources/public/
WORKDIR /root/backend
RUN sed -i 's/\r//' ./mvnw
RUN chmod +x ./mvnw
RUN ./mvnw package
EXPOSE 8080
CMD ["java","-jar","target/reddit-clone-0.0.1-SNAPSHOT.jar"]
