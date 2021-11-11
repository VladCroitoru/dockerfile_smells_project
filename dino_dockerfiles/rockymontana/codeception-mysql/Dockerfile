FROM codeception/codeception

MAINTAINER Jonas Erlandsson <jonas.erlandsson@sitedirect.se>

# Install php extensions
RUN docker-php-ext-install \
    mysqli  \
    pdo  \
    pdo_mysql
    
WORKDIR /project
