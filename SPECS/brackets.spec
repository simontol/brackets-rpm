Name:           brackets
Version:        1.0
Release:        1%{?dist}
Summary:        An open source code editor for the web, written in JavaScript, HTML and CSS.
Group:          Development/Tools
License:        MIT
URL:            http://brackets.io/

# The sources for this package were pulled from upstream's vcs.
# Use the fetch_source.sh to download them.
Source0:        brackets-shell-%{version}.tar.gz
Source1:        brackets-%{version}.tar.gz

Requires:       nodejs, gtk2, alsa-lib, GConf2, libgcrypt
BuildRequires:  %{requires}, gtk2-devel, npm, nspr, gyp, desktop-file-utils

AutoReqProv:    no

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%description

%prep

%setup -n brackets-shell
%setup -T -D -b 1 -n brackets

%build

%ifarch x86_64
LD_PRELOAD=/usr/lib64/libudev.so.1
%else
LD_PRELOAD=/usr/lib/libudev.so.1
%endif

cd %{_builddir}/brackets
npm install && npm install grunt-cli
./node_modules/.bin/grunt clean less targethtml useminPrepare htmlmin requirejs concat copy usemin
cp -a src/config.json dist/config.json

cd %{_builddir}/brackets-shell
npm install && npm install grunt-cli
./node_modules/.bin/grunt setup full-build

%install

mkdir --parents %{buildroot}%{_datadir}/%{name}
cp -a %{_builddir}/brackets-shell/installer/linux/debian/package-root/opt/brackets/. %{buildroot}%{_datadir}/%{name}
cp -a %{_builddir}/brackets-shell/installer/linux/debian/package-root/usr/share/icons %{buildroot}%{_datadir}/

mkdir --parents %{buildroot}%{_bindir}
ln -sf %{_datadir}/%{name}/brackets %{buildroot}%{_bindir}/%{name}

mkdir --parents %{buildroot}%{_datadir}/applications
cat <<EOT >> %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=Brackets
Type=Application
Categories=Development
Exec=brackets %U
Icon=brackets
MimeType=text/html;
Keywords=Text;Editor;Write;Web;Development;
EOT

desktop-file-install --mode 0644 %{buildroot}%{_datadir}/applications/%{name}.desktop

%ifarch x86_64
ln -sf /usr/lib64/libudev.so.1 %{buildroot}%{_datadir}/%{name}/libudev.so.0
%else
ln -sf /usr/lib/libudev.so.1 %{buildroot}%{_datadir}/%{name}/libudev.so.0
%endif

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
/usr/bin/update-desktop-database &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
/usr/bin/update-desktop-database &> /dev/null || :

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files

%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/*/*/*/*.svg
%attr(755, root, root) %{_datadir}/%{name}/brackets
%attr(755, root, root) %{_datadir}/%{name}/Brackets
%attr(755, root, root) %{_datadir}/%{name}/Brackets-node
%attr(755, root, root) %{_bindir}/%{name}

%changelog
