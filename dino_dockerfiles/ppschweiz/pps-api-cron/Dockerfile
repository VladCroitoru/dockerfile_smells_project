FROM node:5.3-onbuild

ENV CIVICRM_SERVER http://wordpress.local.piratenpartei.ch
ENV CIVICRM_PATH /wp-content/plugins/civicrm/civicrm/extern/rest.php/extern/rest.php
ENV CIVICRM_SITE_KEY secret
ENV CIVICRM_API_KEY secret

CMD ./cron.sh
