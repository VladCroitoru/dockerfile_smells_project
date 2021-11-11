FROM thalhalla/steamer
MAINTAINER Josh Cox <josh 'at' webhosting coop>

ENV DONTSTARVE_UPDATED 20170111

# override these variables in with the prompts
ENV STEAM_GID 343050

USER root
# and override this file with the command to start your server
COPY assets /assets
RUN chmod 755 /assets/*.sh && \
chmod 755 /assets/steamer.txt && \
chmod 755 /assets/dstserver && \
cp /assets/dstserver /opt/steamer/ && \
chown -R steam. /home/steam && \
chown -R steam. /opt/steamer

USER steam
WORKDIR /home/steam

CMD ["/bin/bash",  "/assets/valve-start.sh"]
