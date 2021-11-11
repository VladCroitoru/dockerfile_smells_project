FROM openjdk:11-jdk
WORKDIR /khumu
COPY . .
RUN ./gradlew build  --exclude-task test --exclude-task testClasses

# jar에는 빌드 시의 resources가 포함될 수 있지만
# 우리는 실행 시 외부에서 properties나 resource를 주입시켜줄 것임.
# 오픈소스로 프로젝트를 관리하기 때문에 빌드 시 credential을 jar에 넣을 수 없음.
# 그 외부 주입 경로는 build/resources/main/
RUN cp -r src/main/resources/* build/resources/main
RUN mv build/libs/*.jar build/libs/alimi.jar

ENTRYPOINT ["java", "-Dspring.profiles.active=dev", "-jar", "build/libs/alimi.jar", "--spring.config.location=build/resources/main/"]

