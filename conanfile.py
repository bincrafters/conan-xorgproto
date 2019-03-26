#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, AutoToolsBuildEnvironment, tools
from conans.errors import ConanInvalidConfiguration
import os


class XOrgProtoConan(ConanFile):
    name = "xorgproto"
    version = "2018.4"
    description = "This package provides the headers and specification documents defining " \
                  "the core protocol and (many) extensions for the X Window System"
    topics = ("conan", "xorgproto", "xproto", "X11")
    url = "https://github.com/bincrafters/conan-xorgproto"
    homepage = "https://gitlab.freedesktop.org/xorg/proto/xorgproto"
    author = "Bincrafters <bincrafters@gmail.com>"
    license = "X11"
    exports = ["LICENSE.md"]
    settings = "os", "arch", "compiler", "build_type"
    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def configure(self):
        del self.settings.compiler.libcxx
        if self.settings.os != "Linux":
            raise ConanInvalidConfiguration("only Linux is supported")

    def source(self):
        source_url = "https://www.x.org/archive//individual/proto/xorgproto-%s.tar.bz2" % self.version
        tools.get(source_url, sha256="fee885e0512899ea5280c593fdb2735beb1693ad170c22ebcc844470eec415a0")
        os.rename("xorgproto-" + self.version, self._source_subfolder)

    def build(self):
        with tools.chdir(self._source_subfolder):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.configure()
            env_build.make()
            env_build.install()

    def package(self):
        self.copy(pattern="COPYING*", dst="licenses", src=self._source_subfolder)

    def package_id(self):
        self.info.header_only()
