FROM  alpine:3.5

MAINTAINER takayamaki

RUN   apk add --no-cache ruby ruby-dev alpine-sdk apache2 logrotate ca-certificates &&\
      gem install --no-ri --no-rdoc json &&\
      sed -i -e 's%/var/log/messages%#/var/log/messages%' /etc/logrotate.conf &&\
      mkdir -p /run/apache2 &&\
      sed -i -e 's%#LoadModule cgi_module modules/mod_cgi.so%LoadModule cgi_module modules/mod_cgi.so%' /etc/apache2/httpd.conf&&\
      apk del --purge alpine-sdk ruby-dev &&\
      rm -f ~/.ash_history

COPY  dodontof.conf /etc/apache2/conf.d/

RUN   apk add --no-cache --virtual deps wget &&\
      mkdir -p /work && cd /work &&\
      wget -nv -O dodontof.zip https://www.dropbox.com/s/hd26rf4pkbi1oci/DodontoF_Ver.1.48.00_sugar_chocolate_waffle.zip?dl=1 &&\
      unzip -q dodontof.zip && rm dodontof.zip && cd DodontoF_WebSet/public_html &&\
      chmod 705 ../saveData \
                imageUploadSpace \
                imageUploadSpace/smallImages \
                DodontoF \
                DodontoF/DodontoFServer.rb \
                DodontoF/saveDataTempSpace \
                DodontoF/fileUploadSpace \
                DodontoF/replayDataUploadSpace &&\
      chmod 600 DodontoF/log.txt \
                DodontoF/log.txt.0  &&\
      mv ../saveData /var/www/localhost/ &&\
      mv ./* /var/www/localhost/htdocs/ &&\
      sed -i -e 's%#!/usr/local/bin/ruby -Ku%#!/usr/bin/ruby%' /var/www/localhost/htdocs/DodontoF/DodontoFServer.rb &&\
      cd / &&\
      rm -rf /work &&\
      chown apache:apache -R /var/www/localhost/saveData /var/www/localhost/htdocs/* &&\
      rm -f /var/www/localhost/htdocs/DodontoF/src_actionScript.zip &&\
      rm -f ~/.ash_history ~/.wget-hsts &&\
      apk del --purge deps

EXPOSE 80
CMD httpd -D FOREGROUND
