Name:		texlive-pst-fit
Version:	0.02
Release:	1
Summary:	Macros for curve fitting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/pstricks/contrib/pst-fit
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fit.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-fit.doc.tar.xz
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
%{_texmfdistdir}/tex/generic/pst-fit
%{_texmfdistdir}/tex/latex/pst-fit
%doc %{_texmfdistdir}/doc/generic/pst-fit

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
