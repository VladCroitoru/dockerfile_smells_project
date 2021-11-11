FROM selenium/base:2.53.0
MAINTAINER QAutomatron

#==========
# Selenium Force Update
#==========
RUN  mkdir -p /opt/selenium \
  && wget --no-verbose https://selenium-release.storage.googleapis.com/2.53/selenium-server-standalone-2.53.1.jar -O /opt/selenium/selenium-server-standalone.jar

#========================
# Selenium Configuration
#========================

EXPOSE 4444

ENV GRID_NEW_SESSION_WAIT_TIMEOUT -1
ENV GRID_JETTY_MAX_THREADS -1
ENV GRID_NODE_POLLING  5000
ENV GRID_CLEAN_UP_CYCLE 5000
ENV GRID_TIMEOUT 150000
ENV GRID_BROWSER_TIMEOUT 300000
ENV GRID_MAX_SESSION 300
ENV GRID_UNREGISTER_IF_STILL_DOWN_AFTER 30000

COPY generate_config /opt/selenium/generate_config
COPY entry_point.sh /opt/bin/entry_point.sh
RUN /opt/selenium/generate_config > /opt/selenium/config.json
RUN chown -R seluser /opt/selenium

USER seluser

CMD ["/opt/bin/entry_point.sh"]
