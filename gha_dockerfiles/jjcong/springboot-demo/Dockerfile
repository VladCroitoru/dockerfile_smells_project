FROM java:8

# 将当前目录中的jar包复制到docker容器中的app.jar包路径
COPY *.jar /app.jar


MAINTAINER jincong<jincong0620@163.com>

# VOLUME 指定了临时文件目录为/tmp。
# 其效果是在主机 /var/lib/docker 目录下创建了一个临时文件，并链接到容器的/tmp
VOLUME /tmp


# 将jar包添加到容器中并更名为app.jar
ADD springboot-0.0.1-SNAPSHOT.jar app.jar

EXPOSE 8080

RUN bash -c 'touch /app.jar'

ENTRYPOINT ["java","-jar","/app.jar"]
