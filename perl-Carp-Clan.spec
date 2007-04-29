%define	module	Carp-Clan

%define	version	5.9

%define	release	%mkrel 1

%define	pdir	Carp

%define TEST	1
%{?_with_test: %{expand: %%global TEST 1}}
%{?_without_test: %{expand: %%global TEST 0}}

Summary: 	%{module} module for perl
Name: 		perl-%{module}
Version: 	%{version}
Release:	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:  perl(Test::Exception)
BuildArch:	noarch

%description
%{module} module for perl.
This module reports errors from the perspective of the caller of a
"clan" of modules, similar to "Carp.pm" itself. But instead of giving
it a number of levels to skip on the calling stack, you give it a
pattern to characterize the package names of the "clan" of modules
which shall never be blamed for any error.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%if %{TEST}
LANG=C %make test
%endif

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%{_mandir}/*/*
%{perl_vendorlib}/%{pdir}

