import ctypes

k_handle = ctypes.WinDLL("Kernel32.dll")
PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)
dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False

intProcessID = int(input("Enter a PID: "))
dwProcessID = int(hex(intProcessID), base=16)

response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessID)

if (response <= 0):
    print("Handle was not created.")
    error = k_handle.GetLastError()
    if (error != 0):
        print("Error: {0}".format(error))
        exit(1)
else:
    print("Handle created!")