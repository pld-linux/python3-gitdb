%define		module	gitdb
Summary:	Python git object database
Name:		python-%{module}
Version:	2.0.3
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	https://github.com/gitpython-developers/gitdb/archive/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	3554f89d04e55e6fcb9ac1103311cb3e
URL:		http://pypi.python.org/pypi/gitdb
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python-modules
Requires:	python-async >= 0.6.1
Requires:	python-smmap >= 0.8.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GitDB is a pure-Python git object database

%prep
%setup -q -n %{module}-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE
%dir %{py_sitescriptdir}/gitdb
%{py_sitescriptdir}/gitdb/*.py[co]
%dir %{py_sitescriptdir}/gitdb/db
%{py_sitescriptdir}/gitdb/db/*.py[co]
%dir %{py_sitescriptdir}/gitdb/utils
%{py_sitescriptdir}/gitdb/utils/*.py[co]
%dir %{py_sitescriptdir}/gitdb/test
%{py_sitescriptdir}/gitdb/test/*.py[co]
%{py_sitescriptdir}/gitdb2-*.egg-info
