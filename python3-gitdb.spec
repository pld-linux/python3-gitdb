#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (needs git checkout, not archive?)

%define		module	gitdb
Summary:	GitDB - pure-Python git object database
Summary(pl.UTF-8):	GitDB - czysto pythonowa baza danych obiektów gita
Name:		python3-%{module}
Version:	4.0.10
Release:	3
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://github.com/gitpython-developers/gitdb/tags
Source0:	https://github.com/gitpython-developers/gitdb/archive/%{version}/%{module}-%{version}.tar.gz
# Source0-md5:	9fab50d0b256a305ff0371433e15f211
URL:		https://github.com/gitpython-developers/gitdb
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-smmap >= 3.0.1
BuildRequires:	python3-smmap < 6
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python3-modules >= 1:3.6
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
%py3_build %{?with_tests:test}

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/gitdb/test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.rst
%dir %{py3_sitescriptdir}/gitdb
%{py3_sitescriptdir}/gitdb/*.py
%{py3_sitescriptdir}/gitdb/db
%{py3_sitescriptdir}/gitdb/utils
%{py3_sitescriptdir}/gitdb/__pycache__
%{py3_sitescriptdir}/gitdb-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,*.html,*.js}
%endif
