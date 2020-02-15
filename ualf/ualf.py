'''UALF data parsing class'''
class Ualf:

    def  __init__(self, ualf_coordinates):
        self.read_ualf(ualf_coordinates)

    def read_ualf(self, ualf_coordinates):
        ualf_coordinates = list(ualf_coordinates)
        self.version = int(ualf_coordinates[0])
        self.year = int(''.join(ualf_coordinates[2:6]))
        self.month = int(''.join(ualf_coordinates[7:10]))
        self.day = int(''.join(ualf_coordinates[10:13]))
        self.hour = int(''.join(ualf_coordinates[13:15]))
        self.minutes = int(''.join(ualf_coordinates[15:18]))
        self.seconds = int(''.join(ualf_coordinates[18:21]))
        self.nanoseconds = int(''.join(ualf_coordinates[21:31]))
        self.latitude = float(''.join(ualf_coordinates[31:39]))
        self.longitude = float(''.join(ualf_coordinates[39:47]))
        self.peak_current = int(''.join(ualf_coordinates[47:51]))
        self.multiplicity = int(''.join(ualf_coordinates[51:53]))
        self.number_of_sensors = int(''.join(ualf_coordinates[53:56]))
        self.degrees_of_freedom = int(''.join(ualf_coordinates[56:59]))
        self.ellipse_angle = float(''.join(ualf_coordinates[59:66]))
        self.semi_major_axis = float(''.join(ualf_coordinates[66:71]))
        self.semi_minor_axis = float(''.join(ualf_coordinates[71:75]))
        self.chi_square_value = float(''.join(ualf_coordinates[76:81]))
        self.rise_time = float(''.join(ualf_coordinates[81:86]))
        self.peak_to_zero_time = float(''.join(ualf_coordinates[86:91]))
        self.max_rate_of_rise = float(''.join(ualf_coordinates[91:96]))
        self.cloud_indicator = int(''.join(ualf_coordinates[96:98]))
        self.angle_indicator = int(''.join(ualf_coordinates[98:100]))
        self.signal_indicator = int(''.join(ualf_coordinates[100:102]))
        self.timing_indicator = int(''.join(ualf_coordinates[102:104]))
        self.ualf_dict = self.make_ualf_dict()
    def make_ualf_dict(self):
        ualf_dict = {
            "version" : self.version,
            "year" : self.year,
            "month" : self.month,
            "day" : self.day,
            "hour" : self.hour,
            "minutes" : self.minutes,
            "seconds" : self.seconds,
            "nanoseconds" : self.nanoseconds,
            "latitude" : self.latitude,
            "longitude" : self.longitude,
            "peak_current" : self.peak_current,
            "multiplicity" : self.multiplicity,
            "number_of_sensors" : self.number_of_sensors,
            "degrees_of_freedom" : self.degrees_of_freedom,
            "semi_major_axis" : self.semi_major_axis,
            "semi_minor_axis" : self.semi_minor_axis,
            "chi_square_value" : self.chi_square_value,
            "rise_time" : self.rise_time,
            "peak_to_zero_time" : self.peak_to_zero_time,
            "max_rate_of_rise" : self.max_rate_of_rise,
            "cloud_indicator" : self.cloud_indicator,
            "signal_indicator" : self.signal_indicator,
            "timing_indicator" : self.timing_indicator}
        return ualf_dict
    def parse(self):
        return self.ualf_dict
    def print_ualf(self):
        print(self.ualf_dict)
