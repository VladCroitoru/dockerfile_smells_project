FROM node:6
RUN mkdir /source
WORKDIR /source
ADD ./Dockerfile /source/Dockerfile
#COPY package.json bower.json ./
#COPY scripts ./scripts
RUN  npm -g install bower@1.8.0
RUN  npm -g install phantomjs2@2.2.0 
RUN  npm -g install ember-cli@2.9.1
#RUN  npm -g install babel-core babel-preset-es2015
RUN  npm -g install watchman
#RUN  npm -g install esprima
 RUN npm install  -g ansi_up@1.3.0
 RUN npm install  -g bootstrap-sass@3.3.7
 RUN npm install  -g broccoli-asset-rev@2.5.0
 RUN npm install  -g broccoli-middleware@1.0.0-beta.8
 RUN npm install  -g calculate-cache-key-for-tree@1.1.0
 RUN npm install  -g configstore@3.1.0  
 RUN npm install  -g diff@3.2.0  
 RUN npm install  -g ember-api-store@2.2.0
 RUN npm install  -g ember-bootstrap@1.0.0-rc.1
 RUN npm install  -g ember-browserify@1.1.13
 RUN npm install  -g ember-cli-app-version@2.0.2
 RUN npm install  -g ember-cli-babel@5.2.4
 RUN npm install  -g ember-cli-babili@0.1.4
 RUN npm install  -g ember-cli-clipboard@0.4.1
 RUN npm install  -g ember-cli-dependency-checker@1.4.0
 RUN npm install  -g ember-cli-htmlbars@1.3.3
 RUN npm install  -g ember-cli-htmlbars-inline-precompile@0.3.11
 RUN npm install  -g ember-cli-inject-live-reload@1.6.1
 RUN npm install  -g ember-cli-inline-content@0.4.1
 RUN npm install  -g ember-cli-jshint@1.0.5
 RUN npm install  -g ember-cli-node-assets@0.1.6
 RUN npm install  -g ember-cli-qunit@3.1.2
 RUN npm install  -g ember-cli-release@0.2.9
 RUN npm install  -g ember-cli-rtlcss@0.0.1
 RUN npm install  -g ember-cli-sass@5.6.0
 RUN npm install  -g ember-cli-sri@2.1.1
 RUN npm install  -g ember-cli-test-loader@1.1.1
 RUN npm install  -g ember-cli-uglify@1.2.0
 RUN npm install  -g ember-export-application-global@1.1.1
 RUN npm install  -g ember-highcharts@0.5.4
 RUN npm install  -g ember-href-to@1.6.0
 RUN npm install  -g ember-intl@2.13.0
 RUN npm install  -g ember-load-initializers@0.5.1
 RUN npm install  -g ember-power-select@1.0.0-beta.19
 RUN npm install  -g ember-resolver@2.1.1
 RUN npm install  -g ember-route-action-helper@2.0.3
 RUN npm install  -g ember-truth-helpers@1.2.0
 RUN npm install  -g execa@0.6.3  
 RUN npm install  -g express@4.15.3
 RUN npm install  -g forever-agent@0.6.1
 RUN npm install  -g glob@5.0.15
 RUN npm install  -g heimdalljs-graph@0.3.3
 RUN npm install  -g highcharts@5.0.14
 RUN npm install  -g http-proxy@1.16.2
 RUN npm install  -g lacsso@0.0.58
 RUN npm install  -g liquid-fire@0.26.4
 RUN npm install  -g loader.js@4.4.0
 RUN npm install  -g locate-path@2.0.0
 RUN npm install  -g markdown-it@8.3.1
 RUN npm install  -g node-sass@4.5.3
 RUN npm install  -g semver@5.3.0
 RUN npm install  -g shell-quote@1.6.1
 RUN npm install  -g validate-npm-package-name@3.0.0
 RUN npm install  -g xterm@1.0.0
 RUN npm install  -g yamljs@0.2.10
 RUN npm install  -g argparse@1.0.9
 RUN npm install  -g sprintf-js@1.0.3
 RUN npm install  -g glob@7.1.2

#COPY . /source
#RUN ./scripts/build-static -f -s   
RUN ember new my-first-ember-app
RUN npm config set registry https://registry.npm.taobao.org

CMD ["bash"]
#CMD ["npm","start","--","--ssl=false"]
