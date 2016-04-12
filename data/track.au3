

$gameInCurMinute = 1

ConsoleWrite("Ready?! Start in 5 seconds"&@CRLF)
Sleep(7000)

$fileToCopy = @DesktopDir&"\bet365.html"
$i = 0
; loop every ~20sec, 3times per minute, 100 - $gameInCurMinute minutes left
; 90 +extra time (10) + half time (15) ~ 115minutes
While $i < 3*(115 - $gameInCurMinute)

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
   ConsoleWrite($newFile&@CRLF)

   FileCopy($fileToCopy, $newFile)
   Sleep(10000)
WEnd





