FROM 1and1internet/ubuntu-16-laravel-application

# The base image includes a version of laravel that may be incompatible, remove it
RUN rm -rf ./*

COPY dotenv ./.env

# Install dependencies via composer but do not run scripts as application is blank
COPY src/composer* ./
RUN \
	composer install \
		--no-ansi \
		--no-dev \
		--no-interaction \
		--no-progress \
		--prefer-dist \
		--no-scripts \
		--no-autoloader

# Copy the source and default production configuration into the image
COPY src ./

# Run composer scripts and any other setup.
RUN \
	composer dump-autoload --optimize && \
	php artisan optimize && \
	php artisan key:generate && \
	application-component-disable all && \
	application-component-enable web && \
	application-component-enable scheduler && \
	application-set-file-permissions