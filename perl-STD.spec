%define upstream_name    STD
%define upstream_version 20101111

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(STD\\)|perl\\(STD_P6\\)|perl\\(RE_ast\\)|perl\\(STD::Cursor\\)|perl\\(STD_P5\\)'
%endif

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    7

Summary:	%{upstream_name} perl module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module//%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(File::ShareDir)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(YAML::XS)

BuildArch:	noarch

%description
%{upstream_name} perl module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc META.yml LICENSE
%{_bindir}/*
%{_mandir}/man1/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 20101111.0.0-2mdv2011.0
+ Revision: 657830
- rebuild for updated spec-helper

* Thu Dec 30 2010 Guillaume Rousse <guillomovitch@mandriva.org> 20101111.0.0-1mdv2011.0
+ Revision: 626240
- new version

* Fri Sep 03 2010 Jérôme Quelin <jquelin@mandriva.org> 32116.0.0-1mdv2011.0
+ Revision: 575601
- import perl-STD

