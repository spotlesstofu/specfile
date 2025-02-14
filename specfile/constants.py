# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

# valid section names as defined in build/parseSpec.c in RPM source
SECTION_NAMES = {
    "build",
    "changelog",
    "check",
    "clean",
    "conf",
    "description",
    "end",
    "files",
    "filetrigger",
    "filetriggerin",
    "filetriggerpostun",
    "filetriggerun",
    "generate_buildrequires",
    "install",
    "package",
    "patchlist",
    "post",
    "posttrans",
    "postun",
    "postuntrans",
    "pre",
    "prep",
    "pretrans",
    "preun",
    "preuntrans",
    "sepolicy",
    "sourcelist",
    "transfiletrigger",
    "transfiletriggerin",
    "transfiletriggerpostun",
    "transfiletriggerun",
    "trigger",
    "triggerin",
    "triggerpostun",
    "triggerprein",
    "triggerun",
    "verifyscript",
}

SIMPLE_SCRIPT_SECTIONS = {
    "build",
    "check",
    "clean",
    "conf",
    "generate_buildrequires",
    "install",
}

SCRIPT_SECTIONS = {
    "filetrigger",
    "filetriggerin",
    "filetriggerpostun",
    "filetriggerun",
    "post",
    "posttrans",
    "postun",
    "postuntrans",
    "pre",
    "pretrans",
    "preun",
    "preuntrans",
    "transfiletrigger",
    "transfiletriggerin",
    "transfiletriggerpostun",
    "transfiletriggerun",
    "trigger",
    "triggerin",
    "triggerpostun",
    "triggerprein",
    "triggerun",
    "verifyscript",
}

# valid section option strings taken from build/parseSpec.c, build/parsePreamble.c,
# build/parseDescription.c, build/parseFiles.c, build/parsePolicies.c and build/parseScript.c
# in RPM source
SECTION_OPTIONS = {
    "description": "n:l:",
    "files": "n:f:",
    "package": "n:",
    "sepolicy": "n:",
}
SECTION_OPTIONS.update({s: "n:f:p:P:eq" for s in SCRIPT_SECTIONS})

# valid tag names as defined in build/parsePreamble.c in RPM source
TAG_NAMES = {
    "autoprov",
    "autoreq",
    "autoreqprov",
    "bugurl",
    "buildarch",
    "buildarchitectures",
    "buildconflicts",
    "buildprereq",
    "buildrequires",
    "buildroot",
    "conflicts",
    "distribution",
    "disttag",
    "disturl",
    "docdir",
    "enhances",
    "epoch",
    "excludearch",
    "excludeos",
    "exclusivearch",
    "exclusiveos",
    "group",
    "icon",
    "license",
    "modularitylabel",
    "name",
    "nopatch",
    "nosource",
    "obsoletes",
    "orderwithrequires",
    "packager",
    "patch",
    "prefix",
    "prefixes",
    "prereq",
    "provides",
    "recommends",
    "release",
    "removepathpostfixes",
    "requires",
    "source",
    "sourcelicense",
    "suggests",
    "summary",
    "supplements",
    "translationurl",
    "upstreamreleases",
    "url",
    "vcs",
    "vendor",
    "version",
}

# tags that can optionally have an argument (language or qualifier)
TAGS_WITH_ARG = {
    "group",
    "orderwithrequires",
    "prereq",
    "requires",
    "summary",
}

# canonical architecture names as defined in rpmrc.in in RPM source
ARCH_NAMES = {
    "IP",
    "aarch64",
    "alpha",
    "alphaev5",
    "alphaev56",
    "alphaev6",
    "alphaev67",
    "alphapca56",
    "amd64",
    "armv3l",
    "armv4b",
    "armv4l",
    "armv5tejl",
    "armv5tel",
    "armv5tl",
    "armv6hl",
    "armv6l",
    "armv7hl",
    "armv7hnl",
    "armv7l",
    "armv8hl",
    "armv8l",
    "atariclone",
    "atarist",
    "atariste",
    "ataritt",
    "athlon",
    "em64t",
    "falcon",
    "geode",
    "hades",
    "i370",
    "i386",
    "i486",
    "i586",
    "i686",
    "ia32e",
    "ia64",
    "loongarch64",
    "m68k",
    "m68kmint",
    "milan",
    "mips",
    "mips64",
    "mips64el",
    "mips64r6",
    "mips64r6el",
    "mipsel",
    "mipsr6",
    "mipsr6el",
    "pentium3",
    "pentium4",
    "ppc",
    "ppc32dy4",
    "ppc64",
    "ppc64iseries",
    "ppc64le",
    "ppc64p7",
    "ppc64pseries",
    "ppc8260",
    "ppc8560",
    "ppciseries",
    "ppcpseries",
    "riscv",
    "riscv64",
    "rs6000",
    "s390",
    "s390x",
    "sh",
    "sh3",
    "sh4",
    "sh4a",
    "sparc",
    "sparc64",
    "sparc64v",
    "sparcv8",
    "sparcv9",
    "sparcv9v",
    "sun4",
    "sun4c",
    "sun4d",
    "sun4m",
    "sun4u",
    "x86_64",
    "x86_64_v2",
    "x86_64_v3",
    "x86_64_v4",
    "xtensa",
}
