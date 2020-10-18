import ctypes

PROCESS_ALL_ACCESS = (0x000F0000 | 0x00100000 | 0xFFF)

u_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

lpClassName = None
lpWindowName = ctypes.c_char_p(input("Enter a window name to kill: ").encode("utf-8"))

hWnd = u_handle.FindWindowA(lpClassName, lpWindowName)  # Grabs unprivelidged handle

if (hWnd == 0):
    print("Error: {0} - Could not get handle to the process.".format(k_handle.GetLastError()))
    exit(1)

lpdwProcessID = ctypes.c_ulong()

response = u_handle.GetWindowThreadProcessId(hWnd, ctypes.byref(lpdwProcessID))

if (response == 0):
    print("Error: {0} - Could not get PID.".format(k_handle.GetLastError()))
    exit(1)

dwDesiredAccess = PROCESS_ALL_ACCESS
bInheritHandle = False
dwProcessID = lpdwProcessID

hProcess = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, lpdwProcessID)  # Grabs a privelidged handle

if (hProcess <= 0):
    print("Error: {0} - Could not grab privelidged handle to process.".format(k_handle.GetLastError()))
    exit(1)

uExitCode = 0x1

response = k_handle.TerminateProcess(hProcess, uExitCode)

if (response == 0):
    print("Error: {0} - Could not terminate process.".format(k_handle.GetLastError()))
    exit(1)
else:
    print("Process terminated.")
