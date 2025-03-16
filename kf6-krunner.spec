#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeframever	6.12
%define		qtver		5.15.2
%define		kfname		krunner

Summary:	Framework for Plasma runners
Name:		kf6-%{kfname}
Version:	6.12.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/frameworks/%{kdeframever}/%{kfname}-%{version}.tar.xz
# Source0-md5:	8ce8c7e67b664ae96edad12212a2f0ac
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Network-devel >= %{qtver}
BuildRequires:	Qt6Qml-devel >= %{qtver}
BuildRequires:	Qt6Quick-devel >= %{qtver}
BuildRequires:	Qt6Test-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	Qt6Xml-devel >= %{qtver}
BuildRequires:	cmake >= 3.16
BuildRequires:	gettext-devel
BuildRequires:	kf6-attica-devel >= %{version}
BuildRequires:	kf6-extra-cmake-modules >= %{version}
BuildRequires:	kf6-kauth-devel >= %{version}
BuildRequires:	kf6-kbookmarks-devel >= %{version}
BuildRequires:	kf6-kcodecs-devel >= %{version}
BuildRequires:	kf6-kcompletion-devel >= %{version}
BuildRequires:	kf6-kconfig-devel >= %{version}
BuildRequires:	kf6-kconfigwidgets-devel >= %{version}
BuildRequires:	kf6-kcoreaddons-devel >= %{version}
BuildRequires:	kf6-kdbusaddons-devel >= %{version}
BuildRequires:	kf6-kglobalaccel-devel >= %{version}
BuildRequires:	kf6-kguiaddons-devel >= %{version}
BuildRequires:	kf6-ki18n-devel >= %{version}
BuildRequires:	kf6-kiconthemes-devel >= %{version}
BuildRequires:	kf6-kio-devel >= %{version}
BuildRequires:	kf6-kitemmodels-devel >= %{version}
BuildRequires:	kf6-kitemviews-devel >= %{version}
BuildRequires:	kf6-kjobwidgets-devel >= %{version}
BuildRequires:	kf6-kservice-devel >= %{version}
BuildRequires:	kf6-ktextwidgets-devel >= %{version}
BuildRequires:	kf6-kwidgetsaddons-devel >= %{version}
BuildRequires:	kf6-kwindowsystem-devel >= %{version}
BuildRequires:	kf6-kxmlgui-devel >= %{version}
BuildRequires:	kf6-solid-devel >= %{version}
BuildRequires:	kf6-sonnet-devel >= %{version}
BuildRequires:	kf6-threadweaver-devel >= %{version}
BuildRequires:	ninja
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	kf6-dirs
#Obsoletes:	kf5-%{kfname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
The Plasma workspace provides an application called KRunner which,
among other things, allows one to type into a text area which causes
various actions and information that match the text appear as the text
is being typed.

One application for this is the universal runner you can launch with
ALT-F2.

This functionality is provided via plugins loaded at runtime called
"Runners". These plugins can be used by any application using the
Plasma library. The KRunner framework is used to write these plugins.

%package devel
Summary:	Header files for %{kfname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kfname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
#Obsoletes:	kf5-%{kfname}-devel < %{version}

%description devel
Header files for %{kfname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kfname}.

%prep
%setup -q -n %{kfname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON

%ninja_build -C build

%if %{with tests}
%ninja_build -C build test
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%{_datadir}/qlogging-categories6/krunner.categories
%ghost %{_libdir}/libKF6Runner.so.6
%attr(755,root,root) %{_libdir}/libKF6Runner.so.*.*
%{_datadir}/dbus-1/interfaces/kf6_org.kde.krunner1.xml
%{_datadir}/kdevappwizard/templates/runner6.tar.bz2
%{_datadir}/kdevappwizard/templates/runner6python.tar.bz2
%{_datadir}/qlogging-categories6/krunner.renamecategories

%files devel
%defattr(644,root,root,755)
%{_includedir}/KF6/KRunner
%{_libdir}/cmake/KF6Runner
%{_libdir}/libKF6Runner.so
