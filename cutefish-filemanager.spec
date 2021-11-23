%define oname filemanager

Name:           cutefish-filemanager
Version:        0.5
Release:        1
Summary:        File Manager for Cutefish desktop
License:        GPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/cutefishos/filemanager
Source:         https://github.com/cutefishos/filemanager/archive/refs/tags/%{version}/%{oname}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(FishUI)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)

Requires:       fishui

%description
Cutefish File Manager.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%cmake
%make_build

%install
%make_install -C build

%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
