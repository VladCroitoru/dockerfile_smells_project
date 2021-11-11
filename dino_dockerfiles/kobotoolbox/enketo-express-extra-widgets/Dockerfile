FROM enketo/enketo-express:2.8.1

# GitHub Actions adds an authentication header to the Git configuration,
# which prevents us from installing Node modules in *public* GitHub
# repositories. Remove it crudely. See also
# https://github.com/actions/checkout/issues/162#issuecomment-591198381
RUN sed -i '/extraheader = AUTHORIZATION/d' .git/config

# `npm install` custom widgets here. Please note that widgets must also be
# listed in config.json to be enabled; see
# https://github.com/kobotoolbox/enketo-express/blob/master/doc/custom-widgets.md

RUN npm install https://github.com/kobotoolbox/enketo-image-customization-widget.git
RUN npm install https://github.com/kobotoolbox/enketo-literacy-test-widget.git

# Avoid problems like like:
#   Error: Cannot find module 'vex-dialog-enketo' from '/srv/src/enketo_express/public/js/src/module'
RUN npm install
