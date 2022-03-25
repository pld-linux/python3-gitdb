#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (needs git checkout, not archive?)

%define		module	gitdb
Summary:	GitDB - pure-Python git object database
Summary(pl.UTF-8):	GitDB - czysto pythonowa baza danych obiektów gita
Name:		python-%{module}
Version:	4.0.9
Release:	2
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://github.com/gitpython-developers/gitdb/releases
Source0:	https://github.com/gitpython-developers/gitdb/archive/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	2f3e4166f6cd72e7946202d1f1144f29
URL:		https://github.com/gitpython-developers/gitdb
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-smmap >= 2.0.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-smmap >= 2.0.0
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GitDB allows you to access bare git repositories for reading and
writing. It aims at allowing full access to loose objects as well as
packs with performance and scalability in mind. It operates
exclusively on streams, allowing to handle large objects with a small
memory footprint.

%description -l pl.UTF-8
GitDB pozwala na dostęp do gołych repozytoriów gita do odczytu i
zapisu. Celem jest umożliwienie pełnego dostępu do luźnych obiektów,
jak i paczek z myślą o wydajności i skalowalności. Operuje wyłącznie
na strumieniach, pozwalając na obsługę dużych obiektów przy niewielkim
narzucie czasu.

%package -n python3-%{module}
Summary:	GitDB - pure-Python git object database
Summary(pl.UTF-8):	GitDB - czysto pythonowa baza danych obiektów gita
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
GitDB allows you to access bare git repositories for reading and
writing. It aims at allowing full access to loose objects as well as
packs with performance and scalability in mind. It operates
exclusively on streams, allowing to handle large objects with a small
memory footprint.

%description -n python3-%{module} -l pl.UTF-8
GitDB pozwala na dostęp do gołych repozytoriów gita do odczytu i
zapisu. Celem jest umożliwienie pełnego dostępu do luźnych obiektów,
jak i paczek z myślą o wydajności i skalowalności. Operuje wyłącznie
na strumieniach, pozwalając na obsługę dużych obiektów przy niewielkim
narzucie czasu.

%package apidocs
Summary:	API documentation for GitDB module
Summary(pl.UTF-8):	Dokumentacja API modułu GitDB
Group:		Documentation

%description apidocs
API documentation for GitDB module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu GitDB.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/gitdb/test

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/gitdb/test
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.rst
%dir %{py_sitescriptdir}/gitdb
%{py_sitescriptdir}/gitdb/*.py[co]
%{py_sitescriptdir}/gitdb/db
%{py_sitescriptdir}/gitdb/utils
%{py_sitescriptdir}/gitdb*-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.rst
%dir %{py3_sitescriptdir}/gitdb
%{py3_sitescriptdir}/gitdb/*.py
%{py3_sitescriptdir}/gitdb/db
%{py3_sitescriptdir}/gitdb/utils
%{py3_sitescriptdir}/gitdb/__pycache__
%{py3_sitescriptdir}/gitdb*-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,*.html,*.js}
%endif
