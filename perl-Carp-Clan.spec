%define	upstream_name	 Carp-Clan
%define	upstream_version 6.08

%define TEST	1
%{?_with_test:	%{expand:	%%global TEST 1}}
%{?_without_test:	%{expand:	%%global TEST 0}}

Summary:	%{upstream_name} module for perl
Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/karenetheridge/Carp-Clan
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/Carp-Clan-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::Exception)

%description
%{upstream_name} module for perl.
This module reports errors from the perspective of the caller of a
"clan" of modules, similar to "Carp.pm" itself. But instead of giving
it a number of levels to skip on the calling stack, you give it a
pattern to characterize the package names of the "clan" of modules
which shall never be blamed for any error.

%prep
%setup -qn %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%if %{TEST}
LANG=C %make test
%endif

%install
%makeinstall_std

%files
%{perl_vendorlib}/Carp
%{_mandir}/man3/*

