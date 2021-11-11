FROM openjdk:8 as builder

#RUN curl -sL https://deb.nodesource.com/setup_12.x | bash - \
#    && curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \
#    && echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list \
#    && apt-get update && apt-get install -y nodejs yarn \
#    && node -v && npm -v && yarn -v

WORKDIR /vrap
COPY . /vrap

RUN ./gradlew clean shadowJar

FROM openjdk:8-jre-alpine

WORKDIR /app

COPY --from=builder /vrap/build/libs/vrap-all.jar /app/vrap.jar
ADD vrap.sh /app/vrap.sh

ENV JAVA_OPTS  ""
EXPOSE 5050
EXPOSE 5005
ENTRYPOINT ["./vrap.sh"]
