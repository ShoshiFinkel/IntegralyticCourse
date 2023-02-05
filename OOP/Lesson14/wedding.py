import pandas as pd
import an_filled as an
import logging

logging.basicConfig(filename= an.LOG_FOLDER + an.LOG_FILE,
                    filemode='a+',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)

class WeddingPlanner:
    def __init__(self) -> None:
        self.m_s_date = ''
        self.m_s_kalla_family = ''
        self.m_s_color_scheme = 'none'
        self.m_s_hall = ''
    
    def book_hall(self, s_hall, s_date):

        self.m_s_date = s_date
        self.m_s_hall =  s_hall

class Weddings:

    def __init__(self) -> None:

        self.m_s_input_path = an.INFO_FOLDER

        self.m_df_halls = pd.DataFrame()
        self.m_df_families = pd.DataFrame()
        self.m_df_colors = pd.DataFrame()

    def load_file(self, s_path, s_file_name):

        df_file = pd.DataFrame()
        if (not s_path) or (not s_file_name):
            logging.error('The file name or path came up empty. Filename: ' + s_file_name + ' Path: ' + s_path)
            return False, df_file
        s_path = s_path + '/' + s_file_name
        try:
            df_file = pd.read_csv(s_path)
        except:
            logging.error('cannot load wedding file: ' + s_path)
            return False, df_file

        return True, df_file

    def load_halls(self):

        b_success = True
        b_success, self.m_df_halls = self.load_file(self.m_s_input_path, an.HALLS_INFO_FILE)
        return b_success


    def load_families(self):

        #b_success = True
        b_success, self.m_df_families = self.load_file(self.m_s_input_path, an.FAMILIES_INFO_FILE)
        if self.m_df_families.empty:
            logging.error('We loaded the family file successfully but it came in empty')
        return b_success

    def load_colors(self): 

        b_success = True
        b_success, self.m_df_colors = self.load_file(self.m_s_input_path, an.COLORS_INFO_FILE)
        return b_success

    def load_wedding_info(self):

        b_success = True
        b_success = self.load_families()
        if not b_success:
            b_success = False
            logging.error('Families did not load')
            
        if b_success:
            b_success = self.load_halls()
            b_success = self.load_colors()
        else:
            logging.error('not booking halls or choosing colors because there are no families loaded')    
        return b_success    

                
        


