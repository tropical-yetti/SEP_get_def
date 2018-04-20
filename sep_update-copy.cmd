@echo off

REM PRE-setting ambience
IF EXIST s:\ (
	NET USE /delete s: /y
)
NET USE s: "\\192.168.1.1\serverfolder"

SET orig=S:\
SET dest=%temp%
reg Query "HKLM\Hardware\Description\System\CentralProcessor\0" | find /i "x86" > NUL && SET OS=32BIT || SET OS=64BIT
CD %dest%

REM Find the server for new definitions
PUSHD %orig%
IF %OS%==32BIT (
	SET "seq="
	FOR %%f IN (*-v5i32.exe) DO SET seq=!seq! %%f
) ELSE (
	SET "seq="
	FOR %%f IN (*-v5i64.exe) DO SET seq=!seq! %%f
)

REM Select the file name in the string
SET sep_update=%seq:!seq! =%

POPD

REM Copy only if it is necessary
IF NOT EXIST %sep_update% (
	XCOPY %orig%\%sep_update% %dest% /sy
)

REM Installing
%sep_update% /q

REM Clear old definitions installers from %TEMP% folder
IF %OS%==32BIT (
	IF EXIST *v5i32.exe DEL *v5i32.exe
) ELSE (
	IF EXIST *v5i64.exe DEL *v5i64.exe
)

REM Leaving everything as it was
SET orig=
SET dest=
SET OS=
SET seq=
SET sep_update=

NET USE /delete s: /y
