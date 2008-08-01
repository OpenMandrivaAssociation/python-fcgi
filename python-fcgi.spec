Name:           python-fcgi
Version:        2000.09.21
Release:        %mkrel 4
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

