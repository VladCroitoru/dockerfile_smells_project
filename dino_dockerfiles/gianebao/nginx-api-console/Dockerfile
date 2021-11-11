FROM nginx:latest

ENV AC_MAIN_DIR raml
ENV RAML_DIR /usr/share/nginx/html/api-console/$AC_MAIN_DIR
ENV AC_MAIN_FILE $AC_MAIN_DIR/api.raml

WORKDIR /

ADD nginx-signing-key nginx-signing-key

RUN \
 apt-key add nginx-signing-key/09122016.key

RUN \
 apt-get update && apt-get -y upgrade &&\
 apt-get -y --no-install-recommends install git &&\
 apt-get -y install curl &&\
 apt-get autoclean && apt-get clean && apt-get autoremove

# Download and install https://github.com/gianebao/api-console
RUN \
 git clone https://github.com/gianebao/api-console &&\
 mv /api-console/dist/* /usr/share/nginx/html

WORKDIR /usr/share/nginx/html

# Point the raml-console-loader to the raml/api.raml
RUN mkdir -p $RAML_DIR &&\
 sed -i \
 "s|<raml-initializer></raml-initializer>|<raml-console-loader src=\"$AC_MAIN_FILE\" disable-theme-switcher disable-raml-client-generator></raml-console-loader>|g" \
 index.html

# Do some cleanup
RUN rm -rf examples /api-console
