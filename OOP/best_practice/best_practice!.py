import pandas as pd
import numpy as np
import an_filled as an
import logging
class WeddingPlanner:
    def __init__(self):
        self.m_s_date=''
        self.m_s_kallah_family=''
        self.m_s_color='none'
        self.m_s_hall=''
    def book_hall(self,s_hall,s_date):
        self.m_s_hall=s_hall
        self.m_s_date=s_date
class Weddings:
    def __init__(self) -> None:
        self.m_s_input_path=an.INFO_FOLDER
        self.m_df_halls=pd.DataFrame()
        self.m_df_families=pd.DataFrame()
        self.m_df_colors=pd.DataFrame()
    def load_file(self,s_path,s_file_name):
        df_file=pd.DataFrame()
        if (not s_path) or (not s_file_name):
            logging.error('file name or path is empty' + s_file_name)
            return False,df_file
        s_path=self.m_s_input_path+'/'+s_file_name
        try:
            df_file=pd.read_csv(s_path)
        except:
            logging.error('cannot load wedding file' + s_file_name)
            return False,df_file
        return True, df_file
    def load_halls(self):
        b_success=True
        b_success,self.m_df_halls=self.load_file(self.m_s_input_path,an.HALLS_INFO_FILE)
        return b_success
    def load_families(self):
        b_success=True
        b_success,self.m_df_families=self.load_file(self.m_s_input_path,an.FAMILIES_INFO_FILE)
        return b_success
    def load_colors(self):
        b_success=True
        b_success,self.m_df_colors=self.load_file(self.m_s_input_path,an.COLORS_INFO_FILE)
        return b_success
    def load_wedding_info(self):
        b_success=True
        b_success=self.load_families()
        if not b_success:
            b_success=False
            logging.error('cannot load families')
        if b_success:
            b_success=self.load_halls()
            b_success=self.load_colors()
        else:
            logging.error('not booking halls or colors as there are no familes loaded')
        return b_success