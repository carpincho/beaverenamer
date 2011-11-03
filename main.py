#!/usr/bin/env python
import os

PATH_TO_DIR = "."
extention_allowed = ['.mp4', '.avi', '.srt']


def get_accepted_and_ommited_files(files):
    """
    Splits allowed files from not allowed.
    Returns: ([allowed files],[not_allowed files])
    """
#    assert len(files) > 0, "ERROR: get_accepted_and_ommited_files(). No files"
    allowed = []
    not_allowed = []
    for file in files:
        if is_file_allowed(file):
            allowed.append(file)
        else:
            not_allowed.append(file)
    return (allowed, not_allowed)


def is_file_allowed(file):
    """
    Determine if a file is allowed to be renamed.
    """
    allowed = False
    file_ext = file[-4:]
    for ext in extention_allowed:
        if file_ext == ext:
            allowed = True
            break
    return allowed

if __name__ == '__main__':

    files = os.listdir(PATH_TO_DIR)
    accepted, not_accepted = get_accepted_and_ommited_files([])

    print "Accepted files: %s" % accepted
    print "Not Accepted files %s " % not_accepted
