FROM php

RUN apt-get update && apt-get install -y ca-certificates && update-ca-certificates && apt-get install -y openssl && \
    apt-get install -y libicu-dev libcurl4-gnutls-dev libbz2-dev re2c libpng++-dev libpng3 libjpeg-dev libvpx-dev zlib1g-dev libgd-dev libssl-dev git curl wget && \
    docker-php-ext-install -j$(nproc) bz2 curl fileinfo iconv intl json

RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \
    php -r "if (hash_file('SHA384', 'composer-setup.php') === 'aa96f26c2b67226a324c27919f1eb05f21c248b987e6195cad9690d5c1ff713d53020a02ac8c217dbf90a7eacc9d141d') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;" && \
    php composer-setup.php --install-dir=/usr/bin --filename=composer && \
    php -r "unlink('composer-setup.php');"

RUN cd /tmp && \
    git clone https://github.com/nikic/php-ast.git && cd php-ast && phpize && ./configure && make install && \
    docker-php-ext-enable ast && \
    rm -rf /tmp/php-ast && \
    mkdir /linters

ADD install.sh /linters

RUN cd /linters && \
    chmod 0777 install.sh && ./install.sh && \
    chmod 0777 /linters/*

RUN /linters/phpcs --config-set show_progress 1


#php -d memory_limit=4G /linters/phpmd ./ text unusedcode --suffix=php
#php -d memory_limit=4G /linters/phan -l ./ -p
#php -d memory_limit=4G /linters/phpcs ./ --extensions=php --standard=PSR2 --error-severity=5 --warning-severity=8 --exclude=Generic.Commenting.DocComment,Generic.WhiteSpace.ScopeIndent,Generic.WhiteSpace.DisallowTabIndent,Generic.WhiteSpace.ScopeKeywordSpacing,Generic.WhiteSpace.SuperfluousWhitespace,Squiz.WhiteSpace.SuperfluousWhitespace,Squiz.WhiteSpace.ScopeKeywordSpacing,Squiz.WhiteSpace.ControlStructureSpacing,Squiz.WhiteSpace.ScopeClosingBrace,PSR2.ControlStructures.ControlStructureSpacing,Generic.NamingConventions.UpperCaseConstantName,Squiz.Functions.MultiLineFunctionDeclaration,Squiz.Functions.FunctionDeclarationArgumentSpacing,Generic.Functions.FunctionCallArgumentSpacing,PSR2.Classes.ClassDeclaration,Generic.Formatting.DisallowMultipleStatements,PSR1.Classes.ClassDeclaration,PSR1.Methods.CamelCapsMethodName,Squiz.Classes.ValidClassName,Squiz.Functions.FunctionDeclaration,PSR2.Methods.MethodDeclaration