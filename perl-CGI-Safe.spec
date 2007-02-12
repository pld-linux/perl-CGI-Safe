#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Safe
Summary:	CGI::Safe - safe method of using CGI.pm
Summary(pl.UTF-8):   CGI::Safe - bezpieczny sposób używania CGI.pm
Name:		perl-CGI-Safe
Version:	1.25
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	67e055249e96845adc8858bee0bba785
%{?with_tests:BuildRequires:	perl-CGI >= 2.20}
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-CGI >= 2.20
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module makes running the CGI environment safer by eliminating
dangerous %%ENV variables and presetting certain CGI.pm globals (such
as disabling uploads by default and limiting POST data size).

%description -l pl.UTF-8
Ten moduł czyni uruchamianie środowiska CGI bezpieczniejszym poprzez
usuwanie niebezpiecznych zmiennych z %%ENV i ustawianie kilku
zmiennych globalnych CGI.pm (takich jak domyślne wyłączenie
przysyłania danych czy ograniczenie rozmiaru danych POST).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/Safe.pm
%{_mandir}/man3/*
