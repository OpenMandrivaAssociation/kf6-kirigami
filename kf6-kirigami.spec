%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define oldlibname %mklibname KF6Kirigami
%define olddevname %mklibname KF6Kirigami -d
%define libname %mklibname KirigamiPlatform
%define devname %mklibname KirigamiPlatform -d
#define git 20231103

Name: kf6-kirigami
Version: 5.247.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/kirigami/-/archive/master/kirigami-master.tar.bz2#/kirigami-%{git}.tar.bz2
%else
Source0: https://download.kde.org/%{stable}/frameworks/%{version}/kirigami-%{version}.tar.xz   
%endif
Summary: QtQuick plugins to build user interfaces following the KDE Human Interface Guidelines
URL: https://invent.kde.org/frameworks/kirigami
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6ShaderTools)
Requires: %{libname} = %{EVRD}

%description
QtQuick plugins to build user interfaces following the KDE Human Interface Guidelines

%package -n %{libname}
Summary: QtQuick plugins to build user interfaces following the KDE Human Interface Guidelines
Group: System/Libraries
Requires: %{name} = %{EVRD}
%rename %{oldlibname}

%description -n %{libname}
QtQuick plugins to build user interfaces following the KDE Human Interface Guidelines

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}
%rename %{olddevname}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

QtQuick plugins to build user interfaces following the KDE Human Interface Guidelines

%prep
%autosetup -p1 -n kirigami-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/kdevappwizard/templates/kirigami6.tar.bz2
%{_datadir}/qlogging-categories6/kirigami.categories

%files -n %{devname}
%{_includedir}/KF6/Kirigami
%{_libdir}/cmake/KF6Kirigami*
%{_qtdir}/doc/KF6KirigamiPlatform.*

%files -n %{libname}
%{_libdir}/libKirigami.so*
%{_libdir}/libKirigamiDelegates.so*
%{_libdir}/libKirigamiPlatform.so*
%{_qtdir}/qml/org/kde/kirigami
