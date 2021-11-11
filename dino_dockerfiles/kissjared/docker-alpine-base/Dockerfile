FROM alpine:latest

MAINTAINER weiboyi lijie1@weiboyi.com

ENV TIMEZONE Asia/Shanghai

# 当使用本地构建时换为国内镜像，以加速docker image制作速度，非中国镜内用户请注释掉下一行
#RUN echo 'http://mirrors.aliyun.com/alpine/latest-stable/main' > /etc/apk/repositories \
    #&& echo 'http://mirrors.aliyun.com/alpine/latest-stable/community' >> /etc/apk/repositories \
    #&& echo 'http://mirrors.aliyun.com/alpine/edge/testing' >> /etc/apk/repositories

#时区配置
RUN apk add --update --no-cache tzdata \
    && ln -snf /usr/share/zoneinfo/$TIMEZONE /etc/localtime \
    && echo $TIMEZONE > /etc/timezone \
    && rm -fr /var/cache/apk/*

# 容器命令执行
CMD ["sh"]
