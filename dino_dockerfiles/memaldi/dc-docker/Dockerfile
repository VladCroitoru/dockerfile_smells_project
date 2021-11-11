FROM memaldi/ckan

RUN pip install -e git+https://github.com/edincubator/ckanext-edi_theme#egg=ckanext-edi_theme
RUN pip install -e git+https://github.com/edincubator/ckanext-ga#egg=ckanext-ga
RUN pip install -e git+https://github.com/edincubator/ckanext-protect_resources#egg=ckanext-protect_resources
RUN pip install -e git+https://github.com/edincubator/ckanext-gdpr#egg=ckanext-gdpr

COPY production.ini /etc/ckan/default/production.ini