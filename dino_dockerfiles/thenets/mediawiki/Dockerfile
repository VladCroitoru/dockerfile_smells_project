FROM mediawiki:1.33

LABEL   org.thenets="TheNets.org" \
        org.thenets.wiki="TheNets.org Wiki" \
        version="0.1" \
        description="MediaWiki Docker version created by TheNets.org." \
        maintainer="luiz@thenets.org"

# Install updates
RUN apt-get update && apt-get upgrade -y && apt-get autoremove -y && \
    # Mail dependencies
    pear install mail net_smtp && \
    apt-get autoremove -y  && apt-get clean && rm -r /var/lib/apt/lists/*

ENV APP_DIR=/var/www/html \
    DATA_DIR=/var/www/data \
    EXTENSIONS="Duplicator Echo MobileFrontend VisualEditor NetworkAuth TextExtracts Popups BetaFeatures"

WORKDIR $DATA_DIR

# Install extensions
RUN cd $APP_DIR/extensions && \
    for EXTENSION in $EXTENSIONS; do \
        cd $APP_DIR/extensions && \
        git clone --depth 1 -b $MEDIAWIKI_BRANCH https://gerrit.wikimedia.org/r/p/mediawiki/extensions/"$EXTENSION".git && \
        cd $APP_DIR/extensions/$EXTENSION && \
        git submodule update --init ; \
    done && \
    chown -R 1000.1000 $APP_DIR/extensions/

# Add .htaccess
# http://www.mediawiki.org/wiki/Manual:Short_URL/Apache
ADD ./.htaccess ${APP_DIR}

# Enable Apache Modules
RUN a2enmod rewrite

# Add Scripts
ADD *.sh /

# Entrypoint
ENTRYPOINT ["/entrypoint.sh"]
CMD [""]

WORKDIR $APP_DIR
VOLUME ["$DATA_DIR"]
EXPOSE 80
