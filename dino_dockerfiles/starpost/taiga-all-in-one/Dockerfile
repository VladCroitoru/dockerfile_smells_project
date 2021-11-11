FROM alpine:edge

RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories

RUN apk update && apk add \
        python3 \
        python3-dev \
        libxml2-dev \
        libxslt-dev \
        nodejs-current \
        unzip \
        gettext \
        openssl \
        postgresql \
        postgresql-dev \
	rabbitmq-server \
	gcc \
	jpeg-dev zlib-dev musl-dev \
	git \
	bash \
        nginx
#       redis-server \


# ===== taiga backend
RUN wget -O /taiga-back.zip \
	https://github.com/taigaio/taiga-back/archive/stable.zip
RUN unzip /taiga-back.zip -d /
RUN mv /taiga-back-stable /taiga-back

WORKDIR /taiga-back
RUN LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pip3 install -r requirements.txt"

COPY taiga-back/* /taiga-back/settings/

RUN python3 manage.py compilemessages
RUN python3 manage.py collectstatic --noinput


# ===== taiga frontend
RUN wget -O /taiga-front-dist.zip \
	https://github.com/taigaio/taiga-front-dist/archive/stable.zip
RUN unzip /taiga-front-dist.zip -d /
RUN mv /taiga-front-dist-stable /taiga-front-dist

WORKDIR /taiga-front-dist

COPY taiga-front/* /taiga-front-dist/dist/


# ===== taiga events
RUN git clone https://github.com/taigaio/taiga-events.git /taiga-events
WORKDIR /taiga-events
RUN npm install -g coffee-script
RUN npm install

COPY taiga-events/* /taiga-events/

# ===== nginx config
COPY nginx/nginx.conf /etc/nginx/nginx.conf

# ===== Cleanup
RUN rm -rf /taiga-front-dist.zip /taiga-back.zip


# ===== Helper Scripts
RUN mkdir -p /scripts
COPY scripts/* /scripts/

WORKDIR /scripts

# ===== Fix misc
RUN mkdir -p /run/nginx
RUN chown rabbitmq /usr/lib/rabbitmq


EXPOSE 80

VOLUME /var/lib/postgresql
VOLUME /var/lib/rabbitmq
VOLUME /taiga-back/media

ENTRYPOINT [ "/scripts/entrypoint.sh" ]
CMD [ "./forego", "start" ]


# ===== GitLab Integration
RUN git clone https://github.com/starpost/taiga-contrib-gitlab-auth.git /taiga-gitlab
WORKDIR /taiga-gitlab
RUN git checkout gitlab

# --- front
WORKDIR /taiga-gitlab/front
RUN npm install gulp-cli -g
RUN npm install gulp -D
RUN npm install
RUN gulp build

RUN mkdir -p /taiga-front-dist/dist/plugins/gitlab-auth/
RUN cp -a dist/* /taiga-front-dist/dist/plugins/gitlab-auth/

# --- back
WORKDIR /taiga-gitlab/back
RUN pip3 install -e .

# --- back to scripts
WORKDIR /scripts
