# this code was automatically translated to python from the official JS decoder provided by advantech,
# that can be found here https://advdownload.advantech.com/productfile/Downloadfile3/1-28WM7I8/PayloadParser_V1.6.12.js

__all__ = ['decoder_advantech_wise_2140']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['MASK_PAYLOAD_SENSOR_AXIS_Z_MASK', 'MASK_PAYLOAD_SENSOR_TEMP_F_TYPE', 'convertToSignedInt32', 'MASK_PAYLOAD_SENSOR_MASK2_LOGINDEX', 'translateInt24', 'MASK_HEADER_ADDRESS_NONE', 'MASK_PAYLOAD_AI_MASK2_RANGE', 'MASK_PAYLOAD_REGISTER_STATUS', 'MASK_PAYLOAD_SENSOR_MASSIVE_DATA_TYPE_MASSIVE_TYPE_FFT', 'version', 'MASK_PAYLOAD_AI_STATUS', 'MASK_PAYLOAD_SENSOR_ACCELERATOR_TYPE_MS2', 'MASK_DEVICE_POSITION_LATITUDE', 'MASK_PAYLOAD_DO_STATUS', 'MASK_PAYLOAD_DO_ABSOLUTE_PULSE_OUTPUT', 'MASK_PAYLOAD_AI_MAX_VALUE', 'registerParse', 'hexArr', 'decode', 'MASK_PAYLOAD_SENSOR_AXIS_X_MASK', 'MASK_DEVICE_POWER_SOURCE', 'PAYLOAD_AI_DATA', 'MASK_PAYLOAD_SENSOR_EXTMASK_VELOCITY', 'convertMaskToArray', 'MASK_PAYLOAD_COIL_STATUS', 'MASK_HEADER_ADDRESS_MODE', 'MASK_PAYLOAD_COIL_MULTI_CH', 'MASK_PAYLOAD_SENSOR_MASSIVE_DATA_TYPE_SAMPLE_PER_AXIS', 'MASK_PAYLOAD_DI_STATUS', 'MASK_PAYLOAD_SENSOR_MASSIVE_DATA_TYPE_MASSIVE_TYPE', 'MASK_DEVICE_POSITION', 'MASK_PAYLOAD_SENSOR_EXTMASK_KURTOSIS', 'PAYLOAD_REGISTER_DATA', 'getSourceAddressLength', 'MASK_PAYLOAD_SENSOR_EXTMASK_MASSIVE_DATA_SEC', 'CrcCalc', 'MASK_PAYLOAD_SENSOR_EXTMASK_PEAK', 'MASK_PAYLOAD_COIL_VALUE', 'MASK_DEVICE_TIMESTAMP', 'checkFrameLength', 'DIParse', 'MASK_PAYLOAD_SENSOR_MASK2_TIME', 'MASK_PAYLOAD_AI_RAW_VALUE', 'MASK_PAYLOAD_SENSOR_EXTMASK_B', 'MASK_DEVICE_BATTERY_LEVEL', 'MASK_PAYLOAD_SENSOR_MASSIVE_DATA_TYPE_BYTES_PER_SAMPLE', 'MASK_PAYLOAD_REGISTER_VALUE', 'MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_EVENT', 'MASK_DEVICE_POSITION_LONGITUDE', 'coilParse', 'MIN_FRAME_LENGTH', 'PAYLOAD_DO_DATA', 'arrLength', 'DI_MODE_FREQUENCY', 'MASK_PAYLOAD_REGISTER_MULTI_CH', 'MASK_HEADER_ADDRESS_2_OCTECT', 'arrayIndex', 'deviceParse', 'AIParse', 'PAYLOAD_COIL_DATA', 'PAYLOAD_DEVICE_DATA', 'MASK_PAYLOAD_SENSOR_EXTMASK_STDDEVIATION', 'PAYLOAD_SENSOR_DATA', 'MASK_PAYLOAD_SENSOR_ACCELERATOR_TYPE_G', 'MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_MAX_VALUE', 'parsePayLoad', 'MASK_PAYLOAD_SENSOR_EXTMASK_RMS', 'MASK_PAYLOAD_SENSOR_EXTMASK_CRESTFACTOR', 'MASK_HEADER_FRAME_VERSION', 'MASK_DEVICE_EVENT', 'i', 'MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_MIN_VALUE', 'MASK_PAYLOAD_AI_EVENT', 'MASK_HEADER_ADDRESS_8_OCTECT', 'addZero', 'MASK_PAYLOAD_SENSOR_AXIS_Y_MASK', 'translateInt16', 'MASK_PAYLOAD_SENSOR_EXTMASK_MASSIVE_DATA_LOG', 'message', 'MASK_PAYLOAD_DI_VALUE', 'MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_STATUS', 'sensorParse', 'checkPayloadLengthAndSetStorage', 'MASK_PAYLOAD_SENSOR_HUMIDITY_TYPE', 'MASK_PAYLOAD_AI_MIN_VALUE', 'MASK_PAYLOAD_DO_INCREMENTAL_PULSE_OUTPUT', 'parseAxisData', 'MASK_PAYLOAD_SENSOR_EXTMASK_SKEWNESS', 'csvMessage', 'convertToSignedInt16', 'MASK_PAYLOAD_SENSOR_TEMP_C_TYPE', 'MASK_PAYLOAD_DI_EVENT', 'translateInt32', 'PAYLOAD_DI_DATA', 'lostPacketInfo', 'hexPayloadArr', 'MASK_PAYLOAD_SENSOR_EXTMASK_MASSIVE_DATA_INFO', 'au8CRC8_Pol07_Table', 'MASK_HEADER_FIRST_SEGMENT', 'DOParse', 'MASK_PAYLOAD_SENSOR_EXTMASK_DISPLACEMENT', 'MASK_PAYLOAD_SENSOR_TEMP_K_TYPE', 'MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_VALUE', 'MASK_DEVICE_BATTERY_VOLTAGE'])
@Js
def PyJsHoisted_addZero_(i, this, arguments, var=var):
    var = Scope({'i':i, 'this':this, 'arguments':arguments}, var)
    var.registers(['i'])
    var.put('i', (var.get('i')+Js('')))
    if (var.get('i').get('length')<Js(2.0)):
        var.put('i', (Js('0')+var.get('i')))
    return var.get('i')
PyJsHoisted_addZero_.func_name = 'addZero'
var.put('addZero', PyJsHoisted_addZero_)
@Js
def PyJsHoisted_translateInt32_(a, b, c, d, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'd':d, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'c', 'b', 'd'])
    return ((((var.get('d')<<Js(24.0))+(var.get('c')<<Js(16.0)))+(var.get('b')<<Js(8.0)))+var.get('a'))
PyJsHoisted_translateInt32_.func_name = 'translateInt32'
var.put('translateInt32', PyJsHoisted_translateInt32_)
@Js
def PyJsHoisted_translateInt24_(a, b, c, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'c':c, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'c', 'b'])
    return (((var.get('c')<<Js(16.0))+(var.get('b')<<Js(8.0)))+var.get('a'))
PyJsHoisted_translateInt24_.func_name = 'translateInt24'
var.put('translateInt24', PyJsHoisted_translateInt24_)
@Js
def PyJsHoisted_translateInt16_(a, b, this, arguments, var=var):
    var = Scope({'a':a, 'b':b, 'this':this, 'arguments':arguments}, var)
    var.registers(['a', 'b'])
    return (var.get('a')+(var.get('b')<<Js(8.0)))
PyJsHoisted_translateInt16_.func_name = 'translateInt16'
var.put('translateInt16', PyJsHoisted_translateInt16_)
@Js
def PyJsHoisted_convertMaskToArray_(number, channelCount, this, arguments, var=var):
    var = Scope({'number':number, 'channelCount':channelCount, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'number', 'biArray', 'temp', 'channelCount'])
    var.put('biArray', Js([]))
    pass
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('channelCount')):
        var.put('temp', var.get('number'))
        var.put('temp', (var.get('temp')>>var.get('i')))
        var.get('biArray').callprop('push', (var.get('temp')&Js(1.0)))
        # update
        var.put('i',Js(var.get('i').to_number())+Js(1))
    return var.get('biArray')
PyJsHoisted_convertMaskToArray_.func_name = 'convertMaskToArray'
var.put('convertMaskToArray', PyJsHoisted_convertMaskToArray_)
@Js
def PyJsHoisted_convertToSignedInt16_(number, this, arguments, var=var):
    var = Scope({'number':number, 'this':this, 'arguments':arguments}, var)
    var.registers(['number'])
    if ((var.get('number')&Js(32768))>Js(0.0)):
        var.put('number', (var.get('number')-Js(65536)))
    return var.get('number')
PyJsHoisted_convertToSignedInt16_.func_name = 'convertToSignedInt16'
var.put('convertToSignedInt16', PyJsHoisted_convertToSignedInt16_)
@Js
def PyJsHoisted_convertToSignedInt32_(number, this, arguments, var=var):
    var = Scope({'number':number, 'this':this, 'arguments':arguments}, var)
    var.registers(['number'])
    if ((var.get('number')&Js(2147483648))>Js(0.0)):
        var.put('number', (var.get('number')-Js(4294967296)))
    return var.get('number')
