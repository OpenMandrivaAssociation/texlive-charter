Name:		texlive-charter
Version:	15878
Release:	2
Summary:	Charter fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/charter
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/charter.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/charter.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A commercial text font donated for the common good. Support for
use with LaTeX is available in freenfss, part of psnfss.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/bitstrea/charter/bchb8a.afm
%{_texmfdistdir}/fonts/afm/bitstrea/charter/bchbi8a.afm
%{_texmfdistdir}/fonts/afm/bitstrea/charter/bchr8a.afm
%{_texmfdistdir}/fonts/afm/bitstrea/charter/bchri8a.afm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchb7t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchb8c.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchb8r.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchb8t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchbc7t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchbc8t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchbi7t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchbi8c.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchbi8r.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchbi8t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchbo7t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchbo8c.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchbo8r.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchbo8t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchr7t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchr8c.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchr8r.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchr8t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchrc7t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchrc8t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchri7t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchri8c.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchri8r.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchri8t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchro7t.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchro8c.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchro8r.tfm
%{_texmfdistdir}/fonts/tfm/bitstrea/charter/bchro8t.tfm
%{_texmfdistdir}/fonts/type1/bitstrea/charter/bchb8a.pfb
%{_texmfdistdir}/fonts/type1/bitstrea/charter/bchbi8a.pfb
%{_texmfdistdir}/fonts/type1/bitstrea/charter/bchr8a.pfb
%{_texmfdistdir}/fonts/type1/bitstrea/charter/bchri8a.pfb
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchb7t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchb8c.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchb8t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchbc7t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchbc8t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchbi7t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchbi8c.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchbi8t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchbo7t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchbo8c.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchbo8t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchr7t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchr8c.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchr8t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchrc7t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchrc8t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchri7t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchri8c.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchri8t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchro7t.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchro8c.vf
%{_texmfdistdir}/fonts/vf/bitstrea/charter/bchro8t.vf
%doc %{_texmfdistdir}/doc/fonts/charter/readme.charter

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}
