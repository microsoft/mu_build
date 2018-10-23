@rem @file buildtoolshere.bat
@rem Run this to build the tools right where they are.
@rem
@rem Copyright (c) 2018, Microsoft Corporation
@rem
@rem All rights reserved.
@rem Redistribution and use in source and binary forms, with or without
@rem modification, are permitted provided that the following conditions are met:
@rem 1. Redistributions of source code must retain the above copyright notice,
@rem this list of conditions and the following disclaimer.
@rem 2. Redistributions in binary form must reproduce the above copyright notice,
@rem this list of conditions and the following disclaimer in the documentation
@rem and/or other materials provided with the distribution.
@rem
@rem THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
@rem ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
@rem WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
@rem IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
@rem INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
@rem BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
@rem DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
@rem LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
@rem OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
@rem ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
@rem

@echo off
pushd .

cd %~dp0

set EDK_TOOLS_PATH=%CD%
set BASE_TOOLS_PATH=%EDK_TOOLS_PATH%
set TEMP_PATH=%PATH%
set PATH=%PATH%;%BASE_TOOLS_PATH%\Bin\Win32
call %BASE_TOOLS_PATH%\toolsetup.bat Rebuild
goto end

:end
set EDK_TOOLS_PATH=
set BASE_TOOLS_PATH=
set PATH=%TEMP_PATH%
set TEMP_PATH=
popd
