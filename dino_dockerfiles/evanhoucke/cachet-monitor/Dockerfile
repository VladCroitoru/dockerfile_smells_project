FROM debian

ADD https://github.com/CastawayLabs/cachet-monitor/releases/download/v2.0/cachet-monitor_linux_amd64 /src/cachet-monitor_linux_amd64
ADD example.config.json /etc/cachet-monitor.config.json
RUN chmod +x /src/cachet-monitor_linux_amd64
CMD /src/cachet-monitor_linux_amd64

