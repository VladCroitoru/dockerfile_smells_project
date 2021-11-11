FROM openjdk:8-jre-buster
WORKDIR /bot_src
ARG BUILD_NBR
ARG BRANCH_NAME
ARG BRANCH_NAME
ARG GITHUB_RUN_NUMBER
ADD build/libs/ClaptrapBot-*.jar /bot_src/bot.jar
RUN java -version
ENV PORT=8080
ENV TOKEN=10
CMD java -jar bot.jar -t ${TOKEN}
LABEL org.opencontainers.image.source=https://github.com/Sebclem/ClaptrapBot/