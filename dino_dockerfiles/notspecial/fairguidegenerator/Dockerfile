FROM notspecial/amivtex

# Install uwsgi (build tools are required)
RUN apt-get update && apt-get install -y build-essential && \
    pip install uwsgi && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get purge -y --auto-remove build-essential

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY fairguidegenerator /fairguidegenerator
COPY app.py /app.py

# Environment variable for config, use path for docker secrets as default
ENV FAIRGUIDEGENERATOR_CONFIG=/run/secrets/fairguidegenerator_config

# Run uwsgi to serve the app on port 80
EXPOSE 80
CMD ["uwsgi", \
# [::] is required to listen for both IPv4 and IPv6
"--http", "[::]:80", \
# More efficient usage of resources
"--processes", "4", \
# Otherwise uwsig will crash with bytesio
"--wsgi-disable-file-wrapper", \
# Exit if app cannot be started, e.g. if config is missing
"--need-app", \
# Allows accessing the app at / as well as /fairguidegenerator
"--manage-script-name", \
"--mount", "/fairguidegenerator=app:app"]
