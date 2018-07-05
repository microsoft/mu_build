## @file
# Standardized Error Hanlding infrastructures.
#
# Copyright (c) 2011 - 2018, Intel Corporation. All rights reserved.<BR>
#
# This program and the accompanying materials are licensed and made available
# under the terms and conditions of the BSD License which accompanies this
# distribution. The full text of the license may be found at
# http://opensource.org/licenses/bsd-license.php
#
# THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
#

'''
ToolError
'''

import Logger.StringTable as ST

FILE_OPEN_FAILURE = 1
FILE_WRITE_FAILURE = 2
FILE_PARSE_FAILURE = 3
FILE_READ_FAILURE = 4
FILE_CREATE_FAILURE = 5
FILE_CHECKSUM_FAILURE = 6
FILE_COMPRESS_FAILURE = 7
FILE_DECOMPRESS_FAILURE = 8
FILE_MOVE_FAILURE = 9
FILE_DELETE_FAILURE = 10
FILE_COPY_FAILURE = 11
FILE_POSITIONING_FAILURE = 12
FILE_ALREADY_EXIST = 13
FILE_NOT_FOUND = 14
FILE_TYPE_MISMATCH = 15
FILE_CASE_MISMATCH = 16
FILE_DUPLICATED = 17
FILE_UNKNOWN_ERROR = 0x0FFF

OPTION_UNKNOWN = 0x1000
OPTION_MISSING = 0x1001
OPTION_CONFLICT = 0x1002
OPTION_VALUE_INVALID = 0x1003
OPTION_DEPRECATED = 0x1004
OPTION_NOT_SUPPORTED = 0x1005
OPTION_UNKNOWN_ERROR = 0x1FFF

PARAMETER_INVALID = 0x2000
PARAMETER_MISSING = 0x2001
PARAMETER_UNKNOWN_ERROR = 0x2FFF

FORMAT_INVALID = 0x3000
FORMAT_NOT_SUPPORTED = 0x3001
FORMAT_UNKNOWN = 0x3002
FORMAT_UNKNOWN_ERROR = 0x3FFF

RESOURCE_NOT_AVAILABLE = 0x4000
RESOURCE_ALLOCATE_FAILURE = 0x4001
RESOURCE_FULL = 0x4002
RESOURCE_OVERFLOW = 0x4003
RESOURCE_UNDERRUN = 0x4004
RESOURCE_UNKNOWN_ERROR = 0x4FFF

ATTRIBUTE_NOT_AVAILABLE = 0x5000
ATTRIBUTE_GET_FAILURE = 0x5001
ATTRIBUTE_SET_FAILURE = 0x5002
ATTRIBUTE_UPDATE_FAILURE = 0x5003
ATTRIBUTE_ACCESS_DENIED = 0x5004
ATTRIBUTE_RETRIEVE_FAILURE = 0x5005
ATTRIBUTE_UNKNOWN_ERROR = 0x5FFF
ATTRIBUTE_RETRIEVE_FAILURE = 0x5F00

IO_NOT_READY = 0x6000
IO_BUSY = 0x6001
IO_TIMEOUT = 0x6002
IO_UNKNOWN_ERROR = 0x6FFF

COMMAND_FAILURE = 0x7000

CODE_ERROR = 0xC0DE

AUTOGEN_ERROR = 0xF000
PARSER_ERROR = 0xF001
BUILD_ERROR = 0xF002
GENFDS_ERROR = 0xF003
ECC_ERROR = 0xF004
EOT_ERROR = 0xF005
DDC_ERROR = 0xF009
WARNING_AS_ERROR = 0xF006
MIGRATION_ERROR = 0xF010
EDK1_INF_ERROR = 0xF011
ABORT_ERROR = 0xFFFE
UNKNOWN_ERROR = 0xFFFF

UPT_ALREADY_INSTALLED_ERROR = 0xD000
UPT_ENVIRON_MISSING_ERROR = 0xD001
UPT_REPKG_ERROR = 0xD002
UPT_ALREADY_RUNNING_ERROR = 0xD003
UPT_MUL_DEC_ERROR = 0xD004
UPT_DB_UPDATE_ERROR = 0xD005
UPT_INI_PARSE_ERROR = 0xE000

