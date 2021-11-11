FROM azul/zulu-openjdk:14
RUN apt-get update && apt-get install -y curl \
  && curl -sL https://deb.nodesource.com/setup_14.x | bash - \
  && apt-get install -y nodejs \
  && curl -L https://www.npmjs.com/install.sh | sh

WORKDIR /usr/src/app

COPY . .

RUN cd frontend && npm install
RUN cd frontend && npm run build
RUN cd backend && chmod +x gradlew
RUN cd backend && ./gradlew stage

EXPOSE 4567
CMD ["java", "-cp", "/usr/src/app/backend/build/libs/devops-all.jar", "ch.zhaw.iwi.devops.Main"]
