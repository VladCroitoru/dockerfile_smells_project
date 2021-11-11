### 1. Get Linux
FROM alpine:latest

### 2. Get Java via the package manager
RUN apk update \
&& apk upgrade \
&& apk add --no-cache bash \
&& apk add --no-cache --virtual=build-dependencies unzip \
&& apk add --no-cache curl \
&& apk add --no-cache openjdk8-jre

### 3. Get Python, PIP

RUN apk add --no-cache python3 \
&& python3 -m ensurepip \
&& pip3 install --upgrade pip setuptools \
&& rm -r /usr/lib/python*/ensurepip && \
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
rm -r /root/.cache

### Get Flask for the app
RUN pip install --trusted-host pypi.python.org flask

####
#### OPTIONAL : 4. SET JAVA_HOME environment variable, uncomment the line below if you need it

#ENV JAVA_HOME="/usr/lib/jvm/java-1.8-openjdk"

####
EXPOSE 8081
ENV TZ=PRC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ADD xxl-job-admin-*.jar /app.jar
ADD xxl-job-executor-sample*.jar /app2.jar
ADD tables_xxl_job.sql /init.sql

#ENTRYPOINT ["sh","-c","java -jar /app.jar"]
#CMD nohup java -jar /app.jar &
#ENTRYPOINT ["java","-jar","/app2.jar"]
ADD start.sh /start.sh
# 赋予文件权限并运行start.sh脚本
RUN chmod +x start.sh
ENTRYPOINT ["sh","/start.sh"]

