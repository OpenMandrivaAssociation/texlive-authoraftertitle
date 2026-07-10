%global tl_name authoraftertitle
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Make author, etc., available after \maketitle
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/authoraftertitle
License:	cc0
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/authoraftertitle.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/authoraftertitle.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This jiffy package makes the author, title and date of the package
available to the user (as \MyAuthor, etc) after the \maketitle command
has been executed.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/authoraftertitle
%dir %{_datadir}/texmf-dist/tex/latex/authoraftertitle
%doc %{_datadir}/texmf-dist/doc/latex/authoraftertitle/README.md
%doc %{_datadir}/texmf-dist/doc/latex/authoraftertitle/authoraftertitle.pdf
%doc %{_datadir}/texmf-dist/doc/latex/authoraftertitle/authoraftertitle.tex
%{_datadir}/texmf-dist/tex/latex/authoraftertitle/authoraftertitle.sty
