FROM davask/d-apache2-php5
MAINTAINER davask <contact@davaskweblimited.com>

LABEL dwl.app.framework="wordpress"

RUN apt-get update
RUN apt-get install -y php5-gd
RUN rm -rf /var/lib/apt/lists/*

# Declare instantiation counter
ENV DWL_INIT_COUNT 3
# Copy instantiation specific file
COPY ./wordpress.sh $DWL_INIT_DIR/$DWL_INIT_COUNT-wordpress.sh
