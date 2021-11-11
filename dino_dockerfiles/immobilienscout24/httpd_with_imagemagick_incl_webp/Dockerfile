FROM httpd:2.2

RUN set -x && \
    cp /etc/apt/sources.list /etc/apt/sources.list.orig && \
    sed -i -rn "s;^(deb) (.*);\1 \2\ndeb-src \2;p" /etc/apt/sources.list && \
    apt-get update && \
    buildDeps=$(apt-cache showsrc imagemagick | sed -rn 's;^Build-Depends.*: (.*);\1;p' | tr "," "\n" | sort -u | sed -rn 's;^ *([^ ]*).*;\1;p' | tr "\n" " ") && \
    apt-get install -y --no-install-recommends $buildDeps libgraphviz-dev build-essential fakeroot devscripts libwebp-dev && \
    mkdir src && \
    cd src && \
    apt-get source imagemagick -y && \
    cd $(find -mindepth 1 -maxdepth 1 -type d -name "imagemagick-*") && \
    debchange --nmu "enable webp" && \
    debuild -us -uc -i -I && \
    apt-get remove -y --auto-remove --purge build-essential fakeroot devscripts libgraphviz-dev $buildDeps && \
    apt-get autoclean -y && \
    apt-get install apt-utils -y --no-install-recommends && \
    cd .. && \
    mkdir -p /usr/local/imagemagick-debs && \
    find -maxdepth 1 -type f -name "*deb" -exec mv -t /usr/local/imagemagick-debs/ {} + && \
    cd /usr/local/imagemagick-debs && \
    apt-ftparchive packages . > Packages && \
    gzip -c Packages > Packages.gz && \
    apt-ftparchive release . > Release && \
    sed -i '2s;^;Codename: imagemagick-with-webp\n;' Release && \
    echo 'deb file:/usr/local/imagemagick-debs ./' > /etc/apt/sources.list.d/local_imagemagick_repo.list && \
    apt-get update -o Dir::Etc::sourcelist="sources.list.d/local_imagemagick_repo.list" -o Dir::Etc::sourceparts="-" -o APT::Get::List-Cleanup="0" -y && \
    apt-get --no-install-recommends install -t imagemagick-with-webp libmagickcore-dev libmagickwand-dev -y --force-yes && \
    [ -f libmagickcore-dev_$(dpkg -s libmagickcore-dev | sed -nr 's;^Version: [0-9]+:(.*);\1;p')* ] && [ -f libmagickwand-dev_$(dpkg -s libmagickwand-dev | sed -nr 's;^Version: [0-9]+:(.*);\1;p')* ] && \
    apt-get --no-install-recommends install libcurl4-gnutls-dev libwebp-dev ghostscript -y && \
    apt-get remove -y --auto-remove --purge apt-utils && \
    rm -rf /var/lib/apt/lists/* && \
    cd - && \
    cd .. && \
    rm -rf src && \
    rm -rf /usr/local/imagemagick-debs && \
    rm -rf /etc/apt/sources.list.d/local_imagemagick_repo.list && \ 
    mv /etc/apt/sources.list.orig /etc/apt/sources.list
