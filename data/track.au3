
ConsoleWrite("Ready?! Start in 5 seconds"&@CRLF)
Sleep(5000)

$fileToCopy = @DesktopDir&"\bet365.html"
$i = 0
While True

   If FileExists($fileToCopy) Then
	  ;ConsoleWrite("Deleting!"&@CRLF)
	  FileDelete($fileToCopy)
	  DirRemove(@DesktopDir&"\bet365_files",1)
   EndIf
   
	  
   Send("^s")
   sleep(3000)

   Send("{TAB}")
   Sleep(500)
   Send("{TAB}")
   Sleep(500)
   Send("{TAB}")
   Sleep(500)

   Send("{ENTER}")

   Sleep(500)
   Send("{LEFT}")
   Sleep(500)
   Send("{ENTER}")

   Sleep(5000)

   $i=$i+1

   $newFile = @ScriptDir&"\"&$i&".html"
   ;ConsoleWrite($fileToCopy&@CRLF)
   ConsoleWrite($newFile&@CRLF)

   FileCopy($fileToCopy, $newFile)
   
   Sleep(10000)
WEnd





