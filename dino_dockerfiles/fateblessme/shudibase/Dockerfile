# 生成基础镜像
FROM openjdk:8u131-jdk-alpine
# 添加基础命令
RUN apk update \
&& apk add --no-cache \
&& apk add curl bash tree tzdata && \
# 设置时区
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
echo "Asia/Shanghai" > /etc/timezone
