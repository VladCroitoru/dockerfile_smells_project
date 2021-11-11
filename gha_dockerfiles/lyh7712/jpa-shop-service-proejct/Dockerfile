# 베이스 이미지
FROM adoptopenjdk/openjdk11:alpine
# jar 패키지의 위치를 변수로 설정
ARG JAR_FILE=build/libs/*.jar
# jar 패키지를 컨테이너에 복사
COPY ${JAR_FILE} test.jar
# jar를 옵션과 함께 실행
ENTRYPOINT ["java", "-jar", "/test.jar"]