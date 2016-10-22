%{?scl:%scl_package perl-Module-Build}

%global cpan_version_major 0.42
%global cpan_version_minor 18
%global cpan_version %{cpan_version_major}%{?cpan_version_minor}

Name:           %{?scl_prefix}perl-Module-Build
Epoch:          2
Version:        %{cpan_version_major}%{?cpan_version_minor:.%cpan_version_minor}
Release:        5%{?dist}
Summary:        Build and install Perl modules
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Module-Build/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/Module-Build-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  %{?scl_prefix}perl
BuildRequires:  %{?scl_prefix}perl-devel
BuildRequires:  %{?scl_prefix}perl-generators
BuildRequires:  %{?scl_prefix}perl(Archive::Tar)
BuildRequires:  %{?scl_prefix}perl(AutoSplit)
BuildRequires:  %{?scl_prefix}perl(base)
BuildRequires:  %{?scl_prefix}perl(Carp)
BuildRequires:  %{?scl_prefix}perl(Config)
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta) >= 2.142060
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::Converter) >= 2.141170
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::Merge)
BuildRequires:  %{?scl_prefix}perl(CPAN::Meta::YAML) >= 0.003
BuildRequires:  %{?scl_prefix}perl(Cwd)
BuildRequires:  %{?scl_prefix}perl(Data::Dumper)
BuildRequires:  %{?scl_prefix}perl(deprecate)
BuildRequires:  %{?scl_prefix}perl(DynaLoader)
BuildRequires:  %{?scl_prefix}perl(Exporter)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Install) >= 0.3
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Installed)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Manifest) >= 1.54
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Mkbootstrap)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::Packlist)
BuildRequires:  %{?scl_prefix}perl(ExtUtils::ParseXS) >= 2.21
BuildRequires:  %{?scl_prefix}perl(File::Basename)
BuildRequires:  %{?scl_prefix}perl(File::Compare)
BuildRequires:  %{?scl_prefix}perl(File::Copy)
BuildRequires:  %{?scl_prefix}perl(File::Find)
BuildRequires:  %{?scl_prefix}perl(File::Path)
BuildRequires:  %{?scl_prefix}perl(File::Spec) >= 0.82
BuildRequires:  %{?scl_prefix}perl(File::Spec::Functions)
BuildRequires:  %{?scl_prefix}perl(File::Temp) >= 0.15
BuildRequires:  %{?scl_prefix}perl(Getopt::Long)
BuildRequires:  %{?scl_prefix}perl(if)
BuildRequires:  %{?scl_prefix}perl(inc::latest)
BuildRequires:  %{?scl_prefix}perl(lib)
# perl(Module::Build) is loaded from ./lib
BuildRequires:  %{?scl_prefix}perl(Module::Metadata) >= 1.000002
BuildRequires:  %{?scl_prefix}perl(Parse::CPAN::Meta) >= 1.4401
BuildRequires:  %{?scl_prefix}perl(Perl::OSType) >= 1
BuildRequires:  %{?scl_prefix}perl(strict)
# Optional tests:
%if !%{defined perl_bootstrap} && !%{defined perl_small}
BuildRequires:  %{?scl_prefix}perl(Archive::Zip)
BuildRequires:  %{?scl_prefix}perl(File::ShareDir) >= 1.00
BuildRequires:  %{?scl_prefix}perl(PAR::Dist)
BuildRequires:  %{?scl_prefix}perl(Pod::Readme)
%endif
BuildRequires:  %{?scl_prefix}perl(TAP::Harness)
BuildRequires:  %{?scl_prefix}perl(TAP::Harness::Env)
BuildRequires:  %{?scl_prefix}perl(Test::Harness) >= 3.29
BuildRequires:  %{?scl_prefix}perl(Test::More) >= 0.49
BuildRequires:  %{?scl_prefix}perl(Text::ParseWords)
BuildRequires:  %{?scl_prefix}perl(utf8)
BuildRequires:  %{?scl_prefix}perl(vars)
BuildRequires:  %{?scl_prefix}perl(version) >= 0.87
BuildRequires:  %{?scl_prefix}perl(warnings)
Requires:       %{?scl_prefix}perl(:MODULE_COMPAT_%(%{?scl:scl enable %{scl} '}eval "$(perl -V:version)";echo $version%{?scl:'}))
Requires:       %{?scl_prefix}perl(CPAN::Meta) >= 2.142060
Requires:       %{?scl_prefix}perl(CPAN::Meta::Converter) >= 2.141170
Requires:       %{?scl_prefix}perl(CPAN::Meta::Merge)
Requires:       %{?scl_prefix}perl(ExtUtils::CBuilder) >= 0.27
Requires:       %{?scl_prefix}perl(ExtUtils::Install) >= 0.3
Requires:       %{?scl_prefix}perl(ExtUtils::Manifest) >= 1.54
Requires:       %{?scl_prefix}perl(ExtUtils::Mkbootstrap)
Requires:       %{?scl_prefix}perl(ExtUtils::ParseXS) >= 2.21
Requires:       %{?scl_prefix}perl(inc::latest)
Requires:       %{?scl_prefix}perl(Module::Metadata) >= 1.000002
# Keep PAR support optional (PAR::Dist)
Requires:       %{?scl_prefix}perl(Perl::OSType) >= 1
Requires:       %{?scl_prefix}perl(TAP::Harness::Env)
Requires:       %{?scl_prefix}perl(Test::Harness)
%if !%{defined perl_bootstrap}
# Optional run-time needed for Software::License license identifier,
# bug #1152319
Requires:       %{?scl_prefix}perl(Software::License)
%endif
# Optional run-time needed for generating documentation from POD:
Requires:       %{?scl_prefix}perl(Pod::Html)
Requires:       %{?scl_prefix}perl(Pod::Man) >= 2.17
Requires:       %{?scl_prefix}perl(Pod::Text)
# Run-time for generated Build scripts from Build.PLs:
# Those are already found by dependency generator. Just make sure they
# present.
# Cwd
# File::Basename
# File::Spec
# strict

