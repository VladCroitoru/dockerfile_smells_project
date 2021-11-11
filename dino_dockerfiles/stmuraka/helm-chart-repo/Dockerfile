FROM nginx:alpine

# Install required packages
RUN apk update \
 && apk add \
        openssl \
        inotify-tools

# Configure Nginx
# Update mime.types to serve yaml files
RUN sed -i -e '/^types.*/a\ \ \ \ text/yaml                             yaml yml;' /etc/nginx/mime.types
# Replace default html files
COPY 50x.html /usr/share/nginx/html/
COPY index.html /usr/share/nginx/html/

# Download and install Helm
WORKDIR /root/
ADD https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get /root/get_helm.sh
RUN chmod 700 get_helm.sh \
 && sh ./get_helm.sh \
 && rm ./get_helm.sh

# Setup Charts path
ENV CHART_DIR="/charts"
RUN mkdir -p ${CHART_DIR}
RUN helm repo index ${CHART_DIR}
RUN cp /etc/nginx/conf.d/default.conf /etc/nginx/conf.d/default.conf.orig
RUN sed -e "/^\s*location \/.*/i\ \ \ \ location ${CHART_DIR} {%\
\ \ \ \ \ \ \ \ alias  ${CHART_DIR};%\
\ \ \ \ \ \ \ \ index  index.yaml index.yml;%\
\ \ \ \ }%\
" /etc/nginx/conf.d/default.conf | tr "%" "\n" > /etc/nginx/conf.d/default.new
# Add extra mv step to avoid race condition on dockerhub build
RUN mv /etc/nginx/conf.d/default.new /etc/nginx/conf.d/default.conf
VOLUME ${CHART_DIR}

# INGRESS_SUBDOMAIN = URL used for hosted Chart
ENV INGRESS_SUBDOMAIN="mycluster.us-south.containers.mybluemix.net"
COPY start.sh /root/
CMD ./start.sh
