FROM ubuntu:latest

# 构建时元数据，定义于 http://label-schema.org
ARG BUILD_DATE
ARG VCS_REF
ARG VERSION
LABEL maintainer="moore@moorehy.com" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.name="Ubuntu-VPS" \
      org.label-schema.description="容器化的虚拟专用服务器" \
      org.label-schema.url="https://hub.docker.com/r/littlemo/ubuntu-vps/" \
      org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/littlemo/ubuntu-vps" \
      org.label-schema.vendor="https://www.moorehy.com" \
      org.label-schema.version=$VERSION \
      org.label-schema.schema-version="1.0"

# 替换为中科大软件源
RUN sed -i 's|archive.ubuntu.com|mirrors.ustc.edu.cn|g' /etc/apt/sources.list && \
    sed -i 's|security.ubuntu.com|mirrors.ustc.edu.cn|g' /etc/apt/sources.list

# 安装软件&扩展
RUN apt-get update --fix-missing && apt-get install -y \
        openssh-server landscape-common sudo \
        --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# 配置SSHD
RUN mkdir /var/run/sshd \
    && sed -ri 's|#?PasswordAuthentication yes|PasswordAuthentication no|g' \
        /etc/ssh/sshd_config

# 配置用户
RUN echo 'root:whosyourdaddy' | chpasswd \
    && adduser --disabled-password --gecos "" --quiet dev \
    && echo 'dev:dev' | chpasswd

# 配置用户组，以及sudo组无需输入密码
RUN sed -ri 's|%sudo\tALL=\(ALL:ALL\) ALL|%sudo\tALL=\(ALL:ALL\) NOPASSWD: ALL|g' \
        /etc/sudoers \
    && usermod -aG adm,sudo dev

# 设置工作路径
WORKDIR /root

# 设置开放端口
EXPOSE 22

# 启动命令
CMD [ \
    "/usr/sbin/sshd", "-D" \
]
