%define 	module	gitdb
Summary:	Python git object database
Name:		python-%{module}
Version:	0.6.0
Release:	2
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pypi.python.org/packages/source/g/gitdb/%{module}-%{version}.tar.gz
# Source0-md5:	fbd7d617e208e8d8029beeb09a18f845
URL:		http://pypi.python.org/pypi/gitdb
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-modules
Requires:	python-async >= 0.6.1
Requires:	python-smmap >= 0.8.0
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
%dir %{py_sitedir}/gitdb
%{py_sitedir}/gitdb/*.py[co]
%attr(755,root,root) %{py_sitedir}/gitdb/*.so
%dir %{py_sitedir}/gitdb/db
%{py_sitedir}/gitdb/db/*.py[co]
%dir %{py_sitedir}/gitdb/utils
%{py_sitedir}/gitdb/utils/*.py[co]
%{py_sitedir}/gitdb-*.egg-info
