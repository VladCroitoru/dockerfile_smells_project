# FROM direpos.capitalonline.net/cdsops-alpine:base
FROM xujpxm/alpine-ops:latest

MAINTAINER xujpxm

ENV ENV_CONFIG production
#创建代码目录
RUN mkdir -p /data/v_charge\
    && apk add --no-cache  py-mysqldb redis
#上传代码和nginx+supervisor服务的配置文件
ADD . /data/v_charge
ADD conf/nginx_example.conf /etc/nginx/conf.d/
ADD conf/supervisor_example.ini /etc/supervisor.d/

EXPOSE 80

#安装代码运行依赖包
WORKDIR /data/v_charge/
# 额外安装tzdata，配置tiemzone为中国
RUN  pip install --no-cache-dir -r requirements.txt

# 启动supervisor，配置文件里包含nginx和gunicorn,相当于同时启动两个服务
CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]