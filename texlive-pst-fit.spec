%global tl_name pst-fit
%global tl_revision 70686

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.03
Release:	%{tl_revision}.1
Summary:	Macros for curve fitting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fit
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fit.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package uses PSTricks to fit curves to: Linear Functions; Power
Functions; exp Function; Log_{10} and Log_e functions; Recip; Kings Law
data; Gaussian; and 4th order Polynomial

