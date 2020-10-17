import ctypes

user_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

hWnd = None  # None in place of NULL. We dont need to specify the user of the window
lpText = "Hello World"  # Text to display in window
lpTitle = "Hello"  # Title of the window
uType = 0x00000001  # Simple, Ok and Cancel with text message box type

response = user_handle.MessageBoxW(hWnd, lpText, lpTitle, uType)  # Display the window

error = k_handle.GetLastError()  # Retrieve the last error from the windows kernel

if (error != 0):
    print("Error: {0}".format(error))
    exit(1)

if (response == 1):
    print("User clicked OK!")
elif (response == 2):
    print("User clicked Cancel :(")  # Note clicking the 'x' icon is always the same as cancel
