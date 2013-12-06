%define	upstream_name	 Carp-Clan
%define	upstream_version 6.04

%define TEST	1
%{?_with_test:	%{expand:	%%global TEST 1}}
%{?_without_test:	%{expand:	%%global TEST 0}}

Summary:	%{upstream_name} module for perl
Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	11
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Carp/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
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

