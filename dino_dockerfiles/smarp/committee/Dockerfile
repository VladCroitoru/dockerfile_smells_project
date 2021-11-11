FROM ubuntu:14.04

# Setup general environment
ENV SHELL bash
ENV WORKON_HOME /usr/bin/app

# Copy needed files
COPY bin/committee ${WORKON_HOME}/

WORKDIR ${WORKON_HOME}/

# Create empty json objects for the script
RUN mkdir ${WORKON_HOME}/data

# Create empty files if they don't exist already
RUN if [ ! -e "${WORKON_HOME}/data/rp.json" ]; then echo "{}" > ${WORKON_HOME}/data/rp.json; fi
RUN if [ ! -e "${WORKON_HOME}/data/vr.json" ]; then echo "{}" > ${WORKON_HOME}/data/vr.json; fi 
RUN if [ ! -e "${WORKON_HOME}/data/sv.json" ]; then echo "{}" > ${WORKON_HOME}/data/sv.json; fi

# Start the script
CMD ["./committee", "2052", "2053"]

# Open ports for the committee
EXPOSE 2052 2053