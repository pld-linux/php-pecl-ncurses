%define		php_name	php%{?php_suffix}
%define		modname	ncurses
%define		status		stable
Summary:	%{modname} - Terminal screen handling and optimization package
Summary(pl.UTF-8):	%{modname} - pakiet obsługi i optymalizacji terminala
Name:		%{php_name}-pecl-%{modname}
Version:	1.0.2
Release:	5
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	a466d1b3e556cda67274ba6c36239c48
Patch0:		php-pecl-%{modname}-php52.patch
URL:		http://pecl.php.net/package/ncurses/
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	ncurses-ext-devel
BuildRequires:	rpmbuild(macros) >= 1.650
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Provides:	php(%{modname}) = %{version}
Obsoletes:	php-ncurses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module adds support for ncurses functions (only for cli SAPI).

In PECL status of this extension is: %{status}.

%description -l pl.UTF-8
Ten moduł dodaje obsługę funkcji ncurses (tylko do SAPI cli).

To rozszerzenie ma w PECL status: %{status}.

%prep
%setup -qc
mv %{modname}-%{version}/* .
%patch0 -p1

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_sysconfdir}/cli.d
%{__make} install \
	EXTENSION_DIR=%{php_extensiondir} \
	INSTALL_ROOT=$RPM_BUILD_ROOT
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/cli.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/cli.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
