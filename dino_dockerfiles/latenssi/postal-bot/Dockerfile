FROM python:2.7

# Set the file maintainer (your name - the file's author)
MAINTAINER Lauri Junkkari

# Set env variables used in this Dockerfile
ENV POSTAL_BOT_SRC=.
ENV POSTAL_BOT_SRVHOME=/srv
ENV POSTAL_BOT_SRVPROJ=/srv/postal-bot

# Create application subdirectories
WORKDIR $POSTAL_BOT_SRVHOME
RUN mkdir logs
VOLUME ["$POSTAL_BOT_SRVHOME/logs/"]

# Copy application source code to SRCDIR
COPY $POSTAL_BOT_SRC $POSTAL_BOT_SRVPROJ

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r $POSTAL_BOT_SRVPROJ/requirements.txt -U

# Port to expose
EXPOSE 8000

# Copy entrypoint script into the image
WORKDIR $POSTAL_BOT_SRVPROJ
COPY $POSTAL_BOT_SRC/scripts/docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
