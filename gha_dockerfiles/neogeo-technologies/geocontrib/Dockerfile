FROM python:3.7-slim-bullseye

ENV PYTHONUNBUFFERED=1
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal
ENV LC_ALL="C.UTF-8"
ENV LC_CTYPE="C.UTF-8"

RUN apt-get update && \
    apt-get install -y libproj-dev gdal-bin ldap-utils libpq-dev libmagic1 && \
    apt-get install -y --no-install-recommends netcat && \
    apt-get clean -y

#RUN echo deb http://deb.debian.org/debian testing main contrib non-free >> /etc/apt/sources.list && \
#    apt-get update && \
#    apt-get remove -y binutils && \
#    apt-get autoremove -y && \
#    apt-get purge -y --auto-remove && \
#    rm -rf /var/lib/apt/lists/*

RUN useradd -r -m apprunner
USER apprunner

# Set envs
ENV HOME=/home/apprunner
ENV PATH=$HOME/.local/bin:$PATH
ENV APP_PATH=$HOME/geocontrib_app

# if WORKDIR only is set, then $APP_PATH will be owned by root :-/
RUN mkdir $APP_PATH $APP_PATH/config $APP_PATH/media $APP_PATH/static
WORKDIR $APP_PATH

VOLUME $APP_PATH/config $APP_PATH/media $APP_PATH/static

# Upgrade pip
RUN pip install --user --upgrade pip
# Install python requirements
COPY requirements.txt .
RUN pip install --user -r requirements.txt gunicorn
COPY --chown=apprunner . src/

EXPOSE 5000
ENTRYPOINT ["src/docker/geocontrib/docker-entrypoint.sh"]
CMD ["gunicorn", "-w 3", "-b 0.0.0.0:5000", "config.wsgi:application"]
