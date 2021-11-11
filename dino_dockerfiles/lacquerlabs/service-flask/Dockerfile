FROM alpine:3.7
LABEL maintainer="Joelle Gilley gilley.joelle@gmail.com"

# Set the timezone
# ENV TIMEZONE=America/New_York
ENV TIMEZONE=UTC

# Load ash profile on launch
ENV ENV=/etc/profile

# NOTE: We *COULD* compress down these next 4 RUN
# statements to just ONE but for clarity, readability
# and such, I am breaking things into distinctive steps
# here so this container can be used as a learning toy

# Setup ash profile prompt and my old man alias
# Create work directory
RUN mv /etc/profile.d/color_prompt /etc/profile.d/color_prompt.sh && \
    echo alias dir=\'ls -alh --color\' >> /etc/profile && \
    mkdir -p /app /run/nginx

# Install the required services dumb-init.  Also install and fix timezones / ca-certificates
# Install nginx, python and pip (git too)
RUN apk --update --no-cache add dumb-init tzdata ca-certificates \
    nginx python py2-pip git && \
    cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \
    echo "${TIMEZONE}" > /etc/timezone && \
    apk del tzdata && \
    update-ca-certificates

# install gunicorn and the flask
RUN pip install gunicorn flask

# we're not going to use supervisord in this image because if we have a failure
# starting the app up with gunicorn, we want it to FAIL and the container to stop

# Setup the www-data user that nginx will run as
RUN adduser -u 82 -D -S -G www-data www-data && \
    rm -rf /etc/nginx/conf.d/default.conf && \
    chown -R nginx:www-data /run/nginx && \
    chown -R :www-data /app && \
    chmod -R g+rw /app

# Add the container config files
COPY container_configs /

# setup our working directory
WORKDIR /app

# we're going to copy in the requirements.txt here because we're going to try to
# cache this installation as much as possible.  Copying requirements.txt and
# doing the install BEFORE we copy in the codebase helps with this greatly
COPY ./code/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# go ahead and copy in the codebase as a final step
COPY ./code .

# expose our service port
EXPOSE 80

# start with our PID 1 controller
ENTRYPOINT ["/usr/bin/dumb-init", "--"]

# what we use to start the container
# Gunicorn Bind to 127.0.0.1:9292, 4 workers, reload on code change
CMD ["/bin/sh", "-c", "nginx -g \"daemon on;\" && gunicorn -b 127.0.0.1:9292 -w 4 --reload main:app"]
