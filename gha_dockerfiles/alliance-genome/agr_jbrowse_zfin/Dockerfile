# JBrowse

#
# This docker file uses multistage builds, where the first stage (named 'build')
# gets lots of prereqs, checks out git repos and runs the setup script. The
# resulting image is over 2GB and can be deleted after building. The second
# stage (called 'production') then copies files from the first stage and
# results in a image that is just over 100MB.
#
# Also, note the change to the initial parent image: there is now a jbrowse-buildenv
# image at docker hub
#
# Finally, a short note about how this JBrowse instance is configured to work:
# This instance is served up by nginx and only the configuration files and 
# javascript files are served from here.  All of the data are stored in an AWS
# S3 bucket.  This separation makes development and production issues easier
# (in my opinion)

FROM gmod/jbrowse-buildenv:latest as build
LABEL maintainer="scott@scottcain.net"

# Actual JBrowse code; can bump the release tag and rebuild to get new versions
RUN git clone --single-branch --branch dev https://github.com/GMOD/jbrowse.git

#agr_jbrowse_config contains the configuration files for the various species; they are
#moved into the right place in the long RUN command below
#RUN git clone --single-branch --branch release-3.1.1 https://github.com/alliance-genome/agr_jbrowse_config.git
RUN git clone --single-branch --branch main https://github.com/alliance-genome/agr_jbrowse_zfin.git

#agr_jbrowse_plugin contains a simple plugin that puts the AGR logo in the upper left corner of the page
#RUN git clone --single-branch --branch release-3.2.0 https://github.com/alliance-genome/agr_jbrowse_plugin.git

#website-genome-browsers pulls in some glyphs we use (like diamond, triangle and a modified gene glyph)
#RUN git clone --single-branch --branch agr-release-3.2.0 https://github.com/WormBase/website-genome-browsers.git

#no longer need to fetch vcf files
#WORKDIR /agr_jbrowse_config/scripts
#RUN ./fetch_vcf.sh jbrowse

RUN mkdir /usr/share/nginx/html/jbrowse

RUN rm /usr/share/nginx/html/index.html && rm /usr/share/nginx/html/50x.html && cp -r /jbrowse/* /usr/share/nginx/html/jbrowse && \
    cp /jbrowse/.htaccess /usr/share/nginx/html/jbrowse/.htaccess && \
    cp /agr_jbrowse_zfin/jbrowse/example.html /usr/share/nginx/html/jbrowse && \
    cp -r /agr_jbrowse_zfin/jbrowse/data /usr/share/nginx/html/jbrowse

#getting the cached Alliance favicons to overwrite the J provide by JBrowse
#RUN cp /agr_jbrowse_config/jbrowse/agr_favicons/* /usr/share/nginx/html/jbrowse/img/favicons/

WORKDIR /usr/share/nginx/html/jbrowse

#RUN npm install yarn
#RUN ./node_modules/.bin/yarn
#RUN JBROWSE_BUILD_MIN=1 ./node_modules/.bin/yarn build

#in the near futre, this setup command will be replaced with the yarn commands above
#to make building faster (I don't want to mess with it right before a release)
RUN ./setup.sh -f

#this is the magic that makes the production container so very small
FROM nginx:latest as production

COPY --from=build /usr/share/nginx/html/jbrowse/dist /usr/share/nginx/html/jbrowse/dist
COPY --from=build /usr/share/nginx/html/jbrowse/browser /usr/share/nginx/html/jbrowse/browser
COPY --from=build /usr/share/nginx/html/jbrowse/css /usr/share/nginx/html/jbrowse/css
COPY --from=build /usr/share/nginx/html/jbrowse/data /usr/share/nginx/html/jbrowse/data
COPY --from=build /usr/share/nginx/html/jbrowse/img /usr/share/nginx/html/jbrowse/img
COPY --from=build /usr/share/nginx/html/jbrowse/index.html /usr/share/nginx/html/jbrowse/index.html
COPY --from=build /usr/share/nginx/html/jbrowse/example.html /usr/share/nginx/html/jbrowse/example.html
COPY --from=build /usr/share/nginx/html/jbrowse/jbrowse_conf.json /usr/share/nginx/html/jbrowse/jbrowse_conf.json
COPY --from=build /usr/share/nginx/html/jbrowse/jbrowse.conf /usr/share/nginx/html/jbrowse/jbrowse.conf
COPY --from=build /usr/share/nginx/html/jbrowse/LICENSE /usr/share/nginx/html/jbrowse/LICENSE
COPY --from=build /usr/share/nginx/html/jbrowse/plugins /usr/share/nginx/html/jbrowse/plugins
COPY --from=build /usr/share/nginx/html/jbrowse/site.webmanifest /usr/share/nginx/html/jbrowse/site.webmanifest
COPY --from=build /usr/share/nginx/html/jbrowse/.htaccess /usr/share/nginx/html/jbrowse/.htaccess


VOLUME /data
COPY docker-entrypoint.sh /
CMD ["/docker-entrypoint.sh"]
