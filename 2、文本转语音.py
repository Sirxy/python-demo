# coding: utf-8
# author: xuyang
# created_time: 2020/12/19

from win32com.client import Dispatch

msg = '你好 SAPI'
speaker = Dispatch('SPAI.SpVoice')
speaker.Speak(msg)
del speaker

"""
Traceback (most recent call last):
  File "C:\Users\XH\AppData\Roaming\Python\Python37\site-packages\win32com\client\dynamic.py", line 89, in _GetGoodDispatch
    IDispatch = pythoncom.connect(IDispatch)
pywintypes.com_error: (-2147221005, '无效的类字符串', None, None)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:/dev/南宁的后台工程等/30上的后台和sdk/hzsys/2、文本转语音.py", line 8, in <module>
    speaker = Dispatch('SPAI.SpVoice')
  File "C:\Users\XH\AppData\Roaming\Python\Python37\site-packages\win32com\client\__init__.py", line 95, in Dispatch
    dispatch, userName = dynamic._GetGoodDispatchAndUserName(dispatch,userName,clsctx)
  File "C:\Users\XH\AppData\Roaming\Python\Python37\site-packages\win32com\client\dynamic.py", line 114, in _GetGoodDispatchAndUserName
    return (_GetGoodDispatch(IDispatch, clsctx), userName)
  File "C:\Users\XH\AppData\Roaming\Python\Python37\site-packages\win32com\client\dynamic.py", line 91, in _GetGoodDispatch
    IDispatch = pythoncom.CoCreateInstance(IDispatch, None, clsctx, pythoncom.IID_IDispatch)
pywintypes.com_error: (-2147221005, '无效的类字符串', None, None)
"""
