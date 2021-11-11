FROM flexconstructor/docker-container-monitor
MAINTAINER flexconstructor@gmail.com

# -------- Sets environment variables. -------

ENV WOWZA_VERSION=4.3.0           \
    WOWZA_DATA_DIR=/var/lib/wowza \
    WOWZA_LOG_DIR=/var/log/wowza

# -------- Install dependencies. -------------
RUN yum update -y \
 && yum install -y wget openjdk-7-jre expect tar

# -------- Copy and run prepare script. ------
COPY prepare.sh interaction.exp /app/
RUN /app/prepare.sh

# ---- Copy and run entrypoint script. -------
COPY entrypoint.sh /sbin/entrypoint.sh
RUN chmod 755 /sbin/entrypoint.sh

# ---------- Expose ports. -------------------
EXPOSE 1935/tcp 8086/tcp 8087/tcp 8088/tcp

# ---------- Sets data volumes. --------------
VOLUME ["${WOWZA_DATA_DIR}", "${WOWZA_LOG_DIR}"]

# ----------- Sets entrypoint. ---------------
ENTRYPOINT ["/sbin/entrypoint.sh"]
