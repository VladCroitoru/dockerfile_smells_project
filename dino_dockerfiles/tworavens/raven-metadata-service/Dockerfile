FROM python:3.6.8
MAINTAINER TwoRavens http://2ra.vn/

LABEL organization="Two Ravens" \
      2ra.vn.version="0.0.1-alpha" \
      2ra.vn.release-date="2018-03-08" \
      description="Web service for preprocessing tabular data"

# -------------------------------------
# Install debugging tools
# -------------------------------------
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    apt-utils\
    iputils-ping \
    telnet \
    vim

# -------------------------------------
# Set the workdir
# -------------------------------------
WORKDIR /var/webapps/raven-metadata-service

# -------------------------------------
# Copy over the requirements and run them
# -------------------------------------
COPY ./requirements/ ./requirements
RUN pip3 install --no-cache-dir -r requirements/30_preprocess_web.txt

# -------------------------------------
# Copy over the rest of the repository
# -------------------------------------
COPY . .

# -------------------------------------
# Copy preprocess script
# -------------------------------------
#COPY preprocess/scripts/preprocess_file.sh /usr/bin/preprocess_file.sh
#RUN chmod u+x /usr/bin/preprocess_file.sh

# -------------------------------------
# Create a volume for sharing between containers
# -------------------------------------
VOLUME /ravens_volume

# -------------------------------------
# Expose port for web communication
# - web: 8080
# -------------------------------------
EXPOSE 8080

ENV DJANGO_SETTINGS_MODULE=ravens_metadata.settings.local_settings

# -------------------------------------
# Update the working directory
# -------------------------------------
WORKDIR /var/webapps/raven-metadata-service/preprocess_web/code

# -------------------------------------
# Run preprocess against the entry point input param
# -------------------------------------
#ENTRYPOINT ["/usr/bin/preprocess_file.sh"]

CMD echo 'Starting preprocess web server.' && \
    fab init_db && \
    python manage.py runserver 0.0.0.0:8080

#RUN cd preprocess  && \
#    python preprocess.py
