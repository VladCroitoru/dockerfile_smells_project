FROM python:3.5-alpine
MAINTAINER Andrei Poenaru <andrei.poenaru@gmail.com>

RUN mkdir -p /comics-mailer/code

COPY comics_mailer.py /comics-mailer/code
COPY requirements.txt /comics-mailer/code
COPY docker-startup.sh /comics-mailer/code/startup.sh

# Prepare environment
RUN addgroup -S comics && \
    adduser -S comics -G comics -s /bin/sh && \
    pip install -r /comics-mailer/code/requirements.txt

# Prepare files
RUN mkdir -p /home/comics/.config/comics-mailer && \
    mkdir -p /home/comics/.local/share/comics-mailer && \
    ln -s /home/comics/.config/comics-mailer /comics-mailer/config && \
    ln -s /home/comics/.local/share/comics-mailer /comics-mailer/data

# Set the cron timing (will be used in the startup script)
ENV CRON '0 18 * * 3' 

VOLUME ["/comics-mailer/data", "/comics-mailer/config"]

# Run the startup script as root to set permissions properly. This will drop down to the unprivilleged user for the actual application.
ENTRYPOINT ["/bin/sh", "/comics-mailer/code/startup.sh"]
CMD ["run"]

