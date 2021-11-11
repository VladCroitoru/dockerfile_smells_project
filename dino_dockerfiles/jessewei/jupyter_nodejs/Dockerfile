FROM kota999/anaconda_jupyter:latest

#
# Install watson and tools
# 
RUN pip install --upgrade pip && \
    pip install --no-cache-dir --upgrade watson-developer-cloud  wordcloud google-api-python-client
    
RUN cd /notebooks && \
    npm install watson-developer-cloud --save && \
    npm install json-query -g && \
    npm install  json-query -g && \
    npm cache clean


#
# Arrange workspace
# 
RUN mkdir -p /notebooks/nb_demo && \
    mkdir -p /notebooks/nb_demo/watson && \
    mkdir -p /notebooks/nb_demo/resources 
COPY files/watson/* /notebooks/nb_demo/watson/
COPY files/resources/* /notebooks/nb_demo/resources/