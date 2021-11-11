FROM python:3.5
ENV PYTHONUNBUFFERED 1

ENV APP_USER carra
ENV APP_ROOT /src

#---  Config as root  ( nginx, postgres and others )
RUN mkdir /config
COPY config /config

# RUN apt-get update \
#     && apt-get install -y --no-install-recommends \
#         postgresql-client \
#     && rm -rf /var/lib/apt/lists/*


#--  User and APP_ROOT creation 
RUN groupadd -r ${APP_USER} 
RUN useradd -r -m -d ${APP_ROOT} -s /usr/sbin/nologin -g ${APP_USER} ${APP_USER} 

#---  app env 
COPY src /src
RUN pip install -r /src/requirements.txt


#-- User = $APP_USER  
RUN chown -R ${APP_USER}:${APP_USER} ${APP_ROOT}
WORKDIR ${APP_ROOT}
USER ${APP_USER}

EXPOSE 8000
VOLUME ["/db.sqlite3"]

# moved to docker-compose
ENTRYPOINT ["/src/entrypoint.sh"]
