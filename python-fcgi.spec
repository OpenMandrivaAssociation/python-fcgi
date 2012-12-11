Name:           python-fcgi
Version:        2000.09.21
Release:        %mkrel 7
Epoch:          0
Summary:        Python FastCGI Module
Group:          Development/Python
License:        BSD
URL:            http://alldunn.com/python/
Source0:        http://alldunn.com/python/fcgi.py
%py_requires -d
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The fcgi.py Python module handles communication with the FastCGI module
from the Apache or Stronghold web server without using the FastCGI
developers kit. It will also work in a non-FastCGI environment,
(straight CGI).

%prep

%build

%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{python_sitelib}
%{__install} -m 0755 %{SOURCE0} %{buildroot}%{python_sitelib}/
%{__python} %{_libdir}/python%{python_version}/compileall.py -d %{python_sitelib}/ %{buildroot}%{python_sitelib}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%{python_sitelib}/fcgi.py*



%changelog
* Sat Nov 06 2010 Funda Wang <fwang@mandriva.org> 0:2000.09.21-7mdv2011.0
+ Revision: 593930
- rebuild for py2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0:2000.09.21-6mdv2010.0
+ Revision: 442107
- rebuild

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0:2000.09.21-5mdv2009.1
+ Revision: 323704
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0:2000.09.21-4mdv2009.0
+ Revision: 259602
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0:2000.09.21-3mdv2009.0
+ Revision: 247411
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Oct 29 2007 David Walluck <walluck@mandriva.org> 0:2000.09.21-1mdv2008.1
+ Revision: 103620
- import python-fcgi


