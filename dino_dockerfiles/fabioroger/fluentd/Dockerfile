FROM ziyasal/k8splunk:1.0.5

RUN fluent-gem install fluent-plugin-kafka

ENTRYPOINT ["fluentd" , "-c" , "/etc/td-agent/td-agent.conf"]
