brackets-rpm
============

This is a rpm package generated from the debian package of the wondeful [Brackets Editor](https://github.com/adobe/brackets).

Before running it, you have to create some symlinks:

	ln -s /usr/lib64/libudev.so.1 /usr/lib64/libudev.so.0
	ln -s /usr/lib64/libplc4.so /usr/lib64/libplc4.so.0d
	ln -s /usr/lib64/libnspr4.so /usr/lib64/libnspr4.so.0d

I used alien to convert the debian package and rpmrebuild to apply two small changes (I had to remove cef from deps and fix a filesystem conflict). I don't have any idea how to build a "real" package but this seems to work.

