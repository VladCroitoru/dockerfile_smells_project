FROM rgielen/httpd-image-drush:latest

# If existent, drush will use contrib subdir for managed modules
# See https://www.drupal.org/node/371298
RUN cd ${BASE_DIR} && drush -y dl drupal-7 --drupal-project-rename ${DRUPAL_PROJECT_NAME} \
    && cd ${DRUPAL_DIR} \
    && mkdir ${DRUPAL_MODULES_DIR}/contrib && mkdir ${DRUPAL_MODULES_DIR}/custom && mkdir ${DRUPAL_FILES_DIR} \
    && cp sites/default/default.settings.php sites/default/settings.php \
    && chmod ug+w sites/default/default.settings.php \
    && fix-drupal-permissions.sh --drupal_path=${DRUPAL_DIR} --drupal_user=drupal --httpd_group=www-data

VOLUME ${DRUPAL_MODULES_DIR} ${DRUPAL_THEMES_DIR} ${DRUPAL_FILES_DIR}
