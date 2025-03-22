"""

Python bindings for GLFW.
"""
import __future__
from __future__ import annotations
import ctypes as ctypes
import glob as glob
import os as os
import subprocess as subprocess
import sys as sys
import textwrap as textwrap
__all__ = ['ctypes', 'division', 'glfw', 'glob', 'os', 'print_function', 'subprocess', 'sys', 'textwrap', 'unicode_literals']
def _find_library_candidates(library_names, library_file_extensions, library_search_paths):
    """
    
        Finds and returns filenames which might be the library you are looking for.
        
    """
def _get_frozen_library_search_paths():
    """
    
        Returns a list of library search paths for frozen executables.
        
    """
def _get_library_search_paths():
    """
    
        Returns a list of library search paths, considering of the current working
        directory, default paths and paths from environment variables.
        
    """
def _get_package_path_variant(package_path):
    ...
def _glfw_get_version(filename):
    """
    
        Queries and returns the library version tuple or None by using a
        subprocess.
        
    """
def _load_first_library(library_names, library_file_extensions, library_search_paths):
    """
    
        Finds, loads and returns the first found version of the library.
        
    """
def _load_library(library_names, library_file_extensions, library_search_paths, version_check_callback):
    """
    
        Finds, loads and returns the most recent version of the library.
        
    """
division: __future__._Feature  # value = _Feature((2, 2, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 131072)
glfw: ctypes.CDLL  # value = <CDLL '/usr/lib/libglfw.so.3.4', handle 294ff860 at 0x7ef23226e720>
print_function: __future__._Feature  # value = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 1048576)
unicode_literals: __future__._Feature  # value = _Feature((2, 6, 0, 'alpha', 2), (3, 0, 0, 'alpha', 0), 2097152)
