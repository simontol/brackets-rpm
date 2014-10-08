Name: 		brackets	
Version: 	0.44
Release:	2%{?dist}
Summary: 	An open source code editor for the web, written in JavaScript, HTML and CSS.
#Group:		
License:	MIT
URL:		http://brackets.io/
# The sources for this package were pulled from upstream's vcs.
# Use the fetch_source.sh to download them.
Source0:	brackets-shell-%{version}.tar.gz
Source1:	brackets-%{version}.tar.gz

Requires:	nodejs,gtk2
BuildRequires:	gtk2-devel,npm,nspr,gyp

AutoReqProv: no

%global _enable_debug_package 0
%global debug_package %{nil}
%global __os_install_post /usr/lib/rpm/brp-compress %{nil}

%description

%prep

%setup -n brackets-shell
%setup -T -D -b 1 -n brackets

%build

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

mkdir --parents %{buildroot}%{_bindir}
ln -sf %{_datadir}/%{name}/brackets %{buildroot}%{_bindir}/%{name}

# set permissions on subdirectories
find %{buildroot}%{_datadir}/%{name} -type d -exec chmod 755 {} \;

%ifarch x86
ln -sf /usr/lib/libudev.so.1 %{buildroot}%{_datadir}/%{name}/libudev.so.0
%endif
%ifarch x86_64
ln -sf /usr/lib64/libudev.so.1 %{buildroot}%{_datadir}/%{name}/libudev.so.0
%endif

%files

%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/*
%attr(755, root, root) %{_datadir}/%{name}/brackets
%attr(755, root, root) %{_datadir}/%{name}/Brackets
%attr(755, root, root) %{_datadir}/%{name}/Brackets-node
%attr(755, root, root) %{_bindir}/%{name}

%changelog



