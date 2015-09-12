Summary:	KDE Screenshot Utility
Name:		ksnapshot
Version:	15.08.0
Release:	2
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
Url:		http://www.kde.org/applications/graphics/ksnapshot
Source0:	http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
# Workaround keyboard grabbing issues with delayed capture
# When capturing screenshots with popped up menus, in some cases
# grabber doesn't get initialized properly
# See KDE bug: https://bugs.kde.org/show_bug.cgi?id=210916
Patch0:		ksnapshot-4.10.3-grabkeyboard.patch
BuildRequires:	kdelibs-devel
BuildRequires:	pkgconfig(libkipi)
BuildRequires:	pkgconfig(xcb-xfixes)
Conflicts:	kdegraphics4-devel < 2:4.6.90
Requires:	kipi-common
Suggests:	kipi-plugins

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
%doc COPYING COPYING.LIB COPYING.DOC
%doc %{_kde_docdir}/HTML/en/%{name}/
%{_kde_bindir}/kbackgroundsnapshot
%{_kde_bindir}/%{name}
%{_kde_applicationsdir}/%{name}.desktop
%{_kde_iconsdir}/hicolor/*/apps/%{name}.png
%{_kde_iconsdir}/hicolor/scalable/apps/%{name}.svgz
%{_datadir}/dbus-1/interfaces/org.kde.ksnapshot.xml

#----------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build