%{?perl_default_filter}
# Remove under-specified dependencies
%if 0%{?rhel} < 7
# RPM 4.8 style
%{?filter_setup:
%filter_from_requires /^%{?scl_prefix}perl(ExtUtils::Install)$/d
%filter_from_requires /^%{?scl_prefix}perl(File::Spec)$/d
%filter_from_requires /^%{?scl_prefix}perl(Module::Build)$/d
%filter_from_requires /^%{?scl_prefix}perl(Module::Metadata)$/d
%filter_from_requires /^%{?scl_prefix}perl(Perl::OSType)$/d
%filter_from_requires /^%{?scl_prefix}perl(CPAN::Meta::YAML) >= 0.002$/d
%?perl_default_filter
}
%else
# RPM 4.9 style
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^%{?scl_prefix}perl\\((ExtUtils::Install|File::Spec|Module::Build|Module::Metadata|Perl::OSType)\\)$
%global __requires_exclude %__requires_exclude|^%{?scl_prefix}perl\\(CPAN::Meta::YAML\\) >= 0.002$
%endif

%description
Module::Build is a system for building, testing, and installing Perl
modules. It is meant to be an alternative to ExtUtils::MakeMaker.
Developers may alter the behavior of the module through sub-classing in a
much more straightforward way than with MakeMaker. It also does not require
a make on your system - most of the Module::Build code is pure-perl and
written in a very cross-platform way. In fact, you don't even need a shell,
so even platforms like MacOS (traditional) can use it fairly easily. Its
only prerequisites are modules that are included with perl 5.6.0, and it
works fine on perl 5.005 if you can install a few additional modules.

%prep
%setup -q -n Module-Build-%{cpan_version}

%build
%{?scl:scl enable %{scl} '}perl Build.PL installdirs=vendor && ./Build%{?scl:'}

