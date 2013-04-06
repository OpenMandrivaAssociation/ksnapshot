Name:		ksnapshot
Summary:	KDE Screenshot Utility
Version:	4.10.2
Release:	1
Epoch:		2
Group:		Graphical desktop/KDE
License:	GPLv2 LGPLv2 GFDL
URL:		http://www.kde.org/applications/graphics/ksnapshot
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kdelibs4-devel
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

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.10.0-1
- New version 4.10.0

* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.1-1
- New version 4.9.1

* Mon Aug 13 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.9.0-1
- New version 4.9.0

* Thu Jul 19 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.97-1
- New version 4.8.97

* Mon Jul 02 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 2:4.8.95-1
- New version 4.8.95

* Fri Jun 08 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.4-69.1mib2010.2
- New version 4.8.4
- MIB (Mandriva International Backports)

* Fri May 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.3-69.1mib2010.2
- New version 4.8.3
- MIB (Mandriva International Backports)

* Wed Apr 04 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.2-69.1mib2010.2
- New version 4.8.2
- MIB (Mandriva International Backports)

* Wed Mar 07 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.1-69.1mib2010.2
- New version 4.8.1
- MIB (Mandriva International Backports)

* Mon Feb 20 2012 Andrey Bondrov <bondrov@math.dvgu.ru> 2:4.8.0-69.1mib2010.2
+ Revision: 762483
- Backport to 2010.2 for MIB users
- Add pkgconfig(xcb-xfixes) to BuildRequires
- MIB (Mandriva International Backports)

* Thu Jan 19 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.8.0-1
+ Revision: 762483
- New upstream tarball

* Fri Jan 06 2012 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.97-1
+ Revision: 758070
- New upstream tarball

* Thu Dec 22 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.95-1
+ Revision: 744553
- New upstream tarball

* Fri Dec 09 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.90-1
+ Revision: 739308
- New upstream tarball $NEW_VERSION

* Sat Nov 19 2011 Nicolas Lécureuil <nlecureuil@mandriva.com> 2:4.7.80-1
+ Revision: 731863
- Really use ksnapshot spec file
- New upstream tarball 4.7.80
- Import package
- Create current folder

