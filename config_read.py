import configparser
class ConfigRead:
    def __init__(self,config_path):
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)
    def get_time_round(self):
        return self.cf.getint("USER","time_round")
    def get_num_round_two(self):
        return self.cf.getint("DAILY","round_total_two")
    def get_num_round_single(self):
        return self.cf.getint("DAILY","round_total_single")
    def get_horizontal_pos(self):
        return  self.cf.getint("SYSTEM","horizontal_pos_relative")
    def get_vertical_pos(self):
        return self.cf.getint("SYSTEM","vertical_pos_relative")