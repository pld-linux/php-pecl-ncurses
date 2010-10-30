%define		_modname	ncurses
%define		_status		stable
Summary:	%{_modname} - Terminal screen handling and optimization package
Summary(pl.UTF-8):	%{_modname} - pakiet obsługi i optymalizacji terminala
Name:		php-pecl-%{_modname}
Version:	1.0.1
Release:	1
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	a2ec4437449f9b36bf3cba7a59a37654
Patch0:		%{name}-php52.patch
URL:		http://pecl.php.net/package/ncurses/
BuildRequires:	ncurses-ext-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
%{?requires_php_extension}
Requires:	php-common >= 4:5.0.4
Obsoletes:	php-ncurses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds support for ncurses functions (only for cli SAPI).

In PECL status of this extension is: %{_status}.

%description -l pl.UTF-8
Ten moduł dodaje obsługę funkcji ncurses (tylko do SAPI cli).

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c
%patch -p0

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/cli.d

%{__make} -C %{_modname}-%{version} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT \
	EXTENSION_DIR=%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/cli.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/cli.d/%{_modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{_modname}.so