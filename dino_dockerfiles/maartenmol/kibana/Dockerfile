# https://github.com/elastic/kibana-docker
FROM docker.elastic.co/kibana/kibana:6.5.1

# Add your kibana plugins setup here
# Example: RUN kibana-plugin install <name|url>

RUN kibana-plugin install https://github.com/bitsensor/elastalert-kibana-plugin/releases/download/1.0.1/elastalert-kibana-plugin-1.0.1-6.5.1.zip
RUN kibana-plugin install https://github.com/MaartenMol96/kibana/releases/download/logtrail/logtrail-6.5.0-0.1.30.custom.zip
RUN kibana-plugin install https://github.com/MaartenMol96/kibana/releases/download/cleaner/cleaner-6.4.0.zip
