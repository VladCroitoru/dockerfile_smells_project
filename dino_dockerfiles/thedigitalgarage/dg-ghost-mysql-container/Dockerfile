FROM ghost

MAINTAINER Edward, eddsuarez89@gmail.com

# Add in better default config
ADD config.example.js config.example.js

# Add a few themes
COPY themes/bootstraptheme    content/themes/bootstraptheme
COPY themes/ghostium          content/themes/ghostium
COPY themes/ghostScroll       content/themes/ghostScroll
COPY themes/mapache-godofredo content/themes/mapache-godofredo
COPY themes/perfetta          content/themes/perfetta
COPY themes/portfolio         content/themes/portfolio
COPY themes/saga              content/themes/saga
COPY themes/webkid            content/themes/webkid

# Fix ownership in src
RUN chown -R user $GHOST_SOURCE/content
RUN chgrp -R 0 $GHOST_SOURCE
RUN chmod -R g+rw $GHOST_SOURCE
RUN find $GHOST_SOURCE -type d -exec chmod g+x {} +

# Install GIT
RUN apt-get update && apt-get install -y git

# Change to non-root user
USER user

# Default environment variables
ENV NODE_ENV production

# Port 2368 for ghost server
EXPOSE 2368
