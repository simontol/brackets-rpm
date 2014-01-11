[Brackets](https://github.com/adobe/brackets) rpm package, generated from the deb.

Requires a symlink:

    ln -s /usr/lib64/libudev.so.1 /usr/lib64/libudev.so.0
    
Run it using the `brackets` command. Alternatively you could symlink the `.desktop` file so it will show up in the menu:

```
ln -s /opt/brackets/brackets.desktop /usr/share/applications/brackets.desktop
// OR just for your user
ln -s /opt/brackets/brackets.desktop ~/.local/share/applications/brackets.desktop
```

I built this using `alien` and `rpmrebuild`:

    alien -r brackets-sprint-34-LINUX64.deb
    rpmrebuild -e -p brackets-0.34.1-10734.x86_64.rpm

Then I removed the dependency to libcef and all paths that conflict with the filesystem (like `/`, `/usr` etc, run `repoquery -l filesystem` to get the full list).
