Name:           python-fcgi
Version:        2000.09.21
Release:        8
Epoch:          0
Summary:        Python FastCGI Module

Group:          Development/Python
License:        BSD
URL:            http://alldunn.com/python/
Source0:        http://alldunn.com/python/fcgi.py
BuildRequires:  python-devel
BuildArch:      noarch

%description
The fcgi.py Python module handles communication with the FastCGI module
from the Apache or Stronghold web server without using the FastCGI
developers kit. It will also work in a non-FastCGI environment,
(straight CGI).

%prep

%build

%install
%{__mkdir_p} %{buildroot}%{py_puresitedir}
%{__install} -m 0755 %{SOURCE0} %{buildroot}%{py_puresitedir}/
python %{_libdir}/python%{py_ver}/compileall.py -d %{py_puresitedir}/ %{buildroot}%{py_puresitedir}

%clean

%files
%defattr(-,root,root,0755)
%{py_puresitedir}/fcgi.py*



