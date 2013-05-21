%define	upstream_name	 Carp-Clan
%define	upstream_version 6.04

%define TEST	1
%{?_with_test: %{expand: %%global TEST 1}}
%{?_without_test: %{expand: %%global TEST 0}}

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	%{upstream_name} module for perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Carp/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Exception)

BuildArch:	noarch

%description
%{upstream_name} module for perl.
This module reports errors from the perspective of the caller of a
"clan" of modules, similar to "Carp.pm" itself. But instead of giving
it a number of levels to skip on the calling stack, you give it a
pattern to characterize the package names of the "clan" of modules
which shall never be blamed for any error.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%defattr(644,root,root,755)
%{_mandir}/*/*
%{perl_vendorlib}/Carp


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.40.0-5mdv2012.0
+ Revision: 765080
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.40.0-4
+ Revision: 763496
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 6.40.0-3
+ Revision: 667039
- mass rebuild

* Thu Jul 22 2010 Funda Wang <fwang@mandriva.org> 6.40.0-2mdv2011.0
+ Revision: 557003
- rebuild

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 6.40.0-1mdv2010.1
+ Revision: 460720
- update to 6.04

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 6.00-4mdv2010.0
+ Revision: 426423
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 6.00-3mdv2009.1
+ Revision: 351682
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 6.00-2mdv2009.0
+ Revision: 223571
- rebuild

* Wed Feb 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 6.00-1mdv2008.1
+ Revision: 173265
- update to new version 6.00

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 29 2007 Nicolas LÃ©cureuil <nlecureuil@mandriva.com> 5.9-1mdv2008.0
+ Revision: 19293
-New version


* Sat Jun 17 2006 Scott Karns <scottk@mandriva.org> 5.3-3mdv2007.0
- Updated spec to comply with Mandriva perl packaging policies

* Sat Jun 04 2005 Luca Berra <bluca@vodka.it> 5.3-2mdk 
- rebuild

* Wed May 05 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 5.3-1mdk
- 5.3

* Wed Apr 21 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 5.2-1mdk
- 5.2
- drop $RPM_OPT_FLAGS, noarch..

* Thu Feb 12 2004 Luca Berra <bluca@vodka.it> 5.1-3mdk
- rebuild for perl 5.8.3

* Tue Dec 30 2003 Luca Berra <bluca@vodka.it> 5.1-2mdk
- add parent dirs (distriblint)

* Sun Oct 05 2003 Luca Berra <bluca@vodka.it> 5.1-1mdk
- Initial build.

