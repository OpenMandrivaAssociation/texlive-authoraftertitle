# revision 24863
# category Package
# catalog-ctan /macros/latex/contrib/authoraftertitle
# catalog-date 2011-12-17 14:41:04 +0100
# catalog-license pd
# catalog-version 0.9
Name:		texlive-authoraftertitle
Version:	0.9
Release:	11
Summary:	Make author, etc., available after \maketitle
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/authoraftertitle
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authoraftertitle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/authoraftertitle.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This jiffy package makes the author, title and date of the
package available to the user (as \MyAuthor, etc) after the
\maketitle command has been executed.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/authoraftertitle/authoraftertitle.sty
%doc %{_texmfdistdir}/doc/latex/authoraftertitle/authoraftertitle.pdf
%doc %{_texmfdistdir}/doc/latex/authoraftertitle/authoraftertitle.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9-3
+ Revision: 749436
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9-2
+ Revision: 745157
- texlive-authoraftertitle

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.9-1
+ Revision: 717870
- texlive-authoraftertitle
- texlive-authoraftertitle
- texlive-authoraftertitle
- texlive-authoraftertitle
- texlive-authoraftertitle

