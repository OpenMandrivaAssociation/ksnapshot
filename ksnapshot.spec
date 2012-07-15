Name:     ksnapshot
Summary: KDE Screenshot Utility
Version: 4.8.97
Release: 1
Epoch:   2
Group:   Graphical desktop/KDE
License: GPLv2 LGPLv2 GFDL
URL:     http://www.kde.org/applications/graphics/ksnapshot
Source:  ftp://ftp.kde.org/pub/kde/unstable/%version/src/%name-%version.tar.xz
BuildRequires: kdelibs4-devel >= 2:%{version}
BuildRequires: libkipi-devel >= 2:%{version}
Conflicts:     kdegraphics4-devel < 2:4.6.90
Requires:      kipi-common

%description
KSnapshot is a KDE snapshot tool with many features.
Features:
    - Save in multiple formats
    - Take new shapshot
    - Open with... possibility to open snapshot in external editor.
    - Copy to clipboard
    - Several capture modes, including selected region or single window
    - Snapshot delay

%files
%_kde_bindir/kbackgroundsnapshot
%_kde_bindir/%name
%_kde_datadir/applications/kde4/%name.desktop
%_kde_iconsdir/hicolor/*/apps/%name.png
%_kde_iconsdir/hicolor/scalable/apps/%name.svgz
%_datadir/dbus-1/interfaces/org.kde.ksnapshot.xml
%doc COPYING COPYING.LIB COPYING.DOC
%doc %_kde_docdir/HTML/en/%name/

#----------------------------------------------------------------------

%prep
%setup -q 

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

