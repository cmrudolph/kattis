#!/usr/bin/env python3

import os
import subprocess


def build(source_base, exe_base, source_files):
    for s in source_files:
        filename_no_ext = os.path.splitext(s)[0]
        ext_no_dot = (os.path.splitext(s)[1])[1:]

        source_path = f"{source_base}/{ext_no_dot}/{s}"
        exe_dir = f"{exe_base}/{ext_no_dot}"
        exe_path = f"{exe_dir}/{filename_no_ext}"

        if not os.path.exists(exe_dir):
            os.makedirs(exe_dir)

        if s.endswith(".c"):
            build_args = ["gcc", "-g", "-O2", "-std=gnu99", "-static",
                          "-Wno-unused-result", "-o", exe_path, source_path,
                          "-lm"]
        elif s.endswith(".cpp"):
            build_args = ["g++", "-g", "-O2", "-static", "-std=gnu++17", "-o",
                          exe_path, source_path]
        elif s.endswith(".fs"):
            build_args = ["fsharpc", source_path, "-o", exe_path + ".exe"]
        elif s.endswith(".go"):
            build_args = ["gccgo", "-g", "-static-libgcc", "-o", exe_path,
                          source_path]
        elif s.endswith(".py"):
            build_args = ["python3", "-m", "py_compile", source_path]

        print(" ".join(build_args))
        subprocess.run(build_args)
