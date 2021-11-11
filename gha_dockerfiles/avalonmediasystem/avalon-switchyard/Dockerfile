# Build development image
FROM        ruby:2.7 as development

RUN         useradd -m -U app \
         && su -s /bin/bash -c "mkdir -p /home/app/switchyard" app
WORKDIR     /home/app/switchyard
COPY        --chown=app:app . .
RUN         bundle install --with development test debug --without production
USER app
ENV         RACK_ENV=development
CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "4567"]

# Build production image
FROM        ruby:2.7 as production

RUN         useradd -m -U app \
         && su -s /bin/bash -c "mkdir -p /home/app/switchyard" app
WORKDIR     /home/app/switchyard
COPY        --chown=app:app . .
RUN         bundle install --without development test debug --with production
USER app
ENV         RACK_ENV=production
CMD ["bundle", "exec", "rackup", "--host", "0.0.0.0", "-p", "4567"]
