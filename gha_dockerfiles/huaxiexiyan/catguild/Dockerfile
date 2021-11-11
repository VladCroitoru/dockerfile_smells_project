# 一阶段编译打包
FROM openjdk:11-jdk-slim AS build-env
COPY ./gradle/wrapper /app/gradle/wrapper
COPY ./*gradle* /app
WORKDIR /app
RUN chmod +x ./gradlew
RUN ./gradlew dependencies -i --stacktrace
COPY ./src/main /app/src/main
RUN ./gradlew clean build -x test -i --stacktrace

# 构建运行环境
FROM gcr.io/distroless/java:11
COPY --from=build-env /app/build/libs/catguild-1.0-SNAPSHOT.jar /app/main.jar
WORKDIR /app
EXPOSE 20000
CMD ["main.jar","--spring.config.location=application.yml"]
