FROM wordpress:latest

MAINTAINER eric@eamann.com

# Sadly, we need to use unzip
RUN apt-get update && apt-get install -y unzip --no-install-recommends \
	&& rm -r /var/lib/apt/lists/*

# Upstream install of Capsule as a theme
RUN curl -o capsule.zip -SL http://downloads.sourceforge.net/project/wp-capsule/1.1.1/capsule-1.1.1.zip \
	&& unzip capsule.zip -d /usr/src/wordpress/wp-content/themes \
	&& rm capsule.zip \
	&& chown -R www-data:www-data /usr/src/wordpress/wp-content/themes/capsule

# Upstream install of WordPress SEO
RUN curl -o wordpress-seo.zip -SL https://downloads.wordpress.org/plugin/wordpress-seo.2.3.2.zip \
	&& unzip wordpress-seo.zip -d /usr/src/wordpress/wp-content/plugins \
	&& rm wordpress-seo.zip \
	&& chown -R www-data:www-data /usr/src/wordpress/wp-content/plugins/wordpress-seo

# Upstream install of S3-Uploads
RUN curl -o s3-uploads.tar.gz -SL https://github.com/humanmade/S3-Uploads/archive/v0.9.0.tar.gz \
	&& tar -xzf s3-uploads.tar.gz -C /usr/src/wordpress/wp-content/plugins \
	&& rm s3-uploads.tar.gz \
	&& chown -R www-data:www-data /usr/src/wordpress/wp-content/plugins/S3-Uploads-0.9.0