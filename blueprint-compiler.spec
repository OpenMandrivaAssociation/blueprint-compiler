%define commit 06278a64248cec92bb95a958eadfba453943c061
%define commit_short %(echo %{commit} | head -c6)

Summary:	A markup language for GTK user interface files
Name:		blueprint-compiler
Version:	0.4.0
Release:	1
License:	GPLv3+
Group:		Development/GNOME and GTK+
Url:		https://gitlab.gnome.org/jwestman/blueprint-compiler
Source0:	https://gitlab.gnome.org/jwestman/blueprint-compiler/-/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildRequires:	meson

%description
A markup language for GTK user interface files.

#----------------------------------------------------------------------------

%package -n python3-%{name}
Summary:	A markup language for GTK user interface files
Group:		Development/Python

%description -n python3-%{name}
A markup language for GTK user interface files.

%files -n python3-%{name}
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/blueprintcompiler

#----------------------------------------------------------------------------

%package -n %{name}-devel
Summary:	Devel file for %{name}
Group:		Development/Python
Requires:	python3-%{name} = %{EVRD}

%description -n %{name}-devel
Devel file for %{name}.

%files -n %{name}-devel
%{_datadir}/pkgconfig/%{name}.pc

#------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-%{commit}

%build
%meson
%meson_build

%install
%meson_install
