FROM node:8.9.4
MAINTAINER Eric Steinborn

# Install AATT
# Note: There are no versions/tags but have opened a new issue here: https://github.com/paypal/AATT/issues/33
# Using latest confirmed working commit HASH
RUN git clone https://github.com/paypal/AATT.git && \
    cd AATT/ && \
    git checkout 9d61dd5c713176135574389ac4cf4fa01bb12af8 && \
    npm install --unsafe-perm --quiet && \
    git submodule init && \
    git submodule update

WORKDIR AATT/

# Default configuration
ENV DEBUG "AATT*"
ENV http_port 3000

EXPOSE 3000

CMD ["node", "app.js"]
