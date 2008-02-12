%define         _class          HTML
%define         _subclass       Progress2
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

%define _requires_exceptions	pear(Smarty.class.php)\\|pear(HTML/Progress2/Observer.php)\\|pear(PHPUnit.php)

Summary:	%{_pearname} - How to include a loading bar in your XHTML documents quickly and easily
Name:		php-pear-%{_pearname}
Version:	2.2.0
Release:	%mkrel 3
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Progress2
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-smarty
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This package provides a way to add a loading bar fully customizable in existing
XHTML documents.
Your browser should accept DHTML feature.

Features:
- create horizontal, vertival bar and also circle, ellipse and polygons
  (square, rectangle).
- allows usage of existing external StyleSheet and/or JavaScript.
- all elements (progress, cells, labels) are customizable by their html
  properties.
- percent/labels are floating all around the progress meter.
- compliant with all CSS/XHMTL standards.
- integration with all template engines is very easy.
- implements Observer design pattern. It is possible to add Listeners.
- adds a customizable monitor pattern to display a progress bar.
  User-end can abort progress at any time.
- allows many progress meter on same page without uses of iframe solution.
- error handling system that support native PEAR_Error, but also
  PEAR_ErrorStack, and any other system you might want to plug-in.
- PHP 5 ready.

This class has in PEAR status: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Generator

install -m0644 %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}
install -m0644 %{_pearname}-%{version}/%{_subclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}
install -m0644 %{_pearname}-%{version}/%{_subclass}/Generator/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}/Generator

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{ChangeLog,NEWS,docs,examples,tests}
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/packages/%{_pearname}.xml
