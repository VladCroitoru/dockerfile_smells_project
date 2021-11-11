FROM nginx:1.13.0

EXPOSE 8080

ADD nginx.conf /etc/nginx/nginx.conf
RUN apt-get update && apt-get install -y unzip wget && mkdir /usr/share/nginx/html/data

RUN wget -O /usr/share/nginx/html/data/googleaccount.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/googleaccount.zip && \
    unzip /usr/share/nginx/html/data/googleaccount.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/googleaccount.zip;

RUN wget -O /usr/share/nginx/html/data/gmail.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/gmail.zip && \
    unzip /usr/share/nginx/html/data/gmail.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/gmail.zip;

RUN wget -O /usr/share/nginx/html/data/googledriveanddocs.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/googledriveanddocs.zip && \
    unzip /usr/share/nginx/html/data/googledriveanddocs.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/googledriveanddocs.zip;

RUN wget -O /usr/share/nginx/html/data/googledocuments.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/googledocuments.zip && \
    unzip /usr/share/nginx/html/data/googledocuments.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/googledocuments.zip;

RUN wget -O /usr/share/nginx/html/data/googlespreadsheets.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/googlespreadsheets.zip && \
    unzip /usr/share/nginx/html/data/googlespreadsheets.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/googlespreadsheets.zip;

RUN wget -O /usr/share/nginx/html/data/androidbasics.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/androidbasics.zip && \
    unzip /usr/share/nginx/html/data/androidbasics.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/androidbasics.zip;

RUN wget -O /usr/share/nginx/html/data/photoshopbasics.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/photoshopbasics.zip && \
    unzip /usr/share/nginx/html/data/photoshopbasics.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/photoshopbasics.zip;

RUN wget -O /usr/share/nginx/html/data/imageediting101.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/imageediting101.zip && \
    unzip /usr/share/nginx/html/data/imageediting101.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/imageediting101.zip;

RUN wget -O /usr/share/nginx/html/data/grammar.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/grammar.zip && \
    unzip /usr/share/nginx/html/data/grammar.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/grammar.zip;

RUN wget -O /usr/share/nginx/html/data/internet101.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/internet101.zip && \
    unzip /usr/share/nginx/html/data/internet101.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/internet101.zip;

RUN wget -O /usr/share/nginx/html/data/chrome.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/chrome.zip && \
    unzip /usr/share/nginx/html/data/chrome.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/chrome.zip;

RUN wget -O /usr/share/nginx/html/data/word2013.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/word2013.zip && \
    unzip /usr/share/nginx/html/data/word2013.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/word2013.zip;

RUN wget -O /usr/share/nginx/html/data/excel2013.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/excel2013.zip && \
    unzip /usr/share/nginx/html/data/excel2013.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/excel2013.zip;

RUN wget -O /usr/share/nginx/html/data/powerpoint2013.zip https://media.gcflearnfree.org/assets/offlinesite/individualtopic_downloads/powerpoint2013.zip && \
    unzip /usr/share/nginx/html/data/powerpoint2013.zip -d /usr/share/nginx/html/data && \
    rm /usr/share/nginx/html/data/powerpoint2013.zip;

ADD index.html /usr/share/nginx/html
