FROM redmine:3.3

RUN sed -i 's/--no-auth-cache --non-interactive/--no-auth-cache --non-interactive --trust-server-cert/g' /usr/src/redmine/lib/redmine/scm/adapters/subversion_adapter.rb
