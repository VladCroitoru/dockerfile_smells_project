FROM heroku/cedar:14
RUN 	cd / ;\
	mkdir app ;\
	cd app ;\
	mkdir src ;\
	mkdir etc ;\
	cd src ;\
	git clone --depth=1 -b mono-4.2.3.4 https://github.com/mono/mono ;\
	cd mono ;\
	./configure.sh --prefix=/app --enable-nls=false --sysconfdir=/app/etc ;\
	make get-monolite-latest ;\
	make ;\
	make install ;\
