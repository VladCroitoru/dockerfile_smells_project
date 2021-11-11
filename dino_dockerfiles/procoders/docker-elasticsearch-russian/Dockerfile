FROM elasticsearch:5.6.8-alpine

RUN bin/elasticsearch-plugin install http://dl.bintray.com/content/imotov/elasticsearch-plugins/org/elasticsearch/elasticsearch-analysis-morphology/5.6.8/elasticsearch-analysis-morphology-5.6.8.zip

ADD ./config /usr/share/elasticsearch/config
