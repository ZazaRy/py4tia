import ctypes

proto_ed_lib = ctypes.CDLL("./libdice.so")

proto_ed_lib.init.argtypes = []
proto_ed_lib.init.restype = None
proto_ed_lib.roll.argtypes = (ctypes.c_uint64, ctypes.c_uint64)
proto_ed_lib.roll.restype = ctypes.c_uint64
proto_ed_lib.__new__

proto_ed_lib.init()

def zig_roll(x, y):
    return proto_ed_lib.roll(x, y)
