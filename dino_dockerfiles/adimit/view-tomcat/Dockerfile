FROM tomcat:8.5-jre8

ENV VISLCG3_REVISION="12191"
ENV runtime_dependencies "libgoogle-perftools4"
ENV build_dependencies "subversion build-essential cmake git libgoogle-perftools-dev libboost-dev libicu-dev"

RUN apt-get -qy update \
 && apt-get install -y $runtime_dependencies $build_dependencies \
 && mkdir -p /usr/local/werti \
 && mkdir -p /usr/local/werti/resources \
 && tmp=$(mktemp -d) \
 && cd $tmp \
 && git clone https://github.com/linziheng/pdtb-parser \
 && mv pdtb-parser/lib/morph/morphg /usr/local/bin \
 && mv pdtb-parser/lib/morph/verbstem.list /usr/local/werti/resources \
 && rm -rf pdtb-parser \
 && cd $tmp \
 && svn co http://beta.visl.sdu.dk/svn/visl/tools/vislcg3/trunk@$VISLCG3_REVISION vislcg3 \
 && cd vislcg3 \
 && ./cmake.sh \
 && make -j5 \
 && make install \
 && apt-get remove -y $build_dependencies \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/* \
 && rm -rf $tmp \
 && echo "/usr/local/lib/x86_64-linux-gnu/" > /etc/ld.so.conf.d/local.conf \
 && ldconfig

COPY conf /usr/local/tomcat/conf/

RUN groupadd -g 1003 view \
 && useradd -u 1003 -g 1003 view \
 && mkdir -p /usr/local/view/db \
 && chown -R view:view /usr/local/tomcat /usr/local/view/db

VOLUME /usr/local/tomcat/webapps
VOLUME /usr/local/view/db

USER view
CMD ["catalina.sh", "run"]
