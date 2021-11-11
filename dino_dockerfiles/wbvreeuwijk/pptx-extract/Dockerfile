FROM openjdk:8 

LABEL version="1.0" 
LABEL description="Docker image for converting PPTX files to QVX" 
LABEL maintainer="bvk@qlik.com" 

RUN apt-get update \
 && apt-get install ca-certificates wget cron -y 
 
RUN wget https://github.com/wbvreeuwijk/pptx-extract/releases/download/0.4.3/pptx-extract.zip \
 && unzip -o pptx-extract.zip \  
 && rm  pptx-extract.zip 
 
RUN mkdir /config \  
 && mkdir /presentations \  
 && mkdir /data 
 
ENV GOOGLE_APPLICATION_CREDENTIALS=/config/google.json
ENV FONT_DIR=/pptx-extract/fonts

VOLUME /config 
VOLUME /presentations 
VOLUME /data 

# Insert schedule in crontab 
RUN echo "FONT_DIR=/pptx-extract/fonts" >> /etc/crontab
RUN echo "GOOGLE_APPLICATION_CREDENTIALS=/config/google.json" >> /etc/crontab
RUN echo "0,15,30,45 * * * * root /pptx-extract/bin/pptx-extract /presentations /data > /proc/1/fd/1 2>/proc/1/fd/2" >> /etc/crontab

WORKDIR /config 

CMD ["cron","-f","-L","15"]

