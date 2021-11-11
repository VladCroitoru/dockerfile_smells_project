# Download base image Linux CentOS
FROM centos
LABEL maintainer "Lukas Maly <Iam@LukasMaly.NET>"

# Define the ENV variable
ENV TECO_CONF_DIR /etc/teco
ENV TECO_CONF_FILE PLCComS.ini
ENV TECO_LOG_DIR /var/log/teco
ENV TECO_LOG_FILE PLCComS.log
ENV TECO_DIR /opt/teco
ENV TECO_LIB_DIR /opt/teco/lib_x86_64

# Create directory
RUN mkdir -p ${TECO_CONF_DIR}
RUN mkdir -p ${TECO_LOG_DIR}
RUN mkdir -p ${TECO_DIR}
RUN mkdir -p ${TECO_LIB_DIR}

# Export shell variables
RUN export MALLOC_CHECK_=4
RUN export LD_LIBRARY_PATH=$TECO_LIB_DIR

# Copy binary file
COPY PLCComS_x86_64 ${TECO_DIR}
RUN chmod 700 ${TECO_DIR}/PLCComS_x86_64

# Copy lib file
COPY lib_x86_64/libcrypto.so.1.0.0 ${TECO_LIB_DIR}

# Copy PLCComS configuration
COPY PLCComS.ini ${TECO_CONF_DIR}
COPY FIXED_Foxtrot.pub ${TECO_CONF_DIR}

# Volume configuration
VOLUME ["/var/log/teco", "/etc/teco"]

# Start PLCComS_x86_64
COPY start.sh /start.sh
CMD ["./start.sh"]

# EOF
