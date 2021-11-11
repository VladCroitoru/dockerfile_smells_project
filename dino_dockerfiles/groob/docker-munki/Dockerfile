FROM nginx
RUN mkdir -p /munki_repo
Run mkdir -p /etc/nginx/sites-enabled/
ADD nginx.conf /etc/nginx/nginx.conf
ADD munki-repo.conf /etc/nginx/sites-enabled/
VOLUME /munki_repo
EXPOSE 80
