FROM scolagreco/docker-nginx:v1.12.2

COPY ./nginx.conf /etc/nginx/nginx.conf

# Metadata params
ARG BUILD_DATE
ARG VERSION="v1.12.2"
ARG VCS_URL="https://github.com/scolagreco/nginx-http-to-https.git"
ARG VCS_REF

# Metadata
LABEL maintainer="Stefano Colagreco <stefano@colagreco.it>" \
        org.label-schema.name="Nginx redirect HTTP to HTTPS" \
        org.label-schema.build-date=$BUILD_DATE \
        org.label-schema.version=$VERSION \
        org.label-schema.vcs-url=$VCS_URL \
        org.label-schema.vcs-ref=$VCS_REF \
        org.label-schema.description="Docker Image con Nginx compilato su Alpine Linux che carica un file di configurazione per eseguire un semplice redirect di tutte le richieste HTTP verso HTTPS."

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
