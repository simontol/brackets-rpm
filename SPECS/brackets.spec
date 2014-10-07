Name: 		brackets	
Version: 	0.43
Release:	1%{?dist}
Summary: 	An open source code editor for the web, written in JavaScript, HTML and CSS.
#Group:		
License:	MIT
#URL:		
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
# git clone https://github.com/adobe/brackets.git
# cd brackets
# git checkout release-0.43
# git submodule update --init
# cd ..
# rm -rf brackets/.git
# tar -cvzf brackets-0.43.tar.gz brackets
Source0:	brackets-shell-%{version}.tar.gz
Source1:	brackets-%{version}.tar.gz

Requires:	nodejs,gtk2
BuildRequires:	npm,nspr,gyp

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
./node_modules/.bin/grunt clean less targethtml useminPrepare htmlmin requirejs concat copy usemin build-config

cd %{_builddir}/brackets-shell
npm install && npm install grunt-cli
./node_modules/.bin/grunt setup full-build

%install
mkdir --parents %{buildroot}%{_datadir}/%{name}
mkdir --parents %{buildroot}%{_bindir}
cp -a %{_builddir}/brackets-shell/out/Release/. %{buildroot}%{_datadir}/%{name}
cp -a %{_builddir}/brackets/dist/. %{buildroot}%{_datadir}/%{name}/www

ln -s %{_datadir}/%{name}/Brackets %{buildroot}%{_bindir}/%{name}

%files
%{_datadir}/%{name}/
%{_datadir}/%{name}/*
%attr(755, root, root) %{_bindir}/%{name}

%changelog



