%define	fontname	tibetan-machine-uni
%define zipname		TibetanMachineUnicodeFont

Name:		%{fontname}-fonts
Version:	1.901
Release:	11%{?dist}
Summary:	Tibetan Machine Uni font for Tibetan, Dzongkha and Ladakhi

Group:		User Interface/X
# .ttf file now states GPLv3+ with fonts exceptions
License:	GPLv3+ with exceptions
URL:		http://www.thlib.org/tools/#wiki=/access/wiki/site/26a34146-33a6-48ce-001e-f16ce7908a6a/tibetan%20machine%20uni.html
Source0:	https://collab.itc.virginia.edu/access/content/group/26a34146-33a6-48ce-001e-f16ce7908a6a/Tibetan%20fonts/Tibetan%20Unicode%20Fonts/%{zipname}.zip

BuildArch:	noarch
BuildRequires:	fontpackages-devel
BuildRequires:	dos2unix
Requires:	fontpackages-filesystem

%description
Tibetan Machine Uni is an TrueType OpenType, Unicode font released by THDL
project. The font supports Tibetan, Dzongkha and Ladakhi in dbu-can script
with full support for the Sanskrit combinations found in chos skad text.

%prep
%setup -q -n %{zipname}

%build
# Empty build section

%install

install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

dos2unix -o ReadMe.txt

%clean

%_font_pkg *.ttf
%doc gpl.txt ReadMe.txt

%changelog
* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.901-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Dec 12 2012 Paul Flo Williams <paul@frixxon.co.uk> - 1.901-10
- New upstream zip with updated licence file but same font

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.901-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.901-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.901-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 17 2010 Jens Petersen <petersen@redhat.com> - 1.901-6
- remove duplicate font dir
- use dos2unix on doc files

* Thu Feb 11 2010 Jens Petersen <petersen@redhat.com> - 1.901-5
- license in the font is now GPLv3+ (with fonts exception)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.901-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Sun Mar 15 2009 Marcin Garski <mgarski[AT]post.pl> 1.901-3
- Update to 1.901b
- Update URL
- Update to new fonts guidelines, thanks to Rajeesh (#477467)

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.901-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Dec 29 2007 Marcin Garski <mgarski[AT]post.pl> 1.901-1
- Update to 1.901

* Fri Aug 31 2007 Marcin Garski <mgarski[AT]post.pl> 1.0-2
- Fix license tag
- Update URL

* Mon Mar 12 2007 Marcin Garski <mgarski[AT]post.pl> 1.0-1
- Initial specfile
