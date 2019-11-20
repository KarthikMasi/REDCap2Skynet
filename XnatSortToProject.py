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

def redcap_project_access(API_KEY):
    """
    Access point to REDCap form
    :param API_KEY:string with REDCap database API_KEY
    :return: redcap Project Object
    """
    try:
        project = redcap.Project('https://redcap.vanderbilt.edu/api/', API_KEY)
    except:
        LOGGER.error('ERROR: Could not access redcap. Either wrong API_URL/API_KEY or redcap down.')
        sys.exit(1)
    return project