%install
%{?scl:scl enable %{scl} '}./Build install destdir=%{buildroot} create_packlist=0%{?scl:'}
%{_fixperms} %{buildroot}/*

%check
rm t/signature.t
LANG=C TEST_SIGNATURE=1 MB_TEST_EXPERIMENTAL=1 %{?scl:scl enable %{scl} '}./Build test%{?scl:'}

%files
%doc LICENSE
%doc Changes contrib README
%{_bindir}/config_data
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
* Sun Jul 24 2016 Petr Pisar <ppisar@redhat.com> - 2:0.42.18-5
- Rebuild without bootstrap

* Tue Jul 12 2016 Petr Pisar <ppisar@redhat.com> - 2:0.42.18-4
- SCL

* Wed May 18 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.18-3
- Perl 5.24 re-rebuild of bootstrapped packages

* Sat May 14 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.18-2
- Perl 5.24 rebuild

* Tue Apr 26 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.18-1
- 0.4218 bump

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2:0.42.16-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 20 2016 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.16-1
- 0.4216 bump

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.42.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.14-1
- 0.4214 bump

* Wed Jun 10 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.12-3
- Perl 5.22 re-rebuild of bootstrapped packages

* Thu Jun 04 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.12-2
- Perl 5.22 rebuild

* Mon May 18 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.12-1
- 0.4212 bump

* Fri Jan 30 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.11-1
- 0.4211 bump

* Fri Jan 30 2015 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.10-4
- Sub-package perl-inc-latest

* Thu Dec 11 2014 Petr Pisar <ppisar@redhat.com> - 2:0.42.10-3
- Disable File::ShareDir optional tests when bootstrapping

* Wed Oct 15 2014 Petr Pisar <ppisar@redhat.com> - 2:0.42.10-2
- Require Software::License to recognize more license identifiers (bug #1152319)

* Wed Sep 10 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.10-1
- 0.4210 bump

* Sun Sep 07 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.08-3
- Perl 5.20 re-rebuild of bootstrapped packages

* Wed Aug 27 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.08-2
- Perl 5.20 rebuild

* Tue Aug 19 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.42.08-1
- 0.4208 bump

* Wed Jul 16 2014 Jitka Plesnikova <jplesnik@redhat.com> - 0.42.06-1
- 0.4206 bump

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.42.05-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Feb 13 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.05-1
- 0.4205 bump

* Wed Jan 15 2014 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.04-1
- 0.4204 bump

* Thu Nov 28 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.03-1
- 0.4203 bump

* Mon Nov 25 2013 Petr Pisar <ppisar@redhat.com> - 2:0.42.02-1
- 0.4202 bump

* Tue Nov 19 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.42.01-1
- 0.4201 bump

* Tue Nov 05 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.40.08-1
- 0.4008 bump

* Wed Aug 14 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.40.07-3
- Perl 5.18 re-rebuild of bootstrapped packages

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.40.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jul 26 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.40.05-1
- 0.4007 bump

* Fri Jul 12 2013 Petr Pisar <ppisar@redhat.com> - 2:0.40.05-2
- Perl 5.18 rebuild

* Mon Apr 29 2013 Jitka Plesnikova <jplesnik@redhat.com> - 2:0.40.05-1
- 0.4005 bump

* Wed Apr 03 2013 Petr Šabata <contyk@redhat.com> - 2:0.40.04-1
- 0.4004 bump

* Tue Jan 29 2013 Petr Pisar <ppisar@redhat.com> - 2:0.40.03-5
- Run-require POD convertors to get manual pages when building other packages

* Mon Dec 10 2012 Petr Pisar <ppisar@redhat.com> - 2:0.40.03-4
- YAML::Tiny is not needed at build time (bug #885146)

* Wed Nov 21 2012 Petr Šabata <contyk@redhat.com> - 2:0.40.03-3
- Add a few missing deps
- Drop command macros

* Mon Sep 03 2012 Petr Pisar <ppisar@redhat.com> - 2:0.40.03-2
- Do not build-require Module::Build (bug #849328)

* Mon Aug 20 2012 Petr Pisar <ppisar@redhat.com> - 2:0.40.03-1
- 0.4003 bump

* Mon Jul 30 2012 Jitka Plesnikova <jplesnik@redhat.com>  2:0.40.02-1
- 0.4002 bump

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.40.01-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jul 10 2012 Petr Pisar <ppisar@redhat.com> - 2:0.40.01-3
- Perl 5.16 re-rebuild of bootstrapped packages

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 2:0.40.01-2
- Perl 5.16 rebuild

* Wed Jun 27 2012 Petr Pisar <ppisar@redhat.com> - 2:0.40.01-1
- 0.4001 bump

* Wed Jun 06 2012 Petr Pisar <ppisar@redhat.com> - 2:0.40-3
- Perl 5.16 rebuild

* Mon Jun 04 2012 Petr Pisar <ppisar@redhat.com> - 2:0.40-2
- Do not run PAR tests on bootstrap

* Thu May 31 2012 Petr Pisar <ppisar@redhat.com> - 2:0.40-1
- 0.40 bump
- All reverse dependecies must require use 2-digit Module::Build version now

* Wed May 30 2012 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.3800-5
- conditionalize some test

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.3800-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 27 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.3800-3
- BR on perl-devel because this package contains macros used by rpmbuild
  for Perl packages

* Mon Jun 20 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.3800-2
- rebuild with Perl 5.14.1, remove defatter

* Wed Mar 16 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1:0.3800-1
- update to 0.3800

* Wed Mar 02 2011 Petr Pisar <ppisar@redhat.com> - 1:0.3624-2
- Raise epoch to  Core level
- Remove BuildRoot stuff

* Mon Feb 28 2011 Marcela Mašláňová <mmaslano@redhat.com> 0.3624-1
- update to new version
- fix BR, R

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3607-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Aug 30 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.3607-3
- switch off experimental test

* Tue Jun  8 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.3607-2
- copy check part&upload key from Paul Howarth
- fix macro

* Mon May 31 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.3607-1
- add BR, update, switch on some other tests

* Tue Mar 09 2010 Marcela Mašláňová <mmaslano@redhat.com> 0.3603-1
- Specfile autogenerated by cpanspec 1.78.