## Error message of each error code
#
gERROR_MESSAGE = {
    FILE_NOT_FOUND          :   ST.ERR_FILE_NOT_FOUND,
    FILE_OPEN_FAILURE       :   ST.ERR_FILE_OPEN_FAILURE,
    FILE_WRITE_FAILURE      :   ST.ERR_FILE_WRITE_FAILURE,
    FILE_PARSE_FAILURE      :   ST.ERR_FILE_PARSE_FAILURE,
    FILE_READ_FAILURE       :   ST.ERR_FILE_READ_FAILURE,
    FILE_CREATE_FAILURE     :   ST.ERR_FILE_CREATE_FAILURE,
    FILE_CHECKSUM_FAILURE   :   ST.ERR_FILE_CHECKSUM_FAILURE,
    FILE_COMPRESS_FAILURE   :   ST.ERR_FILE_COMPRESS_FAILURE,
    FILE_DECOMPRESS_FAILURE :   ST.ERR_FILE_DECOMPRESS_FAILURE,
    FILE_MOVE_FAILURE       :   ST.ERR_FILE_MOVE_FAILURE,
    FILE_DELETE_FAILURE     :   ST.ERR_FILE_DELETE_FAILURE,
    FILE_COPY_FAILURE       :   ST.ERR_FILE_COPY_FAILURE,
    FILE_POSITIONING_FAILURE:   ST.ERR_FILE_POSITIONING_FAILURE,
    FILE_ALREADY_EXIST      :   ST.ERR_FILE_ALREADY_EXIST,
    FILE_TYPE_MISMATCH      :   ST.ERR_FILE_TYPE_MISMATCH ,
    FILE_CASE_MISMATCH      :   ST.ERR_FILE_CASE_MISMATCH,
    FILE_DUPLICATED         :   ST.ERR_FILE_DUPLICATED,
    FILE_UNKNOWN_ERROR      :   ST.ERR_FILE_UNKNOWN_ERROR,

    OPTION_UNKNOWN          :   ST.ERR_OPTION_UNKNOWN,
    OPTION_MISSING          :   ST.ERR_OPTION_MISSING,
    OPTION_CONFLICT         :   ST.ERR_OPTION_CONFLICT,
    OPTION_VALUE_INVALID    :   ST.ERR_OPTION_VALUE_INVALID,
    OPTION_DEPRECATED       :   ST.ERR_OPTION_DEPRECATED,
    OPTION_NOT_SUPPORTED    :   ST.ERR_OPTION_NOT_SUPPORTED,
    OPTION_UNKNOWN_ERROR    :   ST.ERR_OPTION_UNKNOWN_ERROR,

    PARAMETER_INVALID       :   ST.ERR_PARAMETER_INVALID,
    PARAMETER_MISSING       :   ST.ERR_PARAMETER_MISSING,
    PARAMETER_UNKNOWN_ERROR :   ST.ERR_PARAMETER_UNKNOWN_ERROR,

    FORMAT_INVALID          :   ST.ERR_FORMAT_INVALID,
    FORMAT_NOT_SUPPORTED    :   ST.ERR_FORMAT_NOT_SUPPORTED,
    FORMAT_UNKNOWN          :   ST.ERR_FORMAT_UNKNOWN,
    FORMAT_UNKNOWN_ERROR    :   ST.ERR_FORMAT_UNKNOWN_ERROR,

    RESOURCE_NOT_AVAILABLE  :   ST.ERR_RESOURCE_NOT_AVAILABLE,
    RESOURCE_ALLOCATE_FAILURE : ST.ERR_RESOURCE_ALLOCATE_FAILURE,
    RESOURCE_FULL           :   ST.ERR_RESOURCE_FULL,
    RESOURCE_OVERFLOW       :   ST.ERR_RESOURCE_OVERFLOW,
    RESOURCE_UNDERRUN       :   ST.ERR_RESOURCE_UNDERRUN,
    RESOURCE_UNKNOWN_ERROR  :   ST.ERR_RESOURCE_UNKNOWN_ERROR,

    ATTRIBUTE_NOT_AVAILABLE :   ST.ERR_ATTRIBUTE_NOT_AVAILABLE,
    ATTRIBUTE_RETRIEVE_FAILURE : ST.ERR_ATTRIBUTE_RETRIEVE_FAILURE,
    ATTRIBUTE_SET_FAILURE   :   ST.ERR_ATTRIBUTE_SET_FAILURE,
    ATTRIBUTE_UPDATE_FAILURE:   ST.ERR_ATTRIBUTE_UPDATE_FAILURE,
    ATTRIBUTE_ACCESS_DENIED :   ST.ERR_ATTRIBUTE_ACCESS_DENIED,
    ATTRIBUTE_UNKNOWN_ERROR :   ST.ERR_ATTRIBUTE_UNKNOWN_ERROR,

    COMMAND_FAILURE         :   ST.ERR_COMMAND_FAILURE,

    IO_NOT_READY            :   ST.ERR_IO_NOT_READY,
    IO_BUSY                 :   ST.ERR_IO_BUSY,
    IO_TIMEOUT              :   ST.ERR_IO_TIMEOUT,
    IO_UNKNOWN_ERROR        :   ST.ERR_IO_UNKNOWN_ERROR,

    UNKNOWN_ERROR           :   ST.ERR_UNKNOWN_ERROR,

    UPT_ALREADY_INSTALLED_ERROR : ST.ERR_UPT_ALREADY_INSTALLED_ERROR,
    UPT_ENVIRON_MISSING_ERROR   : ST.ERR_UPT_ENVIRON_MISSING_ERROR,
    UPT_REPKG_ERROR             : ST.ERR_UPT_REPKG_ERROR,
    UPT_ALREADY_RUNNING_ERROR   : ST.ERR_UPT_ALREADY_RUNNING_ERROR,
    UPT_MUL_DEC_ERROR           : ST.ERR_MUL_DEC_ERROR,
    UPT_INI_PARSE_ERROR     :   ST.ERR_UPT_INI_PARSE_ERROR,
}

## Exception indicating a fatal error
#
class FatalError(Exception):
    pass

