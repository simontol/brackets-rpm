[Brackets](https://github.com/adobe/brackets) rpm package, generated from the `.deb` package.

<a id="setup">

## Setup

</a>

Use `sudo` or `su -c` as your system requires:

1. Requires a library symlink:

   `ln -s /usr/lib64/libudev.so.1 /usr/lib64/libudev.so.0`
    
2. Install the package locally.  For example, with `yum`:

   `yum localinstall brackets-VERSION.x86_64.rpm`

## Usage

Run it using the `brackets` command.

Alternatively you can symlink the `.desktop` file so it will show up in the menu.

- For all users:

  `ln -s /opt/brackets/brackets.desktop /usr/share/applications/brackets.desktop`

- Or just for your user:

  `ln -s /opt/brackets/brackets.desktop ~/.local/share/applications/brackets.desktop`

## Conversion Process

### Short Version

1. `fakeroot alien -r brackets-VERSION.ARCH.deb`
2. `rpmrebuild -e -p brackets-VERSION.ARCH.rpm`
3. While editing spec file during above `rpmrebuild`, remove
    - `libcef` dependency
    - `/` path
    - `/opt` path
    - `/usr` path
    - `/usr/bin` path
    - `/usr/share` path
        
### Details

The `.rpm` can be built from the `.deb` using `alien` and `rpmrebuild`:

`alien` should be run with `fakeroot` so it can properly allocate file permissions.

    fakeroot alien -r brackets-VERSION.ARCH.deb

After `alien` finishes building the `brackets-VERSION.ARCH.rpm`, run `rpmrebuild` to tune the package. 
This command will open an RPM spec file:

    rpmrebuild -e -p brackets-VERSION.ARCH.rpm

Make the following changes:

1. Scroll to the dependency section (full of `Provides: ...` and `Requires: ...` lines).

   Remove the dependency for `libcef` by deleting the `Requires:` line(s) that contain `libcef`

2. Scroll to the `%files` section and remove conflicts with the filesystem.

   Most of the paths will be `brackets`-specific, but lines with paths like these should be removed:

   - `/`
   - `/opt`
   - `/usr`
   - `/usr/bin`
   - `/usr/share`

   Leave the paths that contain subdirectories of those paths, just remove the base filesystem directories.
   Get the full list of filesystem paths with `repoquery -l filesystem`.

After editing the spec file, the (still-running) `rpmrebuild` command should prompt `continue ? (y/N)`. Enter `y`.

When the `rpmrebuild` process completes, the default behaviour is not to rewrite the input `.rpm`, but to output a new `.rpm`.
The new `.rpm` is located as the `rpmrebuild` output line starting with `result:` indicates.

If you made the correct modifications to the RPM spec file, you should now be able to install brackets by following the [setup](#setup) section with the new `.rpm`.