PyJsHoisted_convertToSignedInt32_.func_name = 'convertToSignedInt32'
var.put('convertToSignedInt32', PyJsHoisted_convertToSignedInt32_)
@Js
def PyJsHoisted_parseAxisData_(index, bIsSensorEventExist, extMask, jsonObj, this, arguments, var=var):
    var = Scope({'index':index, 'bIsSensorEventExist':bIsSensorEventExist, 'extMask':extMask, 'jsonObj':jsonObj, 'this':this, 'arguments':arguments}, var)
    var.registers(['jsonObj', 'index', 'extMask', 'bIsSensorEventExist'])
    if var.get('bIsSensorEventExist'):
        var.get('jsonObj').put('SenEvent', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
    if (var.get('extMask')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_VELOCITY')):
        var.get('jsonObj').put('OAVelocity', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
    if (var.get('extMask')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_PEAK')):
        var.get('jsonObj').put('Peakmg', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
    if (var.get('extMask')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_RMS')):
        var.get('jsonObj').put('RMSmg', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
    if (var.get('extMask')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_KURTOSIS')):
        var.get('jsonObj').put('Kurtosis', var.get('convertToSignedInt16')(var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))))
    if (var.get('extMask')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_CRESTFACTOR')):
        var.get('jsonObj').put('CrestFactor', var.get('convertToSignedInt16')(var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))))
    if (var.get('extMask')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_SKEWNESS')):
        var.get('jsonObj').put('Skewness', var.get('convertToSignedInt16')(var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))))
    if (var.get('extMask')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_STDDEVIATION')):
        var.get('jsonObj').put('Deviation', var.get('convertToSignedInt16')(var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))))
    if (var.get('extMask')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_DISPLACEMENT')):
        var.get('jsonObj').put('Peak-to-Peak Displacement', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
    return var.get('index')
PyJsHoisted_parseAxisData_.func_name = 'parseAxisData'
var.put('parseAxisData', PyJsHoisted_parseAxisData_)
@Js
def PyJsHoisted_DIParse_(index, this, arguments, var=var):
    var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
    var.registers(['length', 'index', 'channel', 'channelMask', 'channelIndex', 'arrBinary', 'mode'])
    pass
    var.put('mode', (var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))&Js(15)))
    if (var.get('version')>Js(0.0)):
        var.put('length', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
    var.put('channel', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
    if (var.get('version')>Js(0.0)):
        var.put('length', Js(1.0), '-')
    var.put('channelIndex', ((var.get('channel')&Js(224))>>Js(5.0)))
    var.put('channelMask', (var.get('channel')&Js(7)))
    var.get('message').put((Js('DI')+var.get('channelIndex')), Js({}))
    if (var.get('channelMask')&var.get('MASK_PAYLOAD_DI_STATUS')):
        var.put('arrBinary', var.get('convertMaskToArray')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), Js(8.0)))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(1.0), '-')
        var.get('message').get((Js('DI')+var.get('channelIndex'))).put('status', Js({}))
        var.get('message').get((Js('DI')+var.get('channelIndex'))).get('status').put('Signal Logic', var.get('arrBinary').get('0'))
        var.get('message').get((Js('DI')+var.get('channelIndex'))).get('status').put('Start Counter', var.get('arrBinary').get('1'))
        var.get('message').get((Js('DI')+var.get('channelIndex'))).get('status').put('Get/Clean Counter Overflow', var.get('arrBinary').get('2'))
        var.get('message').get((Js('DI')+var.get('channelIndex'))).get('status').put('Get/Clean L2H Latch', var.get('arrBinary').get('4'))
        var.get('message').get((Js('DI')+var.get('channelIndex'))).get('status').put('Get/Clean H2L Latch', var.get('arrBinary').get('5'))
    var.get('message').get((Js('DI')+var.get('channelIndex'))).put('mode', var.get('mode'))
    if (var.get('channelMask')&var.get('MASK_PAYLOAD_DI_VALUE')):
        if (var.get('mode')==var.get('DI_MODE_FREQUENCY')):
            def PyJs_LONG_0_(var=var):
                return var.get('message').get((Js('DI')+var.get('channelIndex'))).put('Frequency_Value', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
            PyJs_LONG_0_()
        else:
            def PyJs_LONG_1_(var=var):
                return var.get('message').get((Js('DI')+var.get('channelIndex'))).put('Counter_Value', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
            PyJs_LONG_1_()
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(4.0), '-')
    if (var.get('channelMask')&var.get('MASK_PAYLOAD_DI_EVENT')):
        var.get('message').get((Js('DI')+var.get('channelIndex'))).put('Event', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(1.0), '-')
    if (var.get('version')>Js(0.0)):
        if (var.get('length')>Js(0.0)):
            var.put('index', var.get('length'), '+')
    return var.get('index')
PyJsHoisted_DIParse_.func_name = 'DIParse'
var.put('DIParse', PyJsHoisted_DIParse_)
@Js
def PyJsHoisted_DOParse_(index, this, arguments, var=var):
    var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
    var.registers(['length', 'modeText', 'index', 'status', 'channel', 'channelMask', 'channelIndex', 'mode'])
    pass
    var.put('mode', (var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))&Js(15)))
    if (var.get('version')>Js(0.0)):
        var.put('length', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
    var.put('channel', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
    if (var.get('version')>Js(0.0)):
        var.put('length', Js(1.0), '-')
    var.put('channelIndex', ((var.get('channel')&Js(224))>>Js(5.0)))
    var.put('channelMask', (var.get('channel')&Js(7)))
    var.get('message').put((Js('DO')+var.get('channelIndex')), Js({}))
    var.put('modeText', Js(''))
    while 1:
        SWITCHED = False
        CONDITION = (var.get('mode'))
        if SWITCHED or PyJsStrictEq(CONDITION, Js(0.0)):
            SWITCHED = True
            var.put('modeText', Js('DO'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(1.0)):
            SWITCHED = True
            var.put('modeText', Js('Pulse output'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(2.0)):
            SWITCHED = True
            var.put('modeText', Js('Low to High delay'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(3.0)):
            SWITCHED = True
            var.put('modeText', Js('High to Low delay'))
            break
        if SWITCHED or PyJsStrictEq(CONDITION, Js(4.0)):
            SWITCHED = True
            var.put('modeText', Js('AI alarm drive'))
            break
        SWITCHED = True
        break
    var.get('message').get((Js('DO')+var.get('channelIndex'))).put('Mode', var.get('modeText'))
    if (var.get('channelMask')&var.get('MASK_PAYLOAD_DO_STATUS')):
        var.put('status', var.get('convertMaskToArray')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), Js(8.0)))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(1.0), '-')
        var.get('message').get((Js('DO')+var.get('channelIndex'))).put('status', Js({}))
        var.get('message').get((Js('DO')+var.get('channelIndex'))).get('status').put('Signal Logic', var.get('status').get('0'))
        var.get('message').get((Js('DO')+var.get('channelIndex'))).get('status').put('Pulse Output Continue', var.get('status').get('1'))
    if (var.get('mode')==Js(1.0)):
        var.get('message').get((Js('DO')+var.get('channelIndex'))).put('PulsAbs', Js(0.0))
        var.get('message').get((Js('DO')+var.get('channelIndex'))).put('PulsInc', Js(0.0))
    if (var.get('channelMask')&var.get('MASK_PAYLOAD_DO_ABSOLUTE_PULSE_OUTPUT')):
        def PyJs_LONG_2_(var=var):
            return var.get('message').get((Js('DO')+var.get('channelIndex'))).put('PulsAbs', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
        PyJs_LONG_2_()
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(4.0), '-')
    if (var.get('channelMask')&var.get('MASK_PAYLOAD_DO_INCREMENTAL_PULSE_OUTPUT')):
        def PyJs_LONG_3_(var=var):
            return var.get('message').get((Js('DO')+var.get('channelIndex'))).put('PulsInc', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
        PyJs_LONG_3_()
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(4.0), '-')
    if (var.get('version')>Js(0.0)):
        if (var.get('length')>Js(0.0)):
            var.put('index', var.get('length'), '+')
    return var.get('index')
PyJsHoisted_DOParse_.func_name = 'DOParse'
var.put('DOParse', PyJsHoisted_DOParse_)
@Js
def PyJsHoisted_AIParse_(index, this, arguments, var=var):
    var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
    var.registers(['length', 'index', 'status', 'channel', 'channelMask', 'channelIndex', 'mask2', 'range'])
    pass
    var.put('range', (var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))&Js(15)))
    if (var.get('version')>Js(0.0)):
        var.put('length', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
    var.put('channel', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
    if (var.get('version')>Js(0.0)):
        var.put('length', Js(1.0), '-')
    var.put('channelIndex', ((var.get('channel')&Js(224))>>Js(5.0)))
    var.put('channelMask', (var.get('channel')&Js(31)))
    var.get('message').put((Js('AI')+var.get('channelIndex')), Js({}))
    var.get('message').get((Js('AI')+var.get('channelIndex'))).put('Range', var.get('range'))
    if (var.get('channelMask')&var.get('MASK_PAYLOAD_AI_STATUS')):
        var.put('status', var.get('convertMaskToArray')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), Js(8.0)))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(1.0), '-')
        var.get('message').get((Js('AI')+var.get('channelIndex'))).put('status', Js({}))
        var.get('message').get((Js('AI')+var.get('channelIndex'))).get('status').put('Low Alarm', var.get('status').get('0'))
        var.get('message').get((Js('AI')+var.get('channelIndex'))).get('status').put('High Alarm', var.get('status').get('1'))
    if (var.get('channelMask')&var.get('MASK_PAYLOAD_AI_RAW_VALUE')):
        var.get('message').get((Js('AI')+var.get('channelIndex'))).put('Raw Data', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(2.0), '-')
    if (var.get('channelMask')&var.get('MASK_PAYLOAD_AI_EVENT')):
        var.get('message').get((Js('AI')+var.get('channelIndex'))).put('Event', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(2.0), '-')
    if (var.get('channelMask')&var.get('MASK_PAYLOAD_AI_MAX_VALUE')):
        var.get('message').get((Js('AI')+var.get('channelIndex'))).put('MaxVal', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(2.0), '-')
    if (var.get('channelMask')&var.get('MASK_PAYLOAD_AI_MIN_VALUE')):
        var.get('message').get((Js('AI')+var.get('channelIndex'))).put('MinVal', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(2.0), '-')
    if ((var.get('version')>Js(0.0)) and (var.get('length')>Js(0.0))):
        var.put('mask2', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
        var.put('length', Js(1.0), '-')
        if (var.get('mask2')&var.get('MASK_PAYLOAD_AI_MASK2_RANGE')):
            var.get('message').get((Js('AI')+var.get('channelIndex'))).put('Range', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
            var.put('length', Js(1.0), '-')
        if (var.get('length')>Js(0.0)):
            var.put('index', var.get('length'), '+')
    return var.get('index')
PyJsHoisted_AIParse_.func_name = 'AIParse'
var.put('AIParse', PyJsHoisted_AIParse_)
@Js
def PyJsHoisted_sensorParse_(index, this, arguments, var=var):
    var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
    var.registers(['lastPayload', 'axisIndex', 'bytesPerSample', 'sampleRate', 'timestamp', 'logIndex', 'initialOffset', 'fillLength', 'axisData', 'mask2', 'range', 'length', 'lastOffset', 'axis', 'index', 'objData', 'axisType', 'samplesPerAxis', 'points', 'sampleFreq', 'dataType', 'sampleIndex', 'data', 'totalLength', 'arrAxisMask', 'massType', 'offset', 'intExtMaskEnable', 'i', 'FFTDataStorage', 'arrExtMask', 'intAxisMaskEnable', 'bytesPerAxis'])
    pass
    var.put('range', (var.get('hexArr').get(var.get('index'))&Js(15)))
    if (((PyJsStrictEq(var.get('range'),var.get('MASK_PAYLOAD_SENSOR_TEMP_C_TYPE')) or PyJsStrictEq(var.get('range'),var.get('MASK_PAYLOAD_SENSOR_TEMP_F_TYPE'))) or PyJsStrictEq(var.get('range'),var.get('MASK_PAYLOAD_SENSOR_TEMP_K_TYPE'))) or PyJsStrictEq(var.get('range'),var.get('MASK_PAYLOAD_SENSOR_HUMIDITY_TYPE'))):
        if (var.get('version')>Js(0.0)):
            (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
            var.put('length', var.get('hexArr').get(var.get('index')))
        var.get('message').put('TempHumi', Js({}))
        var.get('message').get('TempHumi').put('Range', var.get('range'))
        (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
        var.put('mask', (var.get('hexArr').get(var.get('index'))&Js(31)))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(1.0), '-')
        (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
        if (var.get('mask')&var.get('MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_STATUS')):
            var.get('message').get('TempHumi').put('Status', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
            if (var.get('version')>Js(0.0)):
                var.put('length', Js(1.0), '-')
        if (var.get('mask')&var.get('MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_EVENT')):
            var.get('message').get('TempHumi').put('Event', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
            if (var.get('version')>Js(0.0)):
                var.put('length', Js(2.0), '-')
        if (var.get('mask')&var.get('MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_VALUE')):
            if PyJsStrictEq(var.get('range'),var.get('MASK_PAYLOAD_SENSOR_HUMIDITY_TYPE')):
                def PyJs_LONG_4_(var=var):
                    return var.get('message').get('TempHumi').put('SenVal', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                PyJs_LONG_4_()
            else:
                def PyJs_LONG_5_(var=var):
                    return var.get('convertToSignedInt32')(var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                var.get('message').get('TempHumi').put('SenVal', PyJs_LONG_5_())
            if (var.get('version')>Js(0.0)):
                var.put('length', Js(4.0), '-')
        if (var.get('mask')&var.get('MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_MAX_VALUE')):
            def PyJs_LONG_6_(var=var):
                return var.get('message').get('TempHumi').put('SenMaxVal', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
            PyJs_LONG_6_()
            if (var.get('version')>Js(0.0)):
                var.put('length', Js(4.0), '-')
        if (var.get('mask')&var.get('MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_MIN_VALUE')):
            def PyJs_LONG_7_(var=var):
                return var.get('message').get('TempHumi').put('SenMinVal', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
            PyJs_LONG_7_()
            if (var.get('version')>Js(0.0)):
                var.put('length', Js(4.0), '-')
        if (var.get('version')>Js(0.0)):
            if (var.get('length')>Js(0.0)):
                var.put('index', var.get('length'), '+')
    if (PyJsStrictEq(var.get('range'),var.get('MASK_PAYLOAD_SENSOR_ACCELERATOR_TYPE_G')) or PyJsStrictEq(var.get('range'),var.get('MASK_PAYLOAD_SENSOR_ACCELERATOR_TYPE_MS2'))):
        var.put('bIsSensorEventExist', Js(False))
        if (var.get('version')>Js(0.0)):
            (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
            var.put('length', var.get('hexArr').get(var.get('index')))
        (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
        var.put('axisMask', ((var.get('hexArr').get(var.get('index'))&Js(224))>>Js(5.0)))
        var.put('arrAxisMask', var.get('convertMaskToArray')(var.get('axisMask'), Js(8.0)))
        var.put('intAxisMaskEnable', Js(0.0))
        @Js
        def PyJs_anonymous_8_(item, this, arguments, var=var):
            var = Scope({'item':item, 'this':this, 'arguments':arguments}, var)
            var.registers(['item'])
            if (var.get('item')==Js(1.0)):
                (var.put('intAxisMaskEnable',Js(var.get('intAxisMaskEnable').to_number())+Js(1))-Js(1))
        PyJs_anonymous_8_._set_name('anonymous')
        var.get('arrAxisMask').callprop('forEach', PyJs_anonymous_8_)
        var.put('mask', (var.get('hexArr').get(var.get('index'))&Js(31)))
        (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
        var.put('extMask', var.get('hexArr').get(var.get('index')))
        var.put('arrExtMask', var.get('convertMaskToArray')(var.get('extMask'), Js(8.0)))
        var.put('intExtMaskEnable', Js(0.0))
        @Js
        def PyJs_anonymous_9_(item, this, arguments, var=var):
            var = Scope({'item':item, 'this':this, 'arguments':arguments}, var)
            var.registers(['item'])
            if (var.get('item')==Js(1.0)):
                (var.put('intExtMaskEnable',Js(var.get('intExtMaskEnable').to_number())+Js(1))-Js(1))
        PyJs_anonymous_9_._set_name('anonymous')
        var.get('arrExtMask').callprop('forEach', PyJs_anonymous_9_)
        if (var.get('mask')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_B')).neg():
            var.get('message').put('Accelerometer', Js({}))
            if (var.get('mask')&var.get('MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_EVENT')):
                var.put('bIsSensorEventExist', Js(True))
            (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
            if (var.get('axisMask')&var.get('MASK_PAYLOAD_SENSOR_AXIS_X_MASK')):
                var.get('message').get('Accelerometer').put('X-Axis', Js({}))
                var.put('index', var.get('parseAxisData')(var.get('index'), var.get('bIsSensorEventExist'), var.get('extMask'), var.get('message').get('Accelerometer').get('X-Axis')))
            if (var.get('axisMask')&var.get('MASK_PAYLOAD_SENSOR_AXIS_Y_MASK')):
                var.get('message').get('Accelerometer').put('Y-Axis', Js({}))
                var.put('index', var.get('parseAxisData')(var.get('index'), var.get('bIsSensorEventExist'), var.get('extMask'), var.get('message').get('Accelerometer').get('Y-Axis')))
            if (var.get('axisMask')&var.get('MASK_PAYLOAD_SENSOR_AXIS_Z_MASK')):
                var.get('message').get('Accelerometer').put('Z-Axis', Js({}))
                var.put('index', var.get('parseAxisData')(var.get('index'), var.get('bIsSensorEventExist'), var.get('extMask'), var.get('message').get('Accelerometer').get('Z-Axis')))
            var.put('length', ((var.get('length')-Js(2.0))-(var.get('intAxisMaskEnable')*((var.get('intExtMaskEnable')*Js(2.0))+(Js(2.0) if var.get('bIsSensorEventExist') else Js(0.0))))))
            var.get('message').get('Accelerometer').put('LogIndex', Js(0.0))
            if ((var.get('version')>Js(0.0)) and (var.get('length')>Js(0.0))):
                var.put('mask2', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
                var.put('length', Js(1.0), '-')
                if (var.get('mask2')&var.get('MASK_PAYLOAD_SENSOR_MASK2_LOGINDEX')):
                    def PyJs_LONG_10_(var=var):
                        return var.get('message').get('Accelerometer').put('LogIndex', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                    PyJs_LONG_10_()
                    var.put('length', Js(4.0), '-')
                if (var.get('mask2')&var.get('MASK_PAYLOAD_SENSOR_MASK2_TIME')):
                    def PyJs_LONG_11_(var=var):
                        return var.get('message').get('Accelerometer').put('Time', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                    PyJs_LONG_11_()
                    var.put('length', Js(4.0), '-')
                if (var.get('length')>Js(0.0)):
                    var.put('index', var.get('length'), '+')
        else:
            (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
            if (var.get('extMask')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_MASSIVE_DATA_INFO')):
                var.put('dataType', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
                var.put('sampleRate', var.get('translateInt24')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                var.put('points', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                var.put('logIndex', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                var.put('timestamp', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                var.put('totalLength', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                var.put('massType', (var.get('dataType')&var.get('MASK_PAYLOAD_SENSOR_MASSIVE_DATA_TYPE_MASSIVE_TYPE')))
                var.put('bytesPerSample', (Js(4.0) if (((var.get('dataType')&var.get('MASK_PAYLOAD_SENSOR_MASSIVE_DATA_TYPE_BYTES_PER_SAMPLE'))>>Js(4.0))>Js(0.0)) else Js(2.0)))
                var.put('samplesPerAxis', (((var.get('points')/Js(2.56))/Js(2.0)) if ((var.get('massType')==var.get('MASK_PAYLOAD_SENSOR_MASSIVE_DATA_TYPE_MASSIVE_TYPE_FFT')) and (((var.get('dataType')&var.get('MASK_PAYLOAD_SENSOR_MASSIVE_DATA_TYPE_SAMPLE_PER_AXIS'))>>Js(2.0))>Js(0.0))) else (var.get('points')/Js(2.56))))
                var.put('bytesPerAxis', (var.get('bytesPerSample')*var.get('samplesPerAxis')))
                var.put('length', (var.get('length')-Js(18.0)))
                var.put('objData', Js({}))
                var.get('objData').put('timestamp', var.get('timestamp'))
                var.get('objData').put('lastSeq', var.get('hexArr').get('1'))
                var.get('objData').put('lastPayload', var.get('hexArr'))
                var.get('objData').put('logIndex', var.get('logIndex'))
                var.get('objData').put('sampleRate', var.get('sampleRate'))
                var.get('objData').put('points', var.get('points'))
                var.get('objData').put('bytesPerSample', var.get('bytesPerSample'))
                var.get('objData').put('samplesPerAxis', var.get('samplesPerAxis'))
                var.get('objData').put('bytesPerAxis', var.get('bytesPerAxis'))
                var.get('objData').put('totalLength', var.get('totalLength'))
                var.get('context').callprop('set', Js('FFTDataStorage'), var.get('JSON').callprop('stringify', var.get('objData')))
            if (var.get('extMask')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_MASSIVE_DATA_SEC')):
                var.put('FFTDataStorage', var.get('JSON').callprop('parse', (var.get('context').callprop('get', Js('FFTDataStorage')) or Js('{}'))))
                if (var.get('FFTDataStorage').get('timestamp').typeof()==Js('undefined')):
                    PyJsTempException = JsToPyException(Js('FFT Data lost first packet.'))
                    raise PyJsTempException
                var.put('axisType', Js([Js('X'), Js('Y'), Js('Z')]))
                if (var.get('axisMask')&var.get('MASK_PAYLOAD_SENSOR_AXIS_X_MASK')).neg():
                    var.put('axisIndex', var.get('axisType').callprop('indexOf', Js('X')))
                    if (var.get('axisIndex')>(-Js(1.0))):
                        var.get('axisType').callprop('splice', var.get('axisIndex'), Js(1.0))
                if (var.get('axisMask')&var.get('MASK_PAYLOAD_SENSOR_AXIS_Y_MASK')).neg():
                    var.put('axisIndex', var.get('axisType').callprop('indexOf', Js('Y')))
                    if (var.get('axisIndex')>(-Js(1.0))):
                        var.get('axisType').callprop('splice', var.get('axisIndex'), Js(1.0))
                if (var.get('axisMask')&var.get('MASK_PAYLOAD_SENSOR_AXIS_Z_MASK')).neg():
                    var.put('axisIndex', var.get('axisType').callprop('indexOf', Js('Z')))
                    if (var.get('axisIndex')>(-Js(1.0))):
                        var.get('axisType').callprop('splice', var.get('axisIndex'), Js(1.0))
                var.put('logIndex', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                var.put('initialOffset', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                var.put('offset', var.get('initialOffset'))
                var.put('length', (var.get('length')-Js(10.0)))
                var.get('message').put('FFT', Js({}))
                if (var.get('extMask')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_MASSIVE_DATA_INFO')).neg():
                    if PyJsStrictEq(var.get('FFTDataStorage').get('lastSeq'),var.get('hexArr').get('1')):
                        PyJsTempException = JsToPyException(Js('Packet of FFT Data duplicated.'))
                        raise PyJsTempException
                    if PyJsStrictNeq(((Js('0x')+(var.get('FFTDataStorage').get('lastSeq')+Js(1.0)).callprop('toString', Js(16.0)))&Js(255)),var.get('hexArr').get('1')):
                        var.put('lastPayload', var.get('FFTDataStorage').get('lastPayload'))
                        pass
                        if (var.get('lastPayload').get('6')&var.get('MASK_PAYLOAD_SENSOR_EXTMASK_MASSIVE_DATA_INFO')):
                            var.put('lastOffset', ((var.get('translateInt32')(var.get('lastPayload').get('29'), var.get('lastPayload').get('30'), var.get('lastPayload').get('31'), var.get('lastPayload').get('32'))+var.get('lastPayload').get('4'))-Js(28.0)))
                        else:
                            var.put('lastOffset', ((var.get('translateInt32')(var.get('lastPayload').get('11'), var.get('lastPayload').get('12'), var.get('lastPayload').get('13'), var.get('lastPayload').get('14'))+var.get('lastPayload').get('4'))-Js(10.0)))
                        if (var.get('logIndex')!=var.get('FFTDataStorage').get('logIndex')):
                            var.put('fillLength', (((var.get('FFTDataStorage').get('bytesPerAxis')*var.get('intAxisMaskEnable'))-Js(1.0))-var.get('lastOffset')))
                            var.put('logIndex', var.get('FFTDataStorage').get('logIndex'))
                            var.put('objData', Js({}))
                            var.get('objData').put('LOG_INDEX', var.get('logIndex'))
                            var.get('objData').put('BYTE_OFFSET', var.get('lastOffset'))
                            var.get('objData').put('LENGTH', var.get('fillLength'))
                            var.get('context').callprop('set', Js('LostPacketInfo'), var.get('JSON').callprop('stringify', var.get('objData')))
                            var.put('objData', Js({}))
                            var.get('context').callprop('set', Js('FFTDataStorage'), var.get('JSON').callprop('stringify', var.get('objData')))
                            PyJsTempException = JsToPyException(Js('FFT Data lost first packet.'))
                            raise PyJsTempException
                        var.put('fillLength', (var.get('offset')-var.get('lastOffset')))
                        var.put('logIndex', var.get('FFTDataStorage').get('logIndex'))
                        var.get('lostPacketInfo').put('LOG_INDEX', var.get('logIndex'))
                        var.get('lostPacketInfo').put('BYTE_OFFSET', var.get('lastOffset'))
                        var.get('lostPacketInfo').put('LENGTH', var.get('fillLength'))
                var.put('timestamp', var.get('FFTDataStorage').get('timestamp'))
                var.put('logIndex', var.get('FFTDataStorage').get('logIndex'))
                var.put('sampleRate', var.get('FFTDataStorage').get('sampleRate'))
                var.put('points', var.get('FFTDataStorage').get('points'))
                var.put('bytesPerSample', var.get('FFTDataStorage').get('bytesPerSample'))
                var.put('samplesPerAxis', var.get('FFTDataStorage').get('samplesPerAxis'))
                var.put('bytesPerAxis', var.get('FFTDataStorage').get('bytesPerAxis'))
                var.put('totalLength', var.get('FFTDataStorage').get('totalLength'))
                var.get('message').get('FFT').put('LOG_INDEX', var.get('logIndex'))
                var.get('message').get('FFT').put('TIME', var.get('timestamp'))
                var.get('message').get('FFT').put('SAMPLING_RATE', var.get('sampleRate'))
                var.get('message').get('FFT').put('NUMBER_OF_SAMPLES', var.get('points'))
                var.get('message').get('FFT').put('START_BYTE_OFFSET', var.get('offset'))
                var.put('axisData', Js({}))
                var.put('csvMessage', Js('"TIME","AXIS_TYPE","DATA","LOG_INDEX","BYTE_OFFSET","SAMPLE_FREQ"\n'))
                #for JS loop
                var.put('i', Js(0.0))
                while (var.get('i')<(var.get('length')/var.get('bytesPerSample'))):
                    var.put('axis', (var.get('axisType').get('0') if (var.get('offset')<var.get('bytesPerAxis')) else (var.get('axisType').get('1') if (var.get('offset')<(var.get('bytesPerAxis')*Js(2.0))) else var.get('axisType').get('2'))))
                    def PyJs_LONG_12_(var=var):
                        return (var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))) if (var.get('bytesPerSample')==Js(2.0)) else var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                    var.put('data', PyJs_LONG_12_())
                    var.put('sampleIndex', ((var.get('offset')%var.get('bytesPerAxis'))/var.get('bytesPerSample')))
                    var.put('sampleFreq', (var.get('sampleIndex')*(var.get('sampleRate')/var.get('points'))))
                    if (var.get('axisData').get(var.get('axis')).typeof()==Js('undefined')):
                        var.get('axisData').put(var.get('axis'), Js({}))
                        var.get('axisData').get(var.get('axis')).put('AXIS_TYPE', var.get('axis'))
                        var.get('axisData').get(var.get('axis')).put('START_SAMPLE_INDEX', var.get('sampleIndex'))
                        var.get('axisData').get(var.get('axis')).put('END_SAMPLE_INDEX', ((var.get('samplesPerAxis')-Js(1.0)) if ((var.get('offset')%var.get('bytesPerAxis'))>=((var.get('initialOffset')+var.get('length'))%var.get('bytesPerAxis'))) else ((((var.get('initialOffset')+var.get('length'))%var.get('bytesPerAxis'))/var.get('bytesPerSample'))-Js(1.0))))
                        var.get('axisData').get(var.get('axis')).put('DATA', Js([]))
                    var.get('axisData').get(var.get('axis')).get('DATA').callprop('push', var.get('data'))
                    var.put('csvMessage', (((((((((((var.get('timestamp')+Js(','))+var.get('axis'))+Js(','))+var.get('data'))+Js(','))+var.get('logIndex'))+Js(','))+var.get('offset'))+Js(','))+(var.get('Math').callprop('floor', (var.get('sampleFreq')*Js(1000.0)))/Js(1000.0)))+Js('\n')), '+')
                    var.put('offset', var.get('bytesPerSample'), '+')
                    if (var.get('offset')>=var.get('totalLength')):
                        var.put('index', (var.get('index')+((((var.get('length')/var.get('bytesPerSample'))-var.get('i'))-Js(1.0))*var.get('bytesPerSample'))))
                        break
                    # update
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.get('message').get('FFT').put('END_BYTE_OFFSET', (var.get('offset')-Js(1.0)))
                var.get('message').get('FFT').put('AXIS_DATA', Js([]))
                for PyJsTemp in var.get('axisData'):
                    var.put('i', PyJsTemp)
                    var.get('message').get('FFT').get('AXIS_DATA').callprop('push', var.get('axisData').get(var.get('i')))
                var.put('axisData', Js({}))
                if (var.get('offset')!=(var.get('bytesPerAxis')*var.get('intAxisMaskEnable'))):
                    var.get('FFTDataStorage').put('lastSeq', var.get('hexArr').get('1'))
                    var.get('FFTDataStorage').put('lastPayload', var.get('hexArr'))
                    var.get('context').callprop('set', Js('FFTDataStorage'), var.get('JSON').callprop('stringify', var.get('FFTDataStorage')))
                else:
                    var.put('objData', Js({}))
                    var.get('context').callprop('set', Js('FFTDataStorage'), var.get('JSON').callprop('stringify', var.get('objData')))
    return var.get('index')
PyJsHoisted_sensorParse_.func_name = 'sensorParse'
var.put('sensorParse', PyJsHoisted_sensorParse_)
@Js
def PyJsHoisted_deviceParse_(index, this, arguments, var=var):
    var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
    var.registers(['longitudeStr', 'length', 'latitudeStr', 'index'])
    pass
    var.get('message').put('Device', Js({}))
    (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
    if (var.get('version')>Js(0.0)):
        var.put('length', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
    var.put('mask', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
    if (var.get('version')>Js(0.0)):
        var.put('length', Js(1.0), '-')
    if (var.get('mask')&var.get('MASK_DEVICE_EVENT')):
        var.get('message').get('Device').put('Events', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(1.0), '-')
    if (var.get('mask')&var.get('MASK_DEVICE_POWER_SOURCE')):
        var.get('message').get('Device').put('PowerSrc', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(1.0), '-')
    if (var.get('mask')&var.get('MASK_DEVICE_BATTERY_LEVEL')):
        var.get('message').get('Device').put('BatteryLevel', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(1.0), '-')
    if (var.get('mask')&var.get('MASK_DEVICE_BATTERY_VOLTAGE')):
        var.get('message').get('Device').put('BatteryVolt', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(2.0), '-')
    if (var.get('mask')&var.get('MASK_DEVICE_TIMESTAMP')):
        def PyJs_LONG_13_(var=var):
            return var.get('message').get('Device').put('Time', var.get('translateInt32')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
        PyJs_LONG_13_()
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(4.0), '-')
    if (var.get('mask')&var.get('MASK_DEVICE_POSITION')):
        var.get('message').get('Device').put('GNSS', Js({}))
        var.put('latitudeStr', Js(''))
        var.put('longitudeStr', Js(''))
        if (var.get('hexArr').get(var.get('index'))&var.get('MASK_DEVICE_POSITION_LATITUDE')):
            var.put('latitudeStr', Js('S'))
        else:
            var.put('latitudeStr', Js('N'))
        if (var.get('hexArr').get(var.get('index'))&var.get('MASK_DEVICE_POSITION_LONGITUDE')):
            var.put('longitudeStr', Js('W'))
        else:
            var.put('longitudeStr', Js('E'))
        (var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))
        def PyJs_LONG_14_(var=var):
            return var.get('message').get('Device').get('GNSS').put('Latitude', (((var.get('translateInt24')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))/Js(100000.0)).callprop('toFixed', Js(5.0))+Js(' '))+var.get('latitudeStr')))
        PyJs_LONG_14_()
        def PyJs_LONG_15_(var=var):
            return var.get('message').get('Device').get('GNSS').put('Longitude', (((var.get('translateInt24')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))/Js(100000.0)).callprop('toFixed', Js(5.0))+Js(' '))+var.get('longitudeStr')))
        PyJs_LONG_15_()
        if (var.get('version')>Js(0.0)):
            var.put('length', Js(7.0), '-')
    if (var.get('version')>Js(0.0)):
        if (var.get('length')>Js(0.0)):
            var.put('index', var.get('length'), '+')
    return var.get('index')
PyJsHoisted_deviceParse_.func_name = 'deviceParse'
var.put('deviceParse', PyJsHoisted_deviceParse_)
@Js
def PyJsHoisted_coilParse_(index, this, arguments, var=var):
    var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
    var.registers(['port', 'length', 'dataMask', 'j', 'chMask', 'i', 'k', 'ch', 'index', 'channel', 'maskGroup', 'channelIndex', 'recordLen', 'infoLen', 'isSupportStatus', 'isSupportData', 'mask'])
    pass
    var.put('mask', (var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))&Js(7)))
    if (var.get('version')>Js(0.0)):
        var.put('length', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
    var.put('channel', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
    if (var.get('version')>Js(0.0)):
        var.put('length', Js(1.0), '-')
    var.put('port', ((var.get('channel')&Js(128))>>Js(7.0)))
    if (var.get('mask')&var.get('MASK_PAYLOAD_COIL_MULTI_CH')):
        var.put('infoLen', (var.get('channel')&Js(127)))
        var.put('recordLen', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
        var.put('dataMask', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
        var.put('ch', Js(0.0))
        var.put('isSupportStatus', ((var.get('dataMask')&var.get('MASK_PAYLOAD_COIL_STATUS'))==var.get('MASK_PAYLOAD_COIL_STATUS')))
        var.put('isSupportData', ((var.get('dataMask')&var.get('MASK_PAYLOAD_COIL_VALUE'))==var.get('MASK_PAYLOAD_COIL_VALUE')))
        #for JS loop
        var.put('i', Js(1.0))
        while (var.get('i')<=(var.get('infoLen')-Js(2.0))):
            var.put('maskGroup', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('j', Js(0.0))
            while (var.get('j')<Js(7.0)):
                if ((var.get('maskGroup')&(Js(1.0)<<var.get('j')))==Js(0.0)):
                    var.put('ch', Js(8.0), '+')
                    # continue update
                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                    continue
                var.put('chMask', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                #for JS loop
                var.put('k', Js(0.0))
                while (var.get('k')<Js(8.0)):
                    if ((var.get('chMask')&(Js(1.0)<<var.get('k')))==Js(0.0)):
                        var.put('ch', Js(1.0), '+')
                        # continue update
                        (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
                        continue
                    var.get('message').put((((Js('RtuCoil')+var.get('port'))+Js('-'))+var.get('ch')), Js({}))
                    var.put('ch', Js(1.0), '+')
                    # update
                    (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
                # update
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        if (var.get('version')>Js(0.0)):
            var.put('length', var.get('infoLen'), '-')
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('ch')):
            if (var.get('message').get((((Js('RtuCoil')+var.get('port'))+Js('-'))+var.get('i'))).typeof()!=Js('undefined')):
                if var.get('isSupportStatus'):
                    var.get('message').get((((Js('RtuCoil')+var.get('port'))+Js('-'))+var.get('i'))).put('Status', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
                    if (var.get('version')>Js(0.0)):
                        var.put('length', Js(1.0), '-')
                if var.get('isSupportData'):
                    var.get('message').get((((Js('RtuCoil')+var.get('port'))+Js('-'))+var.get('i'))).put('Data', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
                    if (var.get('version')>Js(0.0)):
                        var.put('length', Js(1.0), '-')
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    else:
        var.put('channelIndex', (var.get('channel')&Js(127)))
        var.get('message').put((((Js('RtuCoil')+var.get('port'))+Js('-'))+var.get('channelIndex')), Js({}))
        if (var.get('mask')&var.get('MASK_PAYLOAD_COIL_STATUS')):
            var.get('message').get((((Js('RtuCoil')+var.get('port'))+Js('-'))+var.get('channelIndex'))).put('Status', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
            if (var.get('version')>Js(0.0)):
                var.put('length', Js(1.0), '-')
        if (var.get('mask')&var.get('MASK_PAYLOAD_COIL_VALUE')):
            var.get('message').get((((Js('RtuCoil')+var.get('port'))+Js('-'))+var.get('channelIndex'))).put('Data', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
            if (var.get('version')>Js(0.0)):
                var.put('length', Js(1.0), '-')
    if (var.get('version')>Js(0.0)):
        if (var.get('length')>Js(0.0)):
            var.put('index', var.get('length'), '+')
    return var.get('index')
PyJsHoisted_coilParse_.func_name = 'coilParse'
var.put('coilParse', PyJsHoisted_coilParse_)
@Js
def PyJsHoisted_registerParse_(index, this, arguments, var=var):
    var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
    var.registers(['port', 'length', 'dataMask', 'j', 'chMask', 'i', 'k', 'ch', 'index', 'channel', 'maskGroup', 'channelIndex', 'recordLen', 'infoLen', 'isSupportStatus', 'isSupportData', 'mask'])
    pass
    var.put('mask', (var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))&Js(7)))
    if (var.get('version')>Js(0.0)):
        var.put('length', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
    var.put('channel', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
    if (var.get('version')>Js(0.0)):
        var.put('length', Js(1.0), '-')
    var.put('port', ((var.get('channel')&Js(128))>>Js(7.0)))
    if (var.get('mask')&var.get('MASK_PAYLOAD_REGISTER_MULTI_CH')):
        var.put('infoLen', (var.get('channel')&Js(127)))
        var.put('recordLen', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
        var.put('dataMask', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
        var.put('ch', Js(0.0))
        var.put('isSupportStatus', ((var.get('dataMask')&var.get('MASK_PAYLOAD_REGISTER_STATUS'))==var.get('MASK_PAYLOAD_REGISTER_STATUS')))
        var.put('isSupportData', ((var.get('dataMask')&var.get('MASK_PAYLOAD_REGISTER_VALUE'))==var.get('MASK_PAYLOAD_REGISTER_VALUE')))
        #for JS loop
        var.put('i', Js(1.0))
        while (var.get('i')<=(var.get('infoLen')-Js(2.0))):
            var.put('maskGroup', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
            #for JS loop
            var.put('j', Js(0.0))
            while (var.get('j')<Js(7.0)):
                if ((var.get('maskGroup')&(Js(1.0)<<var.get('j')))==Js(0.0)):
                    var.put('ch', Js(8.0), '+')
                    # continue update
                    (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
                    continue
                var.put('chMask', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                #for JS loop
                var.put('k', Js(0.0))
                while (var.get('k')<Js(8.0)):
                    if ((var.get('chMask')&(Js(1.0)<<var.get('k')))==Js(0.0)):
                        var.put('ch', Js(1.0), '+')
                        # continue update
                        (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
                        continue
                    var.get('message').put((((Js('RtuRegister')+var.get('port'))+Js('-'))+var.get('ch')), Js({}))
                    var.put('ch', Js(1.0), '+')
                    # update
                    (var.put('k',Js(var.get('k').to_number())+Js(1))-Js(1))
                # update
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        if (var.get('version')>Js(0.0)):
            var.put('length', var.get('infoLen'), '-')
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('ch')):
            if (var.get('message').get((((Js('RtuRegister')+var.get('port'))+Js('-'))+var.get('i'))).typeof()!=Js('undefined')):
                if var.get('isSupportStatus'):
                    var.get('message').get((((Js('RtuRegister')+var.get('port'))+Js('-'))+var.get('i'))).put('Status', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
                    if (var.get('version')>Js(0.0)):
                        var.put('length', Js(1.0), '-')
                if var.get('isSupportData'):
                    var.get('message').get((((Js('RtuRegister')+var.get('port'))+Js('-'))+var.get('i'))).put('Data', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
                    if (var.get('version')>Js(0.0)):
                        var.put('length', Js(2.0), '-')
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    else:
        var.put('channelIndex', (var.get('channel')&Js(127)))
        var.get('message').put((((Js('RtuRegister')+var.get('port'))+Js('-'))+var.get('channelIndex')), Js({}))
        if (var.get('mask')&var.get('MASK_PAYLOAD_REGISTER_STATUS')):
            var.get('message').get((((Js('RtuRegister')+var.get('port'))+Js('-'))+var.get('channelIndex'))).put('Status', var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))))
            if (var.get('version')>Js(0.0)):
                var.put('length', Js(1.0), '-')
        if (var.get('mask')&var.get('MASK_PAYLOAD_REGISTER_VALUE')):
            var.get('message').get((((Js('RtuRegister')+var.get('port'))+Js('-'))+var.get('channelIndex'))).put('Data', var.get('translateInt16')(var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1))), var.get('hexArr').get((var.put('index',Js(var.get('index').to_number())+Js(1))-Js(1)))))
            if (var.get('version')>Js(0.0)):
                var.put('length', Js(2.0), '-')
    if (var.get('version')>Js(0.0)):
        if (var.get('length')>Js(0.0)):
            var.put('index', var.get('length'), '+')
    return var.get('index')
PyJsHoisted_registerParse_.func_name = 'registerParse'
var.put('registerParse', PyJsHoisted_registerParse_)
@Js
def PyJsHoisted_parsePayLoad_(index, this, arguments, var=var):
    var = Scope({'index':index, 'this':this, 'arguments':arguments}, var)
    var.registers(['bIsSensorEventExist', 'axisMask', 'index', 'extMask', 'mask'])
    var.put('axisMask', Js(''))
    var.put('mask', Js(''))
    var.put('extMask', Js(''))
    var.put('bIsSensorEventExist', Js(False))
    if PyJsStrictEq((var.get('hexArr').get(var.get('index'))&Js(240)),var.get('PAYLOAD_DI_DATA')):
        var.put('index', var.get('DIParse')(var.get('index')))
        if (var.get('index')<(var.get('arrLength')-Js(1.0))):
            var.get('parsePayLoad')(var.get('index'))
            return var.get('undefined')
        else:
            var.get('console').callprop('log', Js('Finish DI Parsing.'))
            return var.get('undefined')
    else:
        if PyJsStrictEq((var.get('hexArr').get(var.get('index'))&Js(240)),var.get('PAYLOAD_DO_DATA')):
            var.put('index', var.get('DOParse')(var.get('index')))
            if (var.get('index')<(var.get('arrLength')-Js(1.0))):
                var.get('parsePayLoad')(var.get('index'))
                return var.get('undefined')
            else:
                var.get('console').callprop('log', Js('Finish DO Parsing.'))
                return var.get('undefined')
        else:
            if PyJsStrictEq((var.get('hexArr').get(var.get('index'))&Js(240)),var.get('PAYLOAD_AI_DATA')):
                var.put('index', var.get('AIParse')(var.get('index')))
                if (var.get('index')<(var.get('arrLength')-Js(1.0))):
                    var.get('parsePayLoad')(var.get('index'))
                    return var.get('undefined')
                else:
                    var.get('console').callprop('log', Js('Finish AI Parsing.'))
                    return var.get('undefined')
            else:
                if PyJsStrictEq((var.get('hexArr').get(var.get('index'))&Js(240)),var.get('PAYLOAD_SENSOR_DATA')):
                    var.put('index', var.get('sensorParse')(var.get('index')))
                    if (var.get('index')<(var.get('arrLength')-Js(1.0))):
                        var.get('parsePayLoad')(var.get('index'))
                        return var.get('undefined')
                    else:
                        var.get('console').callprop('log', Js('Finish Sensor Parsing.'))
                        return var.get('undefined')
                else:
                    if PyJsStrictEq((var.get('hexArr').get(var.get('index'))&Js(240)),var.get('PAYLOAD_DEVICE_DATA')):
                        var.put('index', var.get('deviceParse')(var.get('index')))
                        if (var.get('index')<(var.get('arrLength')-Js(1.0))):
                            var.get('parsePayLoad')(var.get('index'))
                            return var.get('undefined')
                        else:
                            var.get('console').callprop('log', Js('Finish Device Parsing.'))
                            return var.get('undefined')
                    else:
                        if PyJsStrictEq((var.get('hexArr').get(var.get('index'))&Js(240)),var.get('PAYLOAD_COIL_DATA')):
                            var.put('index', var.get('coilParse')(var.get('index')))
                            if (var.get('index')<(var.get('arrLength')-Js(1.0))):
                                var.get('parsePayLoad')(var.get('index'))
                                return var.get('undefined')
                            else:
                                var.get('console').callprop('log', Js('Finish Coil Parsing.'))
                                return var.get('undefined')
                        else:
                            if PyJsStrictEq((var.get('hexArr').get(var.get('index'))&Js(240)),var.get('PAYLOAD_REGISTER_DATA')):
                                var.put('index', var.get('registerParse')(var.get('index')))
                                if (var.get('index')<(var.get('arrLength')-Js(1.0))):
                                    var.get('parsePayLoad')(var.get('index'))
                                    return var.get('undefined')
                                else:
                                    var.get('console').callprop('log', Js('Finish Register Parsing.'))
                                    return var.get('undefined')
PyJsHoisted_parsePayLoad_.func_name = 'parsePayLoad'
var.put('parsePayLoad', PyJsHoisted_parsePayLoad_)
@Js
def PyJsHoisted_getSourceAddressLength_(address, this, arguments, var=var):
    var = Scope({'address':address, 'this':this, 'arguments':arguments}, var)
    var.registers(['addressLength', 'address'])
    var.put('addressLength', Js(0.0))
    if ((var.get('address')!=Js('')) and (var.get('address')!=var.get(u"null"))):
        var.put('addressLength', (var.get('address').get('length')/Js(2.0)))
    return var.get('addressLength')
PyJsHoisted_getSourceAddressLength_.func_name = 'getSourceAddressLength'
var.put('getSourceAddressLength', PyJsHoisted_getSourceAddressLength_)
@Js
def PyJsHoisted_checkFrameLength_(this, arguments, var=var):
    var = Scope({'this':this, 'arguments':arguments}, var)
    var.registers(['addressLength'])
    var.put('addressLength', var.get('getSourceAddressLength')(var.get('message').get('SourceAddress')))
    if (((var.get('message').get('TotalLength')+var.get('addressLength'))+Js(4.0))!=var.get('arrLength')):
        return Js(False)
    else:
        return Js(True)
PyJsHoisted_checkFrameLength_.func_name = 'checkFrameLength'
var.put('checkFrameLength', PyJsHoisted_checkFrameLength_)
@Js
def PyJsHoisted_CrcCalc_(u8Arr, u16Length, this, arguments, var=var):
    var = Scope({'u8Arr':u8Arr, 'u16Length':u16Length, 'this':this, 'arguments':arguments}, var)
    var.registers(['u8Arr', 'u8CRC', 'u16Length', 'u16i'])
    pass
    var.put('u8CRC', Js(255))
    #for JS loop
    var.put('u16i', Js(0.0))
    while (var.get('u16i')<var.get('u16Length')):
        var.put('u8CRC', var.get('au8CRC8_Pol07_Table').get((var.get('u8CRC')^var.get('u8Arr').get(var.get('u16i')))))
        # update
        (var.put('u16i',Js(var.get('u16i').to_number())+Js(1))-Js(1))
    return var.get('u8CRC')
PyJsHoisted_CrcCalc_.func_name = 'CrcCalc'
var.put('CrcCalc', PyJsHoisted_CrcCalc_)
@Js
def PyJsHoisted_checkPayloadLengthAndSetStorage_(hexArr, sequence, this, arguments, var=var):
    var = Scope({'hexArr':hexArr, 'sequence':sequence, 'this':this, 'arguments':arguments}, var)
    var.registers(['sequence', 'hexArr', 'objData', 'sourceAddressLen'])
    var.put('sourceAddressLen', Js(0.0))
    if PyJsStrictEq((var.get('hexArr').get('0')&var.get('MASK_HEADER_ADDRESS_MODE')),var.get('MASK_HEADER_ADDRESS_2_OCTECT')):
        var.put('sourceAddressLen', Js(2.0))
    else:
        if PyJsStrictEq((var.get('hexArr').get('0')&var.get('MASK_HEADER_ADDRESS_MODE')),var.get('MASK_HEADER_ADDRESS_8_OCTECT')):
            var.put('sourceAddressLen', Js(8.0))
    if PyJsStrictNeq((((((var.get('hexArr').get('length')-Js(1.0))-Js(1.0))-Js(1.0))-var.get('sourceAddressLen'))-Js(1.0)),var.get('hexArr').get('2')):
        var.put('objData', Js({}))
        var.get('objData').put('sequence', (var.get('sequence') if PyJsStrictNeq(var.get('sequence'),var.get(u"null")) else var.get('hexArr').get('1')))
        var.get('objData').put('time', var.get('Date').create().callprop('getTime'))
        var.get('objData').put('payload', var.get('hexArr'))
        var.get('context').callprop('set', Js('payloadStorage'), var.get('JSON').callprop('stringify', var.get('objData')))
        return Js(False)
    else:
        return Js(True)
PyJsHoisted_checkPayloadLengthAndSetStorage_.func_name = 'checkPayloadLengthAndSetStorage'
var.put('checkPayloadLengthAndSetStorage', PyJsHoisted_checkPayloadLengthAndSetStorage_)
@Js
def PyJsHoisted_decode_(receivedString, this, arguments, var=var):
    var = Scope({'receivedString':receivedString, 'this':this, 'arguments':arguments}, var)
    var.registers(['receivedString', 'node', 'bIsRunNodeRed', 'currentSeq', 'calculateCRC', 'sourceAddress', 'output', 'msg', 'payloadStorage'])
    var.put('bIsRunNodeRed', Js(False))
    if var.get('bIsRunNodeRed'):
        var.put('receivedString', var.get('msg').get('payload').get('data'))
    else:
        var.put('msg', Js({}))
        var.get('msg').put('payload', Js(''))
    if (var.get('receivedString')==var.get('undefined')):
        var.get('console').callprop('log', Js('Error: No data is received'))
        var.get('msg').put('payload', Js('Error: No data is received'))
        return var.get('msg')
    var.put('arrLength', var.get('receivedString').get('length'))
    if var.get('bIsRunNodeRed').neg():
        @Js
        def PyJs_anonymous_16_(this, arguments, var=var):
            var = Scope({'this':this, 'arguments':arguments}, var)
            var.registers([])
            pass
        PyJs_anonymous_16_._set_name('anonymous')
        var.put('node', PyJs_anonymous_16_)
        @Js
        def PyJs_anonymous_17_(arg, this, arguments, var=var):
            var = Scope({'arg':arg, 'this':this, 'arguments':arguments}, var)
            var.registers(['arg'])
            var.get('console').callprop('log', var.get('arg'))
        PyJs_anonymous_17_._set_name('anonymous')
        var.get('node').put('warn', PyJs_anonymous_17_)
        @Js
        def PyJs_anonymous_18_(arg, this, arguments, var=var):
            var = Scope({'arg':arg, 'this':this, 'arguments':arguments}, var)
            var.registers(['arg'])
            var.get('console').callprop('error', var.get('arg'))
        PyJs_anonymous_18_._set_name('anonymous')
        var.get('node').put('error', PyJs_anonymous_18_)
    try:
        if ((var.get('arrLength')<var.get('MIN_FRAME_LENGTH')) or PyJsStrictNeq((var.get('arrLength')%Js(2.0)),Js(0.0))):
            var.get('msg').put('payload', Js('received frame length error'))
            return var.get('msg')
        var.get('console').callprop('log', Js('Parse Header'))
        var.put('arrLength', (var.get('arrLength')/Js(2.0)))
        var.get('console').callprop('log', (Js('Payload length: ')+var.get('arrLength')))
        #for JS loop
        var.put('i', Js(0.0))
        while (var.get('i')<var.get('arrLength')):
            var.get('hexArr').callprop('push', var.get('parseInt')(var.get('receivedString').callprop('substring', (var.get('i')*Js(2.0)), ((var.get('i')*Js(2.0))+Js(2.0))), Js(16.0)))
            # update
            (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        var.put('version', (var.get('hexArr').get('0')&var.get('MASK_HEADER_FRAME_VERSION')))
        if (var.get('hexArr').get('0')&var.get('MASK_HEADER_FIRST_SEGMENT')).neg():
            var.put('payloadStorage', var.get('JSON').callprop('parse', (var.get('context').callprop('get', Js('payloadStorage')) or Js('{}'))))
            if PyJsStrictEq(var.get('payloadStorage').get('sequence'),var.get('hexArr').get('1')):
                var.get('msg').put('payload', Js('Sequence number repeat. Drop this packet.'))
                return var.get('msg')
            if ((var.get('payloadStorage').get('sequence').typeof()==Js('undefined')) or PyJsStrictNeq(((Js('0x')+(var.get('payloadStorage').get('sequence')+Js(1.0)).callprop('toString', Js(16.0)))&Js(255)),var.get('hexArr').get('1'))):
                var.get('msg').put('payload', Js('Sequence number error. Packet may be lost.'))
                return var.get('msg')
            if ((var.get('payloadStorage').get('time').typeof()==Js('undefined')) or ((var.get('Date').create().callprop('getTime')-var.get('payloadStorage').get('time'))>Js(60000.0))):
                var.get('msg').put('payload', Js('Timeout.'))
                return var.get('msg')
            var.put('currentSeq', var.get('hexArr').get('1'))
            var.put('hexArr', var.get('payloadStorage').get('payload').callprop('concat', var.get('hexArr').callprop('slice', Js(2.0), var.get('hexArr').get('length'))))
            if var.get('checkPayloadLengthAndSetStorage')(var.get('hexArr'), var.get('currentSeq')).neg():
                var.get('console').callprop('log', Js('Need Packet Reassemble.'))
                return var.get(u"null")
        else:
            if var.get('checkPayloadLengthAndSetStorage')(var.get('hexArr'), var.get(u"null")).neg():
                var.get('console').callprop('log', Js('Need Packet Reassemble.'))
                return var.get(u"null")
        var.put('arrLength', var.get('hexArr').get('length'))
        var.get('message').put('SequenceNumber', var.get('hexArr').get(var.put('arrayIndex',Js(var.get('arrayIndex').to_number())+Js(1))))
        var.get('message').put('TotalLength', var.get('hexArr').get(var.put('arrayIndex',Js(var.get('arrayIndex').to_number())+Js(1))))
        var.put('sourceAddress', Js(''))
        if PyJsStrictEq((var.get('hexArr').get('0')&var.get('MASK_HEADER_ADDRESS_MODE')),var.get('MASK_HEADER_ADDRESS_NONE')):
            var.get('console').callprop('log', Js('No source address'))
            (var.put('arrayIndex',Js(var.get('arrayIndex').to_number())+Js(1))-Js(1))
            var.get('message').put('SourceAddress', var.get(u"null"))
        else:
            if PyJsStrictEq((var.get('hexArr').get('0')&var.get('MASK_HEADER_ADDRESS_MODE')),var.get('MASK_HEADER_ADDRESS_2_OCTECT')):
                var.get('console').callprop('log', Js('2 octects source address'))
                (var.put('arrayIndex',Js(var.get('arrayIndex').to_number())+Js(1))-Js(1))
                #for JS loop
                var.put('i', var.get('arrayIndex'))
                while (var.get('i')<(var.get('arrayIndex')+Js(2.0))):
                    var.put('sourceAddress', (var.get('sourceAddress')+var.get('addZero')(var.get('hexArr').get(var.get('i')).callprop('toString', Js(16.0)))))
                    # update
                    (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                var.get('message').put('SourceAddress', var.get('sourceAddress'))
                var.put('arrayIndex', Js(2.0), '+')
            else:
                if PyJsStrictEq((var.get('hexArr').get('0')&var.get('MASK_HEADER_ADDRESS_MODE')),var.get('MASK_HEADER_ADDRESS_8_OCTECT')):
                    var.get('console').callprop('log', Js('8 octects source address'))
                    (var.put('arrayIndex',Js(var.get('arrayIndex').to_number())+Js(1))-Js(1))
                    #for JS loop
                    var.put('i', var.get('arrayIndex'))
                    while (var.get('i')<(var.get('arrayIndex')+Js(8.0))):
                        var.put('sourceAddress', (var.get('sourceAddress')+var.get('addZero')(var.get('hexArr').get(var.get('i')).callprop('toString', Js(16.0)))))
                        # update
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
                    var.get('message').put('SourceAddress', var.get('sourceAddress'))
                    var.put('arrayIndex', Js(8.0), '+')
        var.put('hexPayloadArr', var.get('hexArr').callprop('slice', (Js(3.0)+var.get('getSourceAddressLength')(var.get('message').get('SourceAddress'))), (var.get('hexArr').get('length')-Js(1.0))))
        var.put('calculateCRC', var.get('CrcCalc')(var.get('hexPayloadArr'), var.get('hexPayloadArr').get('length')))
        if (var.get('version')>Js(0.0)):
            var.put('calculateCRC', ((~var.get('calculateCRC'))&Js(255)))
        if (var.get('calculateCRC')!=var.get('hexArr').get((var.get('hexArr').get('length')-Js(1.0)))):
            var.get('console').callprop('log', Js('Frame CRC check failed.'))
            var.get('msg').put('payload', Js('Frame CRC check failed.'))
            return var.get('msg')
        if ((var.get('message').get('SourceAddress')!=var.get(u"null")) and var.get('checkFrameLength')().neg()):
            var.get('console').callprop('log', Js('Frame length error'))
            var.get('msg').put('payload', Js('Frame length error'))
            return var.get('msg')
        var.get('console').callprop('log', Js('Parse Payload'))
        var.get('parsePayLoad')(var.get('arrayIndex'))
    except PyJsException as PyJsTempException:
        PyJsHolder_6578_70439102 = var.own.get('ex')
        var.force_own_put('ex', PyExceptionToJs(PyJsTempException))
        try:
            var.get('console').callprop('log', (Js('Error: Parser failed. ')+var.get('ex')))
            var.get('msg').put('payload', (Js('Error: Parser failed. ')+var.get('ex')))
            var.put('output', Js([var.get('msg'), var.get(u"null")]))
            if (var.get('lostPacketInfo').get('LOG_INDEX').typeof()!=Js('undefined')):
                var.get('output').callprop('push', Js({'payload':var.get('JSON').callprop('stringify', var.get('lostPacketInfo'))}))
                var.put('lostPacketInfo', Js({}))
            return var.get('output')
        finally:
            if PyJsHolder_6578_70439102 is not None:
                var.own['ex'] = PyJsHolder_6578_70439102
            else:
                del var.own['ex']
            del PyJsHolder_6578_70439102
    if var.get('bIsRunNodeRed'):
        var.get('msg').put('payload', var.get('message'))
        var.put('output', Js([var.get('msg')]))
        if (var.get('csvMessage').get('length')>Js(0.0)):
            var.get('output').callprop('push', Js({'payload':var.get('csvMessage')}))
            if (var.get('lostPacketInfo').get('LOG_INDEX').typeof()!=Js('undefined')):
                var.get('output').callprop('push', Js({'payload':var.get('JSON').callprop('stringify', var.get('lostPacketInfo'))}))
                var.put('lostPacketInfo', Js({}))
        return var.get('output')
    else:
        var.put('stringified', var.get('JSON').callprop('stringify', var.get('message'), var.get(u"null"), Js(4.0)))
        string_ret = var.get('stringified').to_string().value
        return string_ret
PyJsHoisted_decode_.func_name = 'decode'
var.put('decode', PyJsHoisted_decode_)
pass
var.put('message', Js({}))
var.put('csvMessage', Js(''))
var.put('lostPacketInfo', Js({}))
pass
var.put('hexArr', Js([]))
var.put('hexPayloadArr', Js([]))
var.put('arrayIndex', Js(0.0))
var.put('MIN_FRAME_LENGTH', Js(4.0))
var.put('MASK_HEADER_FIRST_SEGMENT', Js(128))
var.put('MASK_HEADER_ADDRESS_MODE', Js(12))
var.put('MASK_HEADER_ADDRESS_NONE', Js(0))
var.put('MASK_HEADER_ADDRESS_2_OCTECT', Js(4))
var.put('MASK_HEADER_ADDRESS_8_OCTECT', Js(8))
var.put('MASK_HEADER_FRAME_VERSION', Js(3))
var.put('PAYLOAD_DI_DATA', Js(0))
var.put('PAYLOAD_DO_DATA', Js(16))
var.put('PAYLOAD_AI_DATA', Js(48))
var.put('PAYLOAD_SENSOR_DATA', Js(80))
var.put('PAYLOAD_DEVICE_DATA', Js(96))
var.put('PAYLOAD_COIL_DATA', Js(112))
var.put('PAYLOAD_REGISTER_DATA', Js(128))
var.put('MASK_PAYLOAD_DI_STATUS', Js(1))
var.put('MASK_PAYLOAD_DI_VALUE', Js(2))
var.put('MASK_PAYLOAD_DI_EVENT', Js(4))
var.put('DI_MODE_FREQUENCY', Js(4.0))
var.put('MASK_PAYLOAD_DO_STATUS', Js(1))
var.put('MASK_PAYLOAD_DO_ABSOLUTE_PULSE_OUTPUT', Js(2))
var.put('MASK_PAYLOAD_DO_INCREMENTAL_PULSE_OUTPUT', Js(4))
var.put('MASK_PAYLOAD_AI_STATUS', Js(1))
var.put('MASK_PAYLOAD_AI_RAW_VALUE', Js(2))
var.put('MASK_PAYLOAD_AI_EVENT', Js(4))
var.put('MASK_PAYLOAD_AI_MAX_VALUE', Js(8))
var.put('MASK_PAYLOAD_AI_MIN_VALUE', Js(16))
var.put('MASK_PAYLOAD_AI_MASK2_RANGE', Js(1))
var.put('MASK_PAYLOAD_SENSOR_TEMP_C_TYPE', Js(0))
var.put('MASK_PAYLOAD_SENSOR_TEMP_F_TYPE', Js(1))
var.put('MASK_PAYLOAD_SENSOR_TEMP_K_TYPE', Js(2))
var.put('MASK_PAYLOAD_SENSOR_HUMIDITY_TYPE', Js(3))
var.put('MASK_PAYLOAD_SENSOR_ACCELERATOR_TYPE_G', Js(4))
var.put('MASK_PAYLOAD_SENSOR_ACCELERATOR_TYPE_MS2', Js(5))
var.put('MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_STATUS', Js(1))
var.put('MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_EVENT', Js(2))
var.put('MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_VALUE', Js(4))
var.put('MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_MAX_VALUE', Js(8))
var.put('MASK_PAYLOAD_SENSOR_MASK_SENSNSOR_MIN_VALUE', Js(16))
var.put('MASK_PAYLOAD_SENSOR_AXIS_X_MASK', Js(1))
var.put('MASK_PAYLOAD_SENSOR_AXIS_Y_MASK', Js(2))
var.put('MASK_PAYLOAD_SENSOR_AXIS_Z_MASK', Js(4))
var.put('MASK_PAYLOAD_SENSOR_MASK2_LOGINDEX', Js(1))
var.put('MASK_PAYLOAD_SENSOR_MASK2_TIME', Js(2))
var.put('MASK_PAYLOAD_SENSOR_EXTMASK_VELOCITY', Js(1))
var.put('MASK_PAYLOAD_SENSOR_EXTMASK_PEAK', Js(2))
var.put('MASK_PAYLOAD_SENSOR_EXTMASK_RMS', Js(4))
var.put('MASK_PAYLOAD_SENSOR_EXTMASK_KURTOSIS', Js(8))
var.put('MASK_PAYLOAD_SENSOR_EXTMASK_CRESTFACTOR', Js(16))
var.put('MASK_PAYLOAD_SENSOR_EXTMASK_SKEWNESS', Js(32))
var.put('MASK_PAYLOAD_SENSOR_EXTMASK_STDDEVIATION', Js(64))
var.put('MASK_PAYLOAD_SENSOR_EXTMASK_DISPLACEMENT', Js(128))
var.put('MASK_PAYLOAD_SENSOR_EXTMASK_B', Js(1))
var.put('MASK_PAYLOAD_SENSOR_EXTMASK_MASSIVE_DATA_INFO', Js(1))
var.put('MASK_PAYLOAD_SENSOR_EXTMASK_MASSIVE_DATA_SEC', Js(2))
var.put('MASK_PAYLOAD_SENSOR_EXTMASK_MASSIVE_DATA_LOG', Js(4))
var.put('MASK_PAYLOAD_SENSOR_MASSIVE_DATA_TYPE_MASSIVE_TYPE', Js(3))
var.put('MASK_PAYLOAD_SENSOR_MASSIVE_DATA_TYPE_SAMPLE_PER_AXIS', Js(12))
var.put('MASK_PAYLOAD_SENSOR_MASSIVE_DATA_TYPE_BYTES_PER_SAMPLE', Js(16))
var.put('MASK_PAYLOAD_SENSOR_MASSIVE_DATA_TYPE_MASSIVE_TYPE_FFT', Js(1))
var.put('MASK_DEVICE_EVENT', Js(1))
var.put('MASK_DEVICE_POWER_SOURCE', Js(2))
var.put('MASK_DEVICE_BATTERY_LEVEL', Js(4))
var.put('MASK_DEVICE_BATTERY_VOLTAGE', Js(8))
var.put('MASK_DEVICE_TIMESTAMP', Js(16))
var.put('MASK_DEVICE_POSITION', Js(32))
var.put('MASK_DEVICE_POSITION_LATITUDE', Js(2))
var.put('MASK_DEVICE_POSITION_LONGITUDE', Js(1))
var.put('MASK_PAYLOAD_COIL_STATUS', Js(1))
var.put('MASK_PAYLOAD_COIL_VALUE', Js(2))
var.put('MASK_PAYLOAD_COIL_MULTI_CH', Js(4))
var.put('MASK_PAYLOAD_REGISTER_STATUS', Js(1))
var.put('MASK_PAYLOAD_REGISTER_VALUE', Js(2))
var.put('MASK_PAYLOAD_REGISTER_MULTI_CH', Js(4))
var.put('au8CRC8_Pol07_Table', Js([Js(0), Js(7), Js(14), Js(9), Js(28), Js(27), Js(18), Js(21), Js(56), Js(63), Js(54), Js(49), Js(36), Js(35), Js(42), Js(45), Js(112), Js(119), Js(126), Js(121), Js(108), Js(107), Js(98), Js(101), Js(72), Js(79), Js(70), Js(65), Js(84), Js(83), Js(90), Js(93), Js(224), Js(231), Js(238), Js(233), Js(252), Js(251), Js(242), Js(245), Js(216), Js(223), Js(214), Js(209), Js(196), Js(195), Js(202), Js(205), Js(144), Js(151), Js(158), Js(153), Js(140), Js(139), Js(130), Js(133), Js(168), Js(175), Js(166), Js(161), Js(180), Js(179), Js(186), Js(189), Js(199), Js(192), Js(201), Js(206), Js(219), Js(220), Js(213), Js(210), Js(255), Js(248), Js(241), Js(246), Js(227), Js(228), Js(237), Js(234), Js(183), Js(176), Js(185), Js(190), Js(171), Js(172), Js(165), Js(162), Js(143), Js(136), Js(129), Js(134), Js(147), Js(148), Js(157), Js(154), Js(39), Js(32), Js(41), Js(46), Js(59), Js(60), Js(53), Js(50), Js(31), Js(24), Js(17), Js(22), Js(3), Js(4), Js(13), Js(10), Js(87), Js(80), Js(89), Js(94), Js(75), Js(76), Js(69), Js(66), Js(111), Js(104), Js(97), Js(102), Js(115), Js(116), Js(125), Js(122), Js(137), Js(142), Js(135), Js(128), Js(149), Js(146), Js(155), Js(156), Js(177), Js(182), Js(191), Js(184), Js(173), Js(170), Js(163), Js(164), Js(249), Js(254), Js(247), Js(240), Js(229), Js(226), Js(235), Js(236), Js(193), Js(198), Js(207), Js(200), Js(221), Js(218), Js(211), Js(212), Js(105), Js(110), Js(103), Js(96), Js(117), Js(114), Js(123), Js(124), Js(81), Js(86), Js(95), Js(88), Js(77), Js(74), Js(67), Js(68), Js(25), Js(30), Js(23), Js(16), Js(5), Js(2), Js(11), Js(12), Js(33), Js(38), Js(47), Js(40), Js(61), Js(58), Js(51), Js(52), Js(78), Js(73), Js(64), Js(71), Js(82), Js(85), Js(92), Js(91), Js(118), Js(113), Js(120), Js(127), Js(106), Js(109), Js(100), Js(99), Js(62), Js(57), Js(48), Js(55), Js(34), Js(37), Js(44), Js(43), Js(6), Js(1), Js(8), Js(15), Js(26), Js(29), Js(20), Js(19), Js(174), Js(169), Js(160), Js(167), Js(178), Js(181), Js(188), Js(187), Js(150), Js(145), Js(152), Js(159), Js(138), Js(141), Js(132), Js(131), Js(222), Js(217), Js(208), Js(215), Js(194), Js(197), Js(204), Js(203), Js(230), Js(225), Js(232), Js(239), Js(250), Js(253), Js(244), Js(243)]))
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass
pass


# Add lib to the module scope
decoder_advantech_wise_2140 = var.to_python()