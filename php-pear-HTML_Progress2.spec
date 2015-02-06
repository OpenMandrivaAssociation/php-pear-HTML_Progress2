%define         _class          HTML
%define         _subclass       Progress2
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	2.4.1
Release:	9
Summary:	How to include a loading bar in your XHTML documents quickly and easily
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Progress2
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
Requires:	php-smarty
BuildArch:	noarch
BuildRequires:	php-pear

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

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/ChangeLog
%doc %{upstream_name}-%{version}/NEWS
%doc %{upstream_name}-%{version}/docs
%doc %{upstream_name}-%{version}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4.1-7mdv2012.0
+ Revision: 741996
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 2.4.1-6
+ Revision: 679347
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 2.4.1-5mdv2011.0
+ Revision: 613673
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.1-4mdv2010.1
+ Revision: 477870
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 2.4.1-3mdv2010.0
+ Revision: 441120
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 2.4.1-2mdv2009.1
+ Revision: 322115
- rebuild

* Tue Sep 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 2.4.1-1mdv2009.0
+ Revision: 278918
- update to new version 2.4.1

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-4mdv2009.0
+ Revision: 236874
- rebuild

* Tue Feb 12 2008 Thierry Vignaud <tv@mandriva.org> 2.2.0-3mdv2008.1
+ Revision: 166718
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Aug 31 2007 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-3mdv2008.0
+ Revision: 76964
- fix deps

* Fri Apr 20 2007 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-2mdv2008.0
+ Revision: 15465
- rule out the PHPUnit.php dep


* Sat Mar 10 2007 Oden Eriksson <oeriksson@mandriva.com> 2.2.0-1mdv2007.1
+ Revision: 140467
- 2.2.0
- fix deps

* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-2mdv2007.1
+ Revision: 81633
- Import php-pear-HTML_Progress2

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-2mdk
- new group (Development/PHP)

* Mon Nov 07 2005 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-1mdk
- initial Mandriva package

