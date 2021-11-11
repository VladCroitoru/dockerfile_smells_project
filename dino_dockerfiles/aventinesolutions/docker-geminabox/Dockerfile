FROM aventinesolutions/docker-archlinux-rvm

MAINTAINER Matthew Eichler <matthew.eichler@aventinesolutions.nl>

ENV APP_HOME /opt/rubie

COPY install_geminabox.sh config.ru rackup.sh .ruby-version .ruby-gemset $APP_HOME/
RUN sudo chown -Rv rubie $APP_HOME

USER rubie
WORKDIR $APP_HOME

RUN $APP_HOME/install_geminabox.sh 

EXPOSE 9292
VOLUME ["/data"]
ENTRYPOINT ["/bin/zsh"]
