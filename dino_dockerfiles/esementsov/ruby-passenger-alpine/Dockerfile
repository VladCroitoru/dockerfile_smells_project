FROM alpine:3.6

LABEL name="Alpine 3.6 + ruby/passenger"

ENV ENV="/etc/profile.d/rbenv.sh"
ENV RBENV_ROOT=/usr/local/rbenv

ENV RBENV_VERSION=2.4.3
ENV RBENV_DOCVERSION=2.4.0
ENV PASSENGER_VERSION=5.2.1

ENV ac_cv_func_isnan yes
ENV ac_cv_func_isinf yes

RUN apk add --no-cache build-base\
				linux-headers\
				gnupg\
				openssl\
				gcc\
				bash\
				vim\
				ca-certificates\
				wget\
				git\
				make\
				patch\
				openssh\
				zip\
				unzip\
				zlib\ 
				zlib-dev\
				ruby\
				bind-tools\
				bzip2\
				g++\
				readline-dev\
				wget\
				postgresql\
				postgresql-dev\
				curl-dev\
				pcre-dev\
				postgresql-client\
				rsync\
				nodejs\
				tzdata\
				tar\
				procps\
				procps-dev

RUN				echo 'export RBENV_ROOT=/usr/local/rbenv' > /etc/profile.d/rbenv.sh\
				&&  echo 'export PATH="$RBENV_ROOT/bin:$PATH"' >> /etc/profile.d/rbenv.sh\
				&&  echo 'export PATH="$RBENV_ROOT/shims:$PATH"' >> /etc/profile.d/rbenv.sh\
				&&  echo 'eval "$(rbenv init -)"'  >> /etc/profile.d/rbenv.sh\
				&&  chmod +x /etc/profile.d/rbenv.sh
				
RUN				git clone https://github.com/rbenv/rbenv.git ${RBENV_ROOT}\
				&&  mkdir -p ${RBENV_ROOT}/plugins\
				&&  git clone https://github.com/rbenv/ruby-build.git ${RBENV_ROOT}/plugins/ruby-build\
				&&  git clone https://github.com/rbenv/rbenv-vars.git ${RBENV_ROOT}/plugins/rbenv-vars\
				&&  source /etc/profile.d/rbenv.sh
				
RUN				${RBENV_ROOT}/bin/rbenv install ${RBENV_VERSION}\
				&&  ${RBENV_ROOT}/shims/gem install passenger -v ${PASSENGER_VERSION} --no-ri --no-rdoc\
				&&  ${RBENV_ROOT}/shims/gem install bundler\
				&&  ${RBENV_ROOT}/shims/passenger-install-nginx-module --auto-download --auto --prefix=/opt/nginx\
				&&  ${RBENV_ROOT}/shims/passenger-config install-agent --auto\
				&&  ${RBENV_ROOT}/shims/passenger-config install-standalone-runtime --auto\
				&&  ${RBENV_ROOT}/bin/rbenv rehash
				
RUN				rm -rf /usr/local/rbenv/versions/${RBENV_VERSION}/lib/ruby/gems/${RBENV_DOCVERSION}/doc\
				/usr/local/rbenv/versions/${RBENV_VERSION}/lib/ruby/gems/${RBENV_DOCVERSION}/gems/passenger-${PASSENGER_VERSION}/doc\
				/usr/local/rbenv/versions/${RBENV_VERSION}/share/

# for clean container:
#				&&  apk del --no-cache gcc g++ linux-headers make ruby build-base

# FOR ssh access to container:
# COPY .ssh /root/.ssh
# RUN chmod 600 /root/.ssh/id_rsa

# healthcheck example:
# HEALTHCHECK CMD passenger-status | awk '/Requests in queue:/{print $4}' || exit 1
