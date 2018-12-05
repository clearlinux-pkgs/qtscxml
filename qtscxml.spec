#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtscxml
Version  : 5.12.0
Release  : 15
URL      : https://download.qt.io/official_releases/qt/5.12/5.12.0/submodules/qtscxml-everywhere-src-5.12.0.tar.xz
Source0  : https://download.qt.io/official_releases/qt/5.12/5.12.0/submodules/qtscxml-everywhere-src-5.12.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GFDL-1.3 GPL-3.0 LGPL-3.0
Requires: qtscxml-bin = %{version}-%{release}
Requires: qtscxml-lib = %{version}-%{release}
Requires: qtscxml-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Network)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)

%description
Test Suite taken from https://github.com/jbeard4/scxml-test-framework,
the test framework of https://github.com/jbeard4/SCION .
It is licensed with the Apache 2.0 license, see LICENSE.txt

%package bin
Summary: bin components for the qtscxml package.
Group: Binaries
Requires: qtscxml-license = %{version}-%{release}

%description bin
bin components for the qtscxml package.


%package dev
Summary: dev components for the qtscxml package.
Group: Development
Requires: qtscxml-lib = %{version}-%{release}
Requires: qtscxml-bin = %{version}-%{release}
Provides: qtscxml-devel = %{version}-%{release}

%description dev
dev components for the qtscxml package.


%package lib
Summary: lib components for the qtscxml package.
Group: Libraries
Requires: qtscxml-license = %{version}-%{release}

%description lib
lib components for the qtscxml package.


%package license
Summary: license components for the qtscxml package.
Group: Default

%description license
license components for the qtscxml package.


%prep
%setup -q -n qtscxml-everywhere-src-5.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
%qmake
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1544048627
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/qtscxml
cp LICENSE.FDL %{buildroot}/usr/share/package-licenses/qtscxml/LICENSE.FDL
cp LICENSE.GPL3-EXCEPT %{buildroot}/usr/share/package-licenses/qtscxml/LICENSE.GPL3-EXCEPT
cp LICENSE.LGPL3 %{buildroot}/usr/share/package-licenses/qtscxml/LICENSE.LGPL3
cp tests/3rdparty/scion-tests/LICENSE.txt %{buildroot}/usr/share/package-licenses/qtscxml/tests_3rdparty_scion-tests_LICENSE.txt
cp tests/3rdparty/scion-tests/scxml-test-framework/LICENSE.txt %{buildroot}/usr/share/package-licenses/qtscxml/tests_3rdparty_scion-tests_scxml-test-framework_LICENSE.txt
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/qscxmlc

%files dev
%defattr(-,root,root,-)
/usr/bin/qscxmlc
/usr/include/qt5/QtScxml/5.12.0/QtScxml/private/qscxmlcompiler_p.h
/usr/include/qt5/QtScxml/5.12.0/QtScxml/private/qscxmlcppdatamodel_p.h
/usr/include/qt5/QtScxml/5.12.0/QtScxml/private/qscxmldatamodel_p.h
/usr/include/qt5/QtScxml/5.12.0/QtScxml/private/qscxmlecmascriptplatformproperties_p.h
/usr/include/qt5/QtScxml/5.12.0/QtScxml/private/qscxmlevent_p.h
/usr/include/qt5/QtScxml/5.12.0/QtScxml/private/qscxmlexecutablecontent_p.h
/usr/include/qt5/QtScxml/5.12.0/QtScxml/private/qscxmlglobals_p.h
/usr/include/qt5/QtScxml/5.12.0/QtScxml/private/qscxmlinvokableservice_p.h
/usr/include/qt5/QtScxml/5.12.0/QtScxml/private/qscxmlstatemachine_p.h
/usr/include/qt5/QtScxml/5.12.0/QtScxml/private/qscxmlstatemachineinfo_p.h
/usr/include/qt5/QtScxml/5.12.0/QtScxml/private/qscxmltabledata_p.h
/usr/include/qt5/QtScxml/5.12.0/QtScxml/private/qtscxml-config_p.h
/usr/include/qt5/QtScxml/QScxmlCompiler
/usr/include/qt5/QtScxml/QScxmlCppDataModel
/usr/include/qt5/QtScxml/QScxmlDataModel
/usr/include/qt5/QtScxml/QScxmlDynamicScxmlServiceFactory
/usr/include/qt5/QtScxml/QScxmlEcmaScriptDataModel
/usr/include/qt5/QtScxml/QScxmlError
/usr/include/qt5/QtScxml/QScxmlEvent
/usr/include/qt5/QtScxml/QScxmlInvokableService
/usr/include/qt5/QtScxml/QScxmlInvokableServiceFactory
/usr/include/qt5/QtScxml/QScxmlNullDataModel
/usr/include/qt5/QtScxml/QScxmlStateMachine
/usr/include/qt5/QtScxml/QScxmlStaticScxmlServiceFactory
/usr/include/qt5/QtScxml/QScxmlTableData
/usr/include/qt5/QtScxml/QtScxml
/usr/include/qt5/QtScxml/QtScxmlDepends
/usr/include/qt5/QtScxml/QtScxmlVersion
/usr/include/qt5/QtScxml/qscxmlcompiler.h
/usr/include/qt5/QtScxml/qscxmlcppdatamodel.h
/usr/include/qt5/QtScxml/qscxmldatamodel.h
/usr/include/qt5/QtScxml/qscxmlecmascriptdatamodel.h
/usr/include/qt5/QtScxml/qscxmlerror.h
/usr/include/qt5/QtScxml/qscxmlevent.h
/usr/include/qt5/QtScxml/qscxmlexecutablecontent.h
/usr/include/qt5/QtScxml/qscxmlglobals.h
/usr/include/qt5/QtScxml/qscxmlinvokableservice.h
/usr/include/qt5/QtScxml/qscxmlnulldatamodel.h
/usr/include/qt5/QtScxml/qscxmlstatemachine.h
/usr/include/qt5/QtScxml/qscxmltabledata.h
/usr/include/qt5/QtScxml/qtscxml-config.h
/usr/include/qt5/QtScxml/qtscxmlversion.h
/usr/lib64/cmake/Qt5Scxml/Qt5ScxmlConfig.cmake
/usr/lib64/cmake/Qt5Scxml/Qt5ScxmlConfigExtras.cmake
/usr/lib64/cmake/Qt5Scxml/Qt5ScxmlConfigVersion.cmake
/usr/lib64/cmake/Qt5Scxml/Qt5ScxmlMacros.cmake
/usr/lib64/libQt5Scxml.prl
/usr/lib64/libQt5Scxml.so
/usr/lib64/pkgconfig/Qt5Scxml.pc
/usr/lib64/qt5/mkspecs/features/qscxmlc.prf
/usr/lib64/qt5/mkspecs/modules/qt_lib_scxml.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_scxml_private.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Scxml.so.5
/usr/lib64/libQt5Scxml.so.5.12
/usr/lib64/libQt5Scxml.so.5.12.0
/usr/lib64/qt5/qml/QtScxml/libdeclarative_scxml.so
/usr/lib64/qt5/qml/QtScxml/plugins.qmltypes
/usr/lib64/qt5/qml/QtScxml/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/qtscxml/LICENSE.FDL
/usr/share/package-licenses/qtscxml/LICENSE.GPL3-EXCEPT
/usr/share/package-licenses/qtscxml/LICENSE.LGPL3
/usr/share/package-licenses/qtscxml/tests_3rdparty_scion-tests_LICENSE.txt
/usr/share/package-licenses/qtscxml/tests_3rdparty_scion-tests_scxml-test-framework_LICENSE.txt
