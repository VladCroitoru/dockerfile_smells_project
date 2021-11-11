FROM opensuse:leap

RUN zypper install -y dbus-1 systemd-sysvinit

# configure dbus to be started by systemd?
# TODO: investigate why it is necessary to remove this configuration param
RUN cp /usr/lib/systemd/system/dbus.service /etc/systemd/system/; \
    sed -i 's/OOMScoreAdjust=-900//' /etc/systemd/system/dbus.service

VOLUME ["/sys/fs/cgroup", "/run"]

CMD ["/sbin/init"]
