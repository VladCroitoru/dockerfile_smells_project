FROM tomcat:8.0.20-jre8
#FROM 826846563965.dkr.ecr.ap-northeast-2.amazonaws.com/base/tomcat-redis-session:8.5.37-jre8-alpine
# Tomcat and Java Vars
ENV TIME_ZONE=Asia/Seoul
# TimeZone Settings
RUN ln -snf /usr/share/zoneinfo/$TIME_ZONE /etc/localtime && echo $TIME_ZONE > /etc/timezone
COPY ./webapp/ /usr/local/tomcat/webapps/ROOT/