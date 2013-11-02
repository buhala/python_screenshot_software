import win32con, ctypes, ctypes.wintypes,os,requests,base64,win32clipboard,subprocess

def takeScreenshot():
	subprocess.call(["nircmd.exe", "savescreenshot","screen.png"])
	request_headers={'Authorization':'Client-ID c40c9ea5161fd8b'};
	fstream=open("screen.png",'rb')
	imagebase64=base64.b64encode(fstream.read())
	fstream.close()
	post={'image':imagebase64}
	r=requests.post("https://api.imgur.com/3/image",data=post,headers=request_headers)
	print(r.json()['data']['link'])
	win32clipboard.OpenClipboard();
	win32clipboard.EmptyClipboard();
	win32clipboard.SetClipboardText(r.json()['data']['link'])
	win32clipboard.CloseClipboard()

ctypes.windll.user32.RegisterHotKey(None, 1, 0, win32con.VK_SNAPSHOT)

msg = ctypes.wintypes.MSG()
while ctypes.windll.user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
	takeScreenshot()
	ctypes.windll.user32.TranslateMessage(ctypes.byref(msg))
	ctypes.windll.user32.DispatchMessageA(ctypes.byref(msg))
