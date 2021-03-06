"""
Class Features:

Name:          drv_adapter_rs_geo
Author(s):     Fabio Delogu (fabio.delogu@cimafoundation.org)
Date:          '20220301'
Version:       '1.0.0'
"""

#######################################################################################
# Libraries
import logging
import os
import numpy as np

from lib_utils_geo import read_data_section

from lib_info_args import logger_name

# Logging
log_stream = logging.getLogger(logger_name)
#######################################################################################


# -------------------------------------------------------------------------------------
# Class driver geographical data
class DriverGeo:

    def __init__(self, src_dict, dst_dict=None, tag_geo_sections='sections'):

        self.src_dict = src_dict
        self.dst_dict = dst_dict

        self.tag_geo_sections = tag_geo_sections
        self.tag_folder_name = 'folder_name'
        self.tag_file_name = 'file_name'

        self.folder_name = self.src_dict[self.tag_geo_sections][self.tag_folder_name]
        self.file_name = self.src_dict[self.tag_geo_sections][self.tag_file_name]

        self.file_path = os.path.join(self.folder_name, self.file_name)

        self.columns_name_expected = ['HMC_X', 'HMC_Y', 'LON', 'LAT',
                                      'BASIN', 'SEC_NAME', 'SEC_RS', 'SEC_TAG', 'TYPE', 'AREA', 'Q_THR1', 'Q_THR2',
                                      'ADMIN_B_L1', 'ADMIN_B_L2', 'ADMIN_B_L3']
        self.columns_name_type = [np.int, np.int, np.float, np.float,
                                  str, str, str, str, str, np.float, np.float, np.float,
                                  str, str, str]

        self.columns_name_tag = ['hmc_id_x', 'hmc_id_y', 'longitude', 'latitude',
                                 'catchment', 'name', 'code', 'tag', 'type', 'area', 'discharge_thr1', 'discharge_thr2',
                                 'boundary_limit_01', 'boundary_limit_02', 'boundary_limit_03']

    # Method to read sections datasets
    def read_data(self):

        log_stream.info(' ----> Get static datasets ... ')

        log_stream.info(' -----> Read sections file ' + self.file_name + ' ... ')
        if os.path.exists(self.file_path):

            sections_obj = read_data_section(self.file_path,
                                             columns_name_expected=self.columns_name_expected,
                                             columns_name_type=self.columns_name_type,
                                             columns_name_tag=self.columns_name_tag)
            log_stream.info(' -----> Read sections file ' + self.file_name + ' ... DONE')
        else:
            log_stream.error(' -----> Read sections file ' + self.file_name + ' ... FAILED')
            raise IOError('File does not exist')

        log_stream.info(' ----> Get static datasets ... DONE')

        return sections_obj
# -------------------------------------------------------------------------------------
