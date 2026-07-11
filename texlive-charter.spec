%global tl_name charter
%global tl_revision 15878

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Charter fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/charter
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/charter.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/charter.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A commercial text font donated for the common good. Support for use with
LaTeX is available in freenfss, part of psnfss.

