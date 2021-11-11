FROM frolvlad/alpine-oraclejdk8
LABEL author="jianzhichun"
LABEL email="zzchun12826@gmail.com"

WORKDIR /app
COPY backend/target/danmu-analyzer.jar .

EXPOSE 8080

CMD java -jar ./danmu-analyzer.jar