FROM shift/ruby:ruby-2.2.3

MAINTAINER Vincent Palmer <shift@someone.section.me>

USER root
RUN echo '#!/bin/bash\n/bin/bash -l -c "cd /home/deploy/app && bundle exec unicorn_rails"' > /start.sh && chmod 0755 /start.sh
USER deploy
EXPOSE 8080/tcp
CMD ["/start.sh"]
