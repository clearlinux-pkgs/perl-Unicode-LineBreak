#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Unicode-LineBreak
Version  : 2019.001
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/Unicode-LineBreak-2019.001.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEZUMI/Unicode-LineBreak-2019.001.tar.gz
Summary  : UAX #14 Unicode Line Breaking Algorithm
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-Unicode-LineBreak-license = %{version}-%{release}
Requires: perl-Unicode-LineBreak-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(MIME::Charset)

%description
Unicode::LineBreak performs Line Breaking Algorithm described in
Unicode Standard Annex #14 [UAX #14]. East_Asian_Width informative
properties defined by Annex #11 [UAX #11] will be concerned to
determine breaking positions.

%package dev
Summary: dev components for the perl-Unicode-LineBreak package.
Group: Development
Provides: perl-Unicode-LineBreak-devel = %{version}-%{release}
Requires: perl-Unicode-LineBreak = %{version}-%{release}

%description dev
dev components for the perl-Unicode-LineBreak package.


%package license
Summary: license components for the perl-Unicode-LineBreak package.
Group: Default

%description license
license components for the perl-Unicode-LineBreak package.


%package perl
Summary: perl components for the perl-Unicode-LineBreak package.
Group: Default
Requires: perl-Unicode-LineBreak = %{version}-%{release}

%description perl
perl components for the perl-Unicode-LineBreak package.


%prep
%setup -q -n Unicode-LineBreak-2019.001
cd %{_builddir}/Unicode-LineBreak-2019.001

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Unicode-LineBreak
cp %{_builddir}/Unicode-LineBreak-2019.001/sombok/COPYING %{buildroot}/usr/share/package-licenses/perl-Unicode-LineBreak/18eaf66587c5eea277721d5e569a6e3cd869f855
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/POD2::JA::Text::LineFold.3
/usr/share/man/man3/POD2::JA::Unicode::GCString.3
/usr/share/man/man3/POD2::JA::Unicode::LineBreak.3
/usr/share/man/man3/Text::LineFold.3
/usr/share/man/man3/Unicode::GCString.3
/usr/share/man/man3/Unicode::LineBreak.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Unicode-LineBreak/18eaf66587c5eea277721d5e569a6e3cd869f855

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/POD2/JA/Text/LineFold.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/POD2/JA/Unicode/GCString.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/POD2/JA/Unicode/LineBreak.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Text/LineFold.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Unicode/GCString.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Unicode/GCString.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Unicode/LineBreak.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Unicode/LineBreak.pod
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Unicode/LineBreak/Constants.pm
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/Unicode/LineBreak/Defaults.pm.sample
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/Unicode/LineBreak/LineBreak.so
/usr/lib/perl5/vendor_perl/5.34.0/x86_64-linux-thread-multi/auto/sombok/extralibs.ld
