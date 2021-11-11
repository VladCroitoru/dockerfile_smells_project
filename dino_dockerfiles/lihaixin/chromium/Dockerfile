FROM lihaixin/novnc
MAINTAINER Haixin Lee <docker@lihaixin.name>

#加载flash仓库源
RUN echo "deb http://archive.canonical.com/ubuntu/ xenial partner" >> /etc/apt/sources.list

#升级系统，安装chromium和flash多媒体插件
RUN apt-get update -y && \
 apt-get install  -y --no-install-recommends adobe-flashplugin chromium-browser chromium-browser-l10n chromium-codecs-ffmpeg


# 升级到最新版本
RUN apt-get upgrade --yes

# 删除不必要的软件和Apt缓存包列表
RUN apt-get -y autoclean && \
    apt-get -y autoremove && \
    rm -rf /var/lib/apt/lists/*

# 容器里超级进程管理
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# 开放VNC端口和noVNC端口
#EXPOSE 5900 
EXPOSE 8787
VOLUME /root/Downloads



# 运行各种Service

CMD ["/usr/bin/supervisord"]
