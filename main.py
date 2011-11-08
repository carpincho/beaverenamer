#!/usr/bin/env python
import os
import re

PATH_TO_DIR = "."
extension_allowed = ['.mp4', '.avi', '.srt']


def get_name_from_filename(filename):
    """
    Get name without file extension.
    """
    return filename[:-4]


def get_extension_from_filename(filename):
    """
    Get extension from filename.
    """
    return filename[-4:]


def get_accepted_and_ommited_files(files):
    """
    Splits allowed files from not allowed.
    Returns: ([allowed files],[not_allowed files])
    """
    assert len(files) > 0, "ERROR: get_accepted_and_ommited_files(). No files"
    allowed = []
    not_allowed = []
    for file in files:
        if is_file_allowed(file):
            allowed.append(file)
        else:
            not_allowed.append(file)
    return (allowed, not_allowed)


def is_file_allowed(filename):
    """
    Determine if a file is allowed to be renamed.
    """
    allowed = False
    file_ext = get_extension_from_filename(filename)
    for ext in extension_allowed:
        if file_ext == ext:
            allowed = True
            break
    return allowed


def remove_extra_spaces(filename):
    """
    Remove doble spaces from 'filename'.
    """
    name = get_name_from_filename(filename)
    ext = get_extension_from_filename(filename)

    new_name = ' '.join(name.split())

    return new_name + ext


def replace_underscore(filename):
    """
    Replace all '_' with a space from 'filename'.
    """
    name = get_name_from_filename(filename)
    ext = get_extension_from_filename(filename)
    old, new = '_', ' '

    new_name = name.replace(old, new)

    return new_name + ext


def replace_dots(filename):
    """
    Replace all '.' with space from 'filename'.
    """
    name = get_name_from_filename(filename)
    ext = get_extension_from_filename(filename)
    old, new = ".", " "

    new_name = name.replace(old, new)

    return new_name + ext


def lower_case(filename):
    """
    Convert filaname to lower. This include the extension too
    """
    return filename.lower()


def remove_url_patterns(filename, pattern):
    """
    Remove pattern from filename."
    """
    name = get_name_from_filename(filename)
    ext = get_extension_from_filename(filename)
    repl = " "
    new_name = re.sub(pattern, repl, name)

    return new_name + ext


if __name__ == '__main__':

    files = os.listdir(PATH_TO_DIR)
    accepted, not_accepted = get_accepted_and_ommited_files(files)

    print "Accepted files: %s" % accepted
    print "Not Accepted files %s " % not_accepted
