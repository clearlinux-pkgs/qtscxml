#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : qtscxml
Version  : 5.10.1
Release  : 4
URL      : http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtscxml-everywhere-src-5.10.1.tar.xz
Source0  : http://download.qt.io/official_releases/qt/5.10/5.10.1/submodules/qtscxml-everywhere-src-5.10.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 GFDL-1.3 GPL-3.0 LGPL-3.0
Requires: qtscxml-bin
Requires: qtscxml-lib
BuildRequires : cmake
BuildRequires : pkgconfig(Qt5Core)
BuildRequires : pkgconfig(Qt5Gui)
BuildRequires : pkgconfig(Qt5Qml)
BuildRequires : pkgconfig(Qt5Test)
BuildRequires : pkgconfig(Qt5Widgets)
BuildRequires : qtbase-dev

%description
Test Suite taken from https://github.com/jbeard4/scxml-test-framework,
the test framework of https://github.com/jbeard4/SCION .
It is licensed with the Apache 2.0 license, see LICENSE.txt

%package bin
Summary: bin components for the qtscxml package.
Group: Binaries

%description bin
bin components for the qtscxml package.


%package dev
Summary: dev components for the qtscxml package.
Group: Development
Requires: qtscxml-lib
Requires: qtscxml-bin
Provides: qtscxml-devel

%description dev
dev components for the qtscxml package.


%package extras
Summary: extras components for the qtscxml package.
Group: Default

%description extras
extras components for the qtscxml package.


%package lib
Summary: lib components for the qtscxml package.
Group: Libraries

%description lib
lib components for the qtscxml package.


%prep
%setup -q -n qtscxml-everywhere-src-5.10.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
qmake QMAKE_CFLAGS="$CFLAGS" QMAKE_CXXFLAGS="$CXXFLAGS" QMAKE_LFLAGS="$LDFLAGS" \
    QMAKE_CFLAGS_RELEASE= QMAKE_CXXFLAGS_RELEASE=
test -r config.log && cat config.log
make  %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/qscxmlc

%files dev
%defattr(-,root,root,-)
/usr/include/qt5/QtScxml/5.10.1/QtScxml/private/qscxmlcompiler_p.h
/usr/include/qt5/QtScxml/5.10.1/QtScxml/private/qscxmlcppdatamodel_p.h
/usr/include/qt5/QtScxml/5.10.1/QtScxml/private/qscxmldatamodel_p.h
/usr/include/qt5/QtScxml/5.10.1/QtScxml/private/qscxmlecmascriptplatformproperties_p.h
/usr/include/qt5/QtScxml/5.10.1/QtScxml/private/qscxmlevent_p.h
/usr/include/qt5/QtScxml/5.10.1/QtScxml/private/qscxmlexecutablecontent_p.h
/usr/include/qt5/QtScxml/5.10.1/QtScxml/private/qscxmlglobals_p.h
/usr/include/qt5/QtScxml/5.10.1/QtScxml/private/qscxmlinvokableservice_p.h
/usr/include/qt5/QtScxml/5.10.1/QtScxml/private/qscxmlstatemachine_p.h
/usr/include/qt5/QtScxml/5.10.1/QtScxml/private/qscxmlstatemachineinfo_p.h
/usr/include/qt5/QtScxml/5.10.1/QtScxml/private/qscxmltabledata_p.h
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
/usr/include/qt5/QtScxml/qtscxmlversion.h
/usr/lib64/cmake/Qt5Scxml/Qt5ScxmlConfig.cmake
/usr/lib64/cmake/Qt5Scxml/Qt5ScxmlConfigExtras.cmake
/usr/lib64/cmake/Qt5Scxml/Qt5ScxmlConfigVersion.cmake
/usr/lib64/cmake/Qt5Scxml/Qt5ScxmlMacros.cmake
/usr/lib64/libQt5Scxml.la
/usr/lib64/libQt5Scxml.prl
/usr/lib64/libQt5Scxml.so
/usr/lib64/pkgconfig/Qt5Scxml.pc
/usr/lib64/qt5/mkspecs/features/qscxmlc.prf
/usr/lib64/qt5/mkspecs/modules/qt_lib_scxml.pri
/usr/lib64/qt5/mkspecs/modules/qt_lib_scxml_private.pri

%files extras
%defattr(-,root,root,-)
/usr/bin/qscxmlc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libQt5Scxml.so.5
/usr/lib64/libQt5Scxml.so.5.10
/usr/lib64/libQt5Scxml.so.5.10.1
/usr/lib64/qt5/qml/QtScxml/libdeclarative_scxml.so
/usr/lib64/qt5/qml/QtScxml/plugins.qmltypes
/usr/lib64/qt5/qml/QtScxml/qmldir
