###########################################################
# Dockerfile that builds a DayZ Experimental Server
###########################################################
FROM steamcmd/steamcmd:latest

LABEL maintainer="sludgerick@ycore.net"

ARG STEAMUSERNAME="${STEAMUSERNAME}"
ARG STEAMPASSWORD="${STEAMPASSWORD}"
ARG PROFILEDIR="${HOMEDIR}$/{PROFILEDIR}"
ARG PORT="${PORT}"

ENV STEAMAPPID 1042420
ENV STEAMAPP dayzserver
ENV STEAMUSERNAME "${STEAMUSERNAME}"
ENV STEAMPASSWORD "${STEAMPASSWORD}"
ENV HOMEDIR "${HOME}"
ENV STEAMAPPDIR "${HOMEDIR}/${STEAMAPP}-exp"
ENV PROFILEDIR="${PROFILEDIR}"
ENV PORT="${PORT}"
#ENV DLURL https://raw.githubusercontent.com/sludgerick/dayzexp

# Create autoupdate config
# Add entry script & ESL config
# # Remove packages and tidy up
# RUN set -x \
# 	&& apt-get update \
# 	&& apt-get install -y --no-install-recommends --no-install-suggests \
# 		wget \
# 		ca-certificates \
# 		curl \
# 		libcap2 \
# 		lib32z1=1:1.2.11.dfsg-2ubuntu1.2 \
# 	&& mkdir -p "${STEAMAPPDIR}" \
# 	&& wget --max-redirect=30 "${DLURL}/main/etc/entry.sh" -O "${HOMEDIR}/entry.sh" \
# 	&& echo DEBUG STEAMUSERNAME: "${STEAMUSERNAME}" \
# 	&& echo DEBUG STEAMPASSWORD: "${STEAMPASSWORD}" \
# 	&& chmod +x "${HOMEDIR}/entry.sh" \
# 	&& chown -R "${USER}:${USER}" "${HOMEDIR}/entry.sh" "${STEAMAPPDIR}" \
#  	&& { \
#  		echo '@sSteamCmdForcePlatformType Linux'; \
#  		echo 'login '"${STEAMUSERNAME}"' '"${STEAMPASSWORD}"''; \
#  		echo 'force_install_dir '"${STEAMAPPDIR}"''; \
#  		echo 'app_update '"${STEAMAPPID}"' validate'; \
#  		echo 'quit'; \
#  	   } > "${HOMEDIR}/${STEAMAPP}_update.txt" \
#  	&& chown -R "${USER}:${USER}" "${HOMEDIR}/${STEAMAPP}_update.txt" \
# 	&& rm -rf /var/lib/apt/lists/*

RUN set -x \
	&& apt-get update \
	&& apt-get install -y --no-install-recommends --no-install-suggests \
		ca-certificates \
		curl \
		libcap2 \
		lib32z1=1:1.2.11.dfsg-2ubuntu1.2 \
	&& mkdir -p "${STEAMAPPDIR}" \
	&& mkdir -p "${PROFILEDIR}" \
	&& echo DEBUG STEAMUSERNAME: "${STEAMUSERNAME}" \
	&& echo DEBUG STEAMPASSWORD: "${STEAMPASSWORD}" \
	&& chown -R "${USER}:${USER}" "${PROFILEDIR}" "${STEAMAPPDIR}" \
	&& rm -rf /var/lib/apt/lists/*

# ENV SRCDS_FPSMAX=300 \
# 	SRCDS_TICKRATE=128 \
# 	SRCDS_PORT=27015 \
# 	SRCDS_TV_PORT=27020 \
# 	SRCDS_CLIENT_PORT=27005 \
# 	SRCDS_NET_PUBLIC_ADDRESS="0" \
# 	SRCDS_IP="0" \
# 	SRCDS_MAXPLAYERS=14 \
# 	SRCDS_TOKEN=0 \
# 	SRCDS_RCONPW="changeme" \
# 	SRCDS_PW="changeme" \
# 	SRCDS_STARTMAP="de_dust2" \
# 	SRCDS_REGION=3 \
# 	SRCDS_MAPGROUP="mg_active" \
# 	SRCDS_GAMETYPE=0 \
# 	SRCDS_GAMEMODE=1 \
# 	SRCDS_HOSTNAME="New \"${STEAMAPP}\" Server" \
# 	SRCDS_WORKSHOP_START_MAP=0 \
# 	SRCDS_HOST_WORKSHOP_COLLECTION=0 \
# 	SRCDS_WORKSHOP_AUTHKEY="" \
# 	ADDITIONAL_ARGS=""

ENV PORT=${PORT}

USER ${USER}

VOLUME ${STEAMAPPDIR}
VOLUME ${HOMEDIR}/${PROFILEDIR}

WORKDIR ${HOMEDIR}

COPY etc/entry.sh ${WORKDIR}
RUN chmod +x entry.sh
CMD ["./entry.sh"]

# Expose ports
# EXPOSE 2302:2302 \
#   2303:2303/udp \
#   2304:2304/udp \
#   27016:27016 \
#   36533:36533/tcp

EXPOSE 2302-2304:2302-2304/udp \
  2302:2302/tcp \
  27015-27030:27015-27030/tcp \
  27036-27037:27036-27037/tcp \
  27000-27031:27000-27031/udp \
  36533:36533/tcp

