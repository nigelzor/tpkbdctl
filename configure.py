import hid
from struct import pack

vid = 0x17ef  # Change it for your device
pid = 0x6009  # Change it for your device

with hid.Device(vid, pid) as h:
    print(f'Device manufacturer: {h.manufacturer}')
    print(f'Product: {h.product}')

    _sensitivity = 255
    _press_speed = 180
    _press_to_select = False
    _press_right = False
    _dragging = False
    _release_to_select = False

    props = 0
    props |= 0x01 if _press_to_select else 0x02
    props |= 0x04 if _dragging else 0x08
    props |= 0x10 if _release_to_select else 0x20
    props |= 0x80 if _press_right else 0x40

    h.send_feature_report(pack('BBBBB', 4, props, 3, _sensitivity, _press_speed))
