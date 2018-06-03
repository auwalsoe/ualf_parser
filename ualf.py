class ualf:
	version = None
	date = None    
	year = None 
	month = None 
	day = None 
	hour = None 
	minutes = None 
	seconds = None 
	nanoseconds = None 
	latitude = None 
	longitude = None 
	peakCurrent = None 
	multiplicity = None 
	numberOfSensors = None   
	degreesOfFreedom = None
	ellipseAngle = None
	semiMajorAxis = None
	semiMinorAxis = None
	chiSquareValue = None
	riseTime = None
	peakToZeroTime = None
	maxRateOfRise = None
	cloudIndicator = None
	angleIndicator = None
	signalIndicator = None
	timingIndicator = None

	ualf_dict = None
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
		self.peakCurrent = int(''.join(ualf_coordinates[47:51]))
		self.multiplicity = int(''.join(ualf_coordinates[51:53]))
		self.numberOfSensors = int(''.join(ualf_coordinates[53:56]))
		self.degreesOfFreedom = int(''.join(ualf_coordinates[56:59]))
		self.ellipseAngle = float(''.join(ualf_coordinates[59:66]))
		self.semiMajorAxis = float(''.join(ualf_coordinates[66:71]))
		self.semiMinorAxis = float(''.join(ualf_coordinates[71:75]))
		self.chiSquareValue = float(''.join(ualf_coordinates[76:81]))
		self.riseTime = float(''.join(ualf_coordinates[81:86]))
		self.peakToZeroTime = float(''.join(ualf_coordinates[86:91]))
		self.maxRateOfRise = float(''.join(ualf_coordinates[91:96]))
		self.cloudIndicator = int(''.join(ualf_coordinates[96:98]))
		self.angleIndicator = int(''.join(ualf_coordinates[98:100]))
		self.signalIndicator = int(''.join(ualf_coordinates[100:102]))
		self.timingIndicator = int(''.join(ualf_coordinates[102:104]))
		self.make_ualf_dict()
	def make_ualf_dict(self):
		self.ualf_dict={
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
		"peakCurrent" : self.peakCurrent,
		"multiplicity" : self.multiplicity,
		"numberOfSensors" : self.numberOfSensors,
		"degreesOfFreedom" : self.degreesOfFreedom,
		"semiMajorAxis" : self.semiMajorAxis,
		"semiMinorAxis" : self.semiMinorAxis,
		"chiSquareValue" : self.chiSquareValue,
		"riseTime" : self.riseTime,
		"peakToZeroTime" : self.peakToZeroTime,
		"maxRateOfRise" : self.maxRateOfRise,
		"cloudIndicator" : self.cloudIndicator,
		"signalIndicator" : self.signalIndicator,
		"timingIndicator" : self.timingIndicator
		}
	def parse(self):
		return self.ualf_dict
	def print_ualf(self):
		print(self.ualf_dict)

