FROM opencpu/base

RUN R -e 'devtools::install_github("rwebapps/nabel")'

RUN \
  echo 'Redirect /index.html /ocpu/library/nabel/www' > /etc/apache2/sites-enabled/app.conf
