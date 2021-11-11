FROM jeandet/teamcity-docker-complete-agent
LABEL maintainer "Alexis Jeandet <alexis.jeandet@member.fsf.org>"

RUN echo "system.has_qt5=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_gcov=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_clang=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_clazy=true" >> /opt/buildagent/conf/buildAgent.dist.properties && \
    echo "system.has_vera=true" >> /opt/buildagent/conf/buildAgent.dist.properties

CMD ["/run-services.sh"]
