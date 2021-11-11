FROM centos:7

ADD . /root/compass-tasks

RUN /root/compass-tasks/build.sh

EXPOSE 6379

VOLUME ["/var/ansible", "/etc/compass/machine_list", "/etc/compass/switch_list"]

ENTRYPOINT ["/bin/bash", "-c"]
CMD ["/usr/local/bin/start.sh"]
