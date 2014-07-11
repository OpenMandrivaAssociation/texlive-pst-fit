# revision 28155
# category Package
# catalog-ctan /graphics/pstricks/contrib/pst-fit
# catalog-date 2012-11-02 19:53:22 +0100
# catalog-license lppl
# catalog-version 0.01
Name:		texlive-pst-fit
Version:	0.01
Release:	7
Summary:	Macros for curve fitting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fit
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fit.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fit.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fit.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides fitting of: 1. Linear Functions; 2. Power
Functions; 3. exp Function; 4. Log_{10} and Log_e functions; 5.
Recip; 6. Kings Law data; 7. Gaussian; and 8. 4th order
Polynomial.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/generic/pst-fit/pst-fit.tex
%{_texmfdistdir}/tex/latex/pst-fit/pst-fit.sty
%doc %{_texmfdistdir}/doc/generic/pst-fit/Changes
%doc %{_texmfdistdir}/doc/generic/pst-fit/README
%doc %{_texmfdistdir}/doc/generic/pst-fit/pst-fit-doc.bib
%doc %{_texmfdistdir}/doc/generic/pst-fit/pst-fit-doc.data
%doc %{_texmfdistdir}/doc/generic/pst-fit/pst-fit-doc.pdf
%doc %{_texmfdistdir}/doc/generic/pst-fit/pst-fit-doc.tex
#- source
%doc %{_texmfdistdir}/source/generic/pst-fit/Makefile

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
