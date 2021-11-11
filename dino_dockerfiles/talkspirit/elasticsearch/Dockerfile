FROM elasticsearch:1.7.3

# Print "Customization Elasticsearh for talkSpirit"

#elasticsearch plugins
RUN /usr/share/elasticsearch/bin/plugin -install royrusso/elasticsearch-HQ
RUN /usr/share/elasticsearch/bin/plugin -install mobz/elasticsearch-head
RUN /usr/share/elasticsearch/bin/plugin -install karmi/elasticsearch-paramedic
RUN /usr/share/elasticsearch/bin/plugin -install polyfractal/elasticsearch-segmentspy
RUN /usr/share/elasticsearch/bin/plugin -install polyfractal/elasticsearch-inquisitor
RUN /usr/share/elasticsearch/bin/plugin -install elasticsearch/elasticsearch-mapper-attachments/2.7.1
RUN /usr/share/elasticsearch/bin/plugin -install lukas-vlcek/bigdesk
RUN /usr/share/elasticsearch/bin/plugin -install lmenezes/elasticsearch-kopf
