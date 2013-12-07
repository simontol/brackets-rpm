[Brackets](https://github.com/adobe/brackets) rpm package, generated from the deb.

Requires a symlink:

    ln -s /usr/lib64/libudev.so.1 /usr/lib64/libudev.so.0

For the older sprint 29, you might also need these:

    ln -s /usr/lib64/libplc4.so /usr/lib64/libplc4.so.0d
    ln -s /usr/lib64/libnspr4.so /usr/lib64/libnspr4.so.0d

I built this using `alien` and `rpmrebuild`:

    alien -r brackets-sprint-34-LINUX64.deb
    rpmrebuild -e -p brackets-0.34.1-10734.x86_64.rpm

Then I removed the dependency to libcef and all paths that conflict with the filesystem (like `/`, `/usr` etc).