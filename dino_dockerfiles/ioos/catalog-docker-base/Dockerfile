FROM ioos/ckan:2.8.6

USER root
# Add my custom configuration file
COPY "./contrib/config/pycsw/pycsw.cfg" "$CKAN_CONFIG/"
# BWA (2019-03-29) need to update debian jessie sources for updates
COPY "./contrib/config/sources.list" "/etc/apt/sources.list"
COPY "./contrib/scripts/" "/usr/local/bin/"
RUN DEBIAN_FRONTEND=noninteractive apt-get update -y && \
                                   apt-get install -q --force-yes -y git libgeos-dev \
                                                        libxml2-dev \
                                                        libxslt1-dev \
                                                        libudunits2-dev && \
                                   apt-get -q clean && \
                                   rm -rf /var/lib/apt/lists/*

# pip install must be run with -e and then requirements manually installed
# in order for most CKAN plugins to work!
RUN ckan-pip install --no-cache-dir --upgrade 'certifi>=2018.10.15' \
                                              'setuptools' wheel Cython && \
    ckan-pip install --no-cache-dir 'pendulum==2.0.3' cf_units && \
    ckan-pip install --no-cache-dir --trusted-host files.pythonhosted.org \
       -e git+https://github.com/ckan/ckanext-googleanalytics.git@v2.0.2#egg=ckanext-googleanalytics \
       -e git+https://github.com/ioos/ckanext-spatial.git@ioos_ckan_master_rebase#egg=ckanext-spatial \
       -e git+https://github.com/ckan/ckanext-harvest.git@v1.1.1#egg=ckanext-harvest \
       -e git+https://github.com/ckan/ckanext-dcat.git@v0.0.8#egg=ckanext-dcat \
       -e git+https://github.com/ioos/catalog-ckan.git@62d4778754d22f5b7f2a5cb6f0c835cc95353ae8#egg=ckanext-ioos-theme \
       -e git+https://github.com/ioos/ckanext-sitemap@no_rev_time_handle#egg=ckanext-sitemap \
       -e git+https://github.com/ckan/ckanext-showcase@v1.2.0#egg=ckanext-showcase && \
    ckan-pip install --no-cache-dir \
       -r "$CKAN_VENV/src/ckanext-spatial/pip-requirements.txt" \
       -r "$CKAN_VENV/src/ckanext-harvest/pip-requirements.txt" \
       -r "$CKAN_VENV/src/ckanext-googleanalytics/requirements.txt" \
       -r "$CKAN_VENV/src/ckanext-dcat/requirements.txt" && \
    ckan-pip install -r "$CKAN_VENV/src/ckanext-sitemap/requirements.txt" && \
    ckan-pip install -U -e git+https://github.com/benjwadams/pycsw.git@link_split_fix_2.2.0#egg=pycsw && \
     # exclude ckanext-sitemap requirement as it clashes with the already
     # installed lxml version
    # fixme: update pycsw version
    ckan-pip install --no-cache-dir lxml>=3.6.2 && \
    ckan-pip install ckanapi

# the above appears to be necessary to run separately, or otherwise it results
# in a double requirements error with the above requirements files

COPY ./contrib/scripts/check_plugins.bash /
COPY ./contrib/fixture_data /opt/fixture_data
RUN chmod +x /check_plugins.bash /opt/fixture_data/set_harvests.bash
# PyCSW config is hardcoded for the time being
COPY ./contrib/config/pycsw/pycsw.cfg /etc/pycsw/pycsw.cfg
ENTRYPOINT ["/check_plugins.bash"]
USER ckan

CMD ["ckan-paster","serve","/etc/ckan/production.ini"]
