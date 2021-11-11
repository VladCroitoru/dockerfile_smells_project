FROM ubuntu:20.04
ENV PIXIV_DOMAIN="pixiv.creeper2077.online" PXIMG_DOMAIN="pximg.creeper2077.online"  PORT=8080 BLOCK_IP=1
ARG ARCHIVE_SOURCE='default' SECURITY_SOURCE='default'
RUN echo -e "\033[33m Pixiv Proxy\n \033[0m" \
    && echo -e "\033[36m Github: https://github.com/Creeper2077/pixiv-proxy \033[0m" \
    && echo -e "\033[33m Please abide by the use agreement of relevant service providers !\033[0m" \
    && echo -e "\n===============================\n" \
    && echo "Start building image." \
    && echo "Update source..." \
    && if [ ${ARCHIVE_SOURCE} != 'default' ]; then sed -i "s/archive.ubuntu.com/${ARCHIVE_SOURCE}/g" /etc/apt/sources.list; fi \
    && if [ ${SECURITY_SOURCE} != 'default' ]; then sed -i "s/security.ubuntu.com/${SECURITY_SOURCE}/g" /etc/apt/sources.list; fi \
    && apt update -qq > /dev/null \
    && apt upgrade -y -qq > /dev/null \
    && echo "Done." \
    && echo "Install Nginx" \
    && apt install curl nginx libnginx-mod-http-subs-filter -y -qq --no-install-recommends > /dev/null \
    && echo "Done." \
    && echo "Add user www..." \
    && groupadd -r www \
    && useradd -r -g www www \
    && echo "Done." \
COPY ./*.conf /home
COPY ./scripts/*.sh /home/scripts
RUN echo "Run final processing..." \
    && chmod -R +x /home/scripts \
    && apt clean -qq > /dev/null \
    && apt autoremove -qq > /dev/null \
    && echo "done." \
    && echo -e "\033[36m All DOne! \033[0m"
CMD [ "/home/scripts/init.sh /home" ]