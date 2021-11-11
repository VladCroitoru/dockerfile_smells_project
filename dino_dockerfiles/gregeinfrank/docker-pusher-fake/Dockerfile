#
# Dockerfile for Pusher-Fake
#
# https://github.com/tristandunn/pusher-fake
#
FROM ruby:2.3.4
MAINTAINER Greg Einfrank <greg.einfrank@gmail.com>

# Create working space
WORKDIR /home

# Install pusher-fake
RUN gem install pusher:1.3.1 pusher-fake:1.8.0

ADD entrypoint.sh /home/entrypoint.sh

ENV PUSHER_APP_ID=PUSHER_APP_ID \
    PUSHER_APP_KEY=PUSHER_APP_KEY \
    PUSHER_APP_SECRET=PUSHER_APP_SECRET \
    PUSHER_WEB_PORT=57003 \
    PUSHER_SOCKET_PORT=57004

EXPOSE $PUSHER_SOCKET_PORT $PUSHER_WEB_PORT

# Default command for image
CMD ["/home/entrypoint.sh"]
