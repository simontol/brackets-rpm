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
Source0:	brackets-%{version}.tar.gz
Source1:	brackets-shell-%{version}.tar.gz

BuildRequires:	npm,nspr,gyp
Requires:	nodejs,gtk+

%description

%prep
%setup -n brackets
%setup -T -D -b 1 -n brackets-shell

%build

npm install
#npm install --prefix brackets-shell

npm install grunt-cli

#./node_modules/.bin/grunt --gruntfile %{name}/Gruntfile.js clean less targethtml useminPrepare htmlmin requirejs concat copy usemin build-config
#./node_modules/.bin/grunt create-project build-www build
./node_modules/.bin/grunt setup full-build

%install
%make_install

%files
%doc

%changelog



