FROM debian:stretch

MAINTAINER davask <admin@davask.com>
USER root
# Update packages
RUN apt-get update && \
apt-get install -y apt-utils locales
RUN sed -i 's|#  UTF-8| UTF-8|g' /etc/locale.gen && \
locale-gen ""
# declare locales
ENV DWL_LOCAL_LANG ${CONF_LOCAL_LANG}
ENV DWL_LOCAL ${CONF_LOCAL}
ENV LANG ${CONF_LOCAL}
ENV LANGUAGE ${CONF_LOCAL_LANG}
# ENV LC_ALL ${CONF_LOCAL}

# declare main user
ENV DWL_USER_ID ${CONF_USER_ID}
ENV DWL_USER_NAME ${CONF_USER_NAME}
ENV DWL_USER_PASSWD ${CONF_USER_PASSWD}
# declare main user
ENV DWL_SSH_ACCESS ${CONF_SSH_ACCESS}

RUN apt update && \
apt install -y \
openssl \
ca-certificates \
apt-transport-https \
software-properties-common \
openssh-server \
nano \
wget \
sudo

RUN apt-get upgrade -y && \
apt-get autoremove -y && \
apt-get clean && \
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN useradd -r \
--comment "dwl ssh user" \
--no-create-home \
--shell /bin/bash \
--uid 999 \
--no-user-group \
admin;
RUN echo "admin ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/admin
RUN chmod 0440 /etc/sudoers.d/admin

#configuration static
COPY ./build/etc/ssh/sshd_config \
./build/etc/ssh/sshd_config.factory-defaults \
/etc/ssh/

COPY ./build/dwl/envvar.sh \
./build/dwl/user.sh \
./build/dwl/ssh.sh \
./build/dwl/permission.sh \
./build/dwl/custom.sh \
./build/dwl/init.sh \
/dwl/

EXPOSE 22

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["/bin/bash /dwl/init.sh"]
WORKDIR /home/admin
RUN chmod +x /dwl/init.sh && chown root:sudo -R /dwl
USER admin
