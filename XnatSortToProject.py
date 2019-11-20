#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Check for new entries on REDCap and upload to animal XNAT

Created on Nov 20, 2019

@author: Karthik Ramadass
'''

import redcap
import dax
import sys
import logging as LOGGER

