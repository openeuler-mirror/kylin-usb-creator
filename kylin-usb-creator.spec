Name:           kylin-usb-creator
Version:        1.1.2
Release:        2
Summary:        kylin-usb-creator
License:        GPL-3+
URL:            http://www.ukui.org
Source0:        %{name}-%{version}.tar.gz
Patch01:        0001-fix-version-of-kylin-usb-creator.patch
Patch02:        0002-add-kylin-user-guide-of-kylin-usb-creator.patch
Patch03:        0003-fix-clang.patch

BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qtchooser
BuildRequires:  qt5-qtbase-devel
BuildRequires:  pkgconf
BuildRequires:  gsettings-qt-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  polkit-qt5-1-devel
BuildRequires:  ukui-interface


%description
 kylin-usb-creator

%prep
%autosetup -p1

%build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  kylin-usb-creator.pro
%{make_build}

%install
rm -rf $RPM_BUILD_ROOT
make INSTALL_ROOT=%{buildroot} install

mkdir -p %{buildroot}/etc/bin/
mkdir -p %{buildroot}/usr/share/doc/kylin-usb-creator/
mkdir -p %{buildroot}/usr/share/man/man1/
cp debian/copyright  %{buildroot}/usr/share/doc/kylin-usb-creator/
gzip -c debian/changelog > %{buildroot}/usr/share/doc/kylin-usb-creator/changelog.gz

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/kylin-usb-creator
%{_datadir}/applications/kylin-usb-creator.desktop
%{_datadir}/doc/kylin-usb-creator/changelog.gz
%{_datadir}/doc/kylin-usb-creator/copyright
%{_datadir}/pixmaps/kylin-usb-creator.png
%{_sysconfdir}/dbus-1/system.d/com.kylinusbcreator.systemdbus.conf
%{_bindir}/kylin-usb-creator-sysdbus
%{_datadir}/dbus-1/system-services/com.kylinusbcreator.systemdbus.service
%{_datadir}/glib-2.0/schemas/org.kylin-usb-creator-data.gschema.xml
%{_datadir}/polkit-1/actions/com.kylinusbcreator.systemdbus.policy
%{_datadir}/kylin-user-guide/data/guide/kylin-usb-creator




%changelog
* Tue Jun 20 2023 yoo <sunyuechi@iscas.ac.cn> - 1.1.2-2
- fix clang build error

* Mon May 08 2023 peijiankang <peijiankang@kylinos.cn> - 1.1.2-1
- update to upstream version 1.1.2

* Wed Mar 22 2023 peijiankang <peijiankang@kylinos.cn> - 1.1.1-4
- add kylin-user-guide of kylin-usb-creator

* Wed Mar 22 2023 peijiankang <peijiankang@kylinos.cn> - 1.1.1-3
- fix version of kylin-usb-creator

* Tue Feb 07 2023 peijiankang <peijiankang@kylinos.cn> - 1.1.1-2
- add build debuginfo and debugsource

* Wed Mar 16 2022 tanyulong <tanyulong@kylinos.cn> - 1.1.1-1
- update to upstream version 1.1.1

* Fri Dec 10 2021 douyan <douyan@kylinos.cn> - 1.0.0-3
- fix min window logic

* Wed Dec 8 2021 douyan <douyan@kylinos.cn> - 1.0.0-2
- add dbus service
* Tue Dec 15 2020 lvhan <lvhan@kylinos.cn> - 1.0.0-1
- update to upstream version 1.0.0-26kord
