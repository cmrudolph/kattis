#!/usr/bin/env python3

import argparse
import os
import sys
import pathlib
import glob
import subprocess
import platform

from timeit import default_timer as timer
from colorama import init, Fore, Style


class TestCase:
    def __init__(self, problem_generic, problem_specific, case_name):
        self.name = case_name
        self.in_path = f"{DATA_ROOT}/{problem_generic}/{case_name}.in"
        self.ans_path = f"{DATA_ROOT}/{problem_generic}/{case_name}.ans"
        self.out_path = f"{TEMP_ROOT}/data/{problem_specific}/{case_name}.ans"
        self.dbg_path = f"{TEMP_ROOT}/data/{problem_specific}/{case_name}.log"


def compare_files(f1_path, f2_path):
    with open(f1_path, "r") as f1:
        f1_lines = list(line for line in f1)

    with open(f2_path, "r") as f2:
        f2_lines = list(line for line in f2)

    return f1_lines == f2_lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('sourcefile')
    parser.add_argument('--debug', '-d', choices=['console', 'file'])
    parser.add_argument('--case', default=None)
    args = parser.parse_args()

    filename_no_ext = os.path.splitext(args.sourcefile)[0]
    ext_no_dot = (os.path.splitext(args.sourcefile)[1])[1:]

    DATA_ROOT = "data"
    CODE_ROOT = ext_no_dot
    EXE_ROOT = "tmp/" + ext_no_dot
    TEMP_ROOT = "tmp"
    PYTHON = "python3"
    GO = "go"
    MONO = "mono"

    init(convert=True)

    problem = os.path.splitext(args.sourcefile)[0]
    underscore_idx = problem.rfind("_")
    if underscore_idx != -1:
        problem_no_underscore = problem[:underscore_idx]
    else:
        problem_no_underscore = problem

    data_path = DATA_ROOT + "/" + problem_no_underscore
    temp_path = TEMP_ROOT + "/data/" + problem

    if not os.path.exists(temp_path):
        os.makedirs(temp_path)

    if args.sourcefile.endswith(".py"):
        script_path = CODE_ROOT + "/" + args.sourcefile
        run_args = [PYTHON, script_path]
    elif args.sourcefile.endswith(".cpp"):
        run_args = [EXE_ROOT + "/" + problem]
    elif args.sourcefile.endswith(".c"):
        run_args = [EXE_ROOT + "/" + problem]
    elif args.sourcefile.endswith(".fs"):
        run_args = [MONO, EXE_ROOT + "/" + problem + ".exe"]
    elif args.sourcefile.endswith(".go"):
        run_args = [EXE_ROOT + "/" + problem]
    elif args.sourcefile.endswith(".cs"):
        run_args = [EXE_ROOT + "/" + problem]

    pathlib.Path(temp_path).mkdir(parents=True, exist_ok=True)

    in_search_path = data_path + "/*.in"
    in_files = glob.glob(in_search_path)
    case_names = [os.path.splitext(os.path.basename(x))[0] for x in in_files]
    cases = [TestCase(problem_no_underscore, problem, x) for x in case_names]
    cases = [tc for tc in cases if (args.case == None or args.case == tc.name)]

    for c in cases:
        dbg_file = None
        err = None

        if args.debug is None:
            err = subprocess.DEVNULL
        elif args.debug == 'file':
            dbg_file = open(c.dbg_path, "w")
            err = dbg_file

        with open(c.in_path, "r") as fin:
            with open(c.out_path, "w", newline="\n") as fout:
                start_time = timer()
                if err is not None:
                    subprocess.run(run_args, stdin=fin, stdout=fout, stderr=err)
                else:
                    subprocess.run(run_args, stdin=fin, stdout=fout)
                end_time = timer()
                elapsed_ms = (end_time - start_time) * 1000.0

        if dbg_file is not None:
            dbg_file.close()

        match = compare_files(c.ans_path, c.out_path)

        report_str = f"{c.name:20} "
        if match:
            report_str += f"{Fore.GREEN}PASS{Style.RESET_ALL} "
        else:
            report_str += f"{Fore.RED}FAIL{Style.RESET_ALL} "
        report_str += f"{round(elapsed_ms, 1):15} ms"

        print(report_str)
