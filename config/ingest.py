from lsst.obs.t80cam.ingest import T80camParseTask

config.parse.retarget(T80camParseTask)

config.parse.translation = {
    'expTime': 'EXPTIME',
    'object': 'OBJECT',
    'imageType': 'IMAGETYP',
    'testType': 'TESTTYPE',
    'filter': 'FILTER',
#    'lsstSerial': 'DETECTOR',
    'date': 'DATE',
    'dateObs': 'DATE',
}
config.parse.translators = {
    'visit': 'translate_visit',
    'wavelength': 'translate_wavelength',
}
config.parse.defaults = {
    'run': "UNKNOWN",
    'visit': "0",
    'basename': "UNKNOWN",
    'filter': "o",
    'date': "UNKNOWN",
    'dateObs': "UNKNOWN",
    'expTime': "30.0",
    'ccd': "0",
    'object': "UNKNOWN",
    'imageType': "Object",
    'testType': "UNKNOWN",
#    'lsstSerial': "bstalder",
    'field': "UNKNOWN",
    'wavelength': "650",
}
config.parse.hdu = 0

config.register.columns = {
    'run': 'text',
    'visit': 'int',
    'basename': 'text',
    'filter': 'text',
    'date': 'text',
    'dateObs': 'text',
    'expTime': 'double',
    'ccd': 'int',
    'object': 'text',
    'imageType': 'text',
    'testType': 'text',
#    'lsstSerial': 'text',
    'field': 'text',
    'wavelength': 'int',
}
# this can be cut down if the registry becomes impractically large
config.register.visit = list(config.register.columns.keys())

config.register.unique = ['visit']
