#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from codecs import open
import os, ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

"""
CS 188 Local Submission Autograder
Written by the CS 188 Staff

==============================================================================
   _____ _              _ 
  / ____| |            | |
 | (___ | |_ ___  _ __ | |
  \___ \| __/ _ \| '_ \| |
  ____) | || (_) | |_) |_|
 |_____/ \__\___/| .__/(_)
                 | |      
                 |_|      

Modifying or tampering with this file is a violation of course policy.
If you're having trouble running the autograder, please contact the staff.
==============================================================================
"""
import bz2, base64

exec(bz2.decompress(base64.b64decode(
    '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')))