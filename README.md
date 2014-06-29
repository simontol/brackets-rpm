[Brackets](https://github.com/adobe/brackets) rpm package, generated from the deb.

<a id="setup">

## Setup

</a>

Requires a library symlink:

    ln -s /usr/lib64/libudev.so.1 /usr/lib64/libudev.so.0
    
Install the package locally.  For example, with `yum`:

    yum localinstall brackets-VERSION.x86_64.rpm

Use `sudo` or `su -c` as your system requires.

## Usage

Run it using the `brackets` command.

Alternatively you can symlink the `.desktop` file so it will show up in the menu:

    // for all users
    ln -s /opt/brackets/brackets.desktop /usr/share/applications/brackets.desktop

    // OR just for your user
    ln -s /opt/brackets/brackets.desktop ~/.local/share/applications/brackets.desktop

## Conversion Process

### Short Version

1. `fakeroot alien -r brackets-VERSION.ARCH.deb`
2. `rpmrebuild -e -p brackets-VERSION.ARCH.rpm
3. While editing spec file during `rpmrebuild`, remove
    - `libcef` dependency
    - `/` path
    - `/opt` path
    - `/usr` path
    - `/usr/bin` path
    - `/usr/share` path
        
### Details

The `.rpm` can be built from the `.deb` using `alien` and `rpmrebuild`:

Alien should be run with `fakeroot` so it can properly allocate file permissions.

    fakeroot alien -r brackets-VERSION.ARCH.deb

After `alien` finishes building the `brackets-VERSION.ARCH.deb`, run rpmrebuild to tune the package. 
This command will open an RPM spec file:

    rpmrebuild -e -p brackets-VERSION.ARCH.rpm

Make the following changes:

1. Scroll to the dependency section and remove the dependency for `libcef` (Chromium Embedded Framework) by deleting `Requires:` lines that contain `libcef`
2. Scroll to the `%files` section and remove conflicts with the filesystem.
   Most of the paths should be `brackets`-specific, but there will likely be a few lines at the bottom and the top of the list with paths
   - `/`
   - `/opt`
   - `/usr`
   - `/usr/bin`
   - `/usr/share`
   Remove lines containing those paths.
   (Get the full list of filesystem paths with `repoquery -l filesystem`.)

`rpmrebuild` should prompt `continue ? (y/N)`, enter `y`.

When the process completes, a *new `.rpm` will be created.*
The default behaviour is not to rewrite the input `.rpm`, but to output a new `.rpm` where the `rpmrebuild` output line starting with "`result:`" indicates.

If you made the correct modifications to the RPM spec file, you should now be able to install brackets by following the [setup](#setup) section with the new `.rpm`.
