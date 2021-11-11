FROM wordpress:latest

RUN apt-get -y update && apt-get install -y wget unzip git nano

RUN cd /usr/src/wordpress/wp-content/plugins && \
    wget https://downloads.wordpress.org/plugin/wp-appkit.1.5.5.zip && \
    wget https://downloads.wordpress.org/plugin/wp-rss-aggregator.4.17.4.zip && \
    wget https://github.com/versionpress/versionpress/releases/download/4.0-beta2/versionpress-4.0-beta2.zip && \
    wget https://github.com/ucsf-app/site/raw/master/plugins/wp-appkit-ssl.zip && \
    wget https://downloads.wordpress.org/plugin/category-tag-pages.zip && \
    wget https://downloads.wordpress.org/plugin/custom-css-js.3.37.zip && \
    wget https://downloads.wordpress.org/plugin/smart-slider-3.zip && \
    unzip \*.zip && \
    rm *.zip
	
COPY themes/twentytwenty-childT.zip /usr/src/wordpress/wp-content/themes/twentytwenty-childT.zip

RUN cd /usr/src/wordpress/wp-content/themes && \
    unzip twentytwenty-childT.zip && \
    rm twentytwenty-childT.zip

COPY uploads/uploads.zip /usr/src/wordpress/wp-content/uploads/uploads.zip

RUN cd /usr/src/wordpress/wp-content/uploads && \
    unzip uploads.zip && \
    rm uploads.zip

COPY wp-config.php /usr/src/wordpress/wp-config.php