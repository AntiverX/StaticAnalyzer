# -*- coding: utf_8 -*-
"""Module for strings-method for java."""

import io
import subprocess
from lxml import etree
import json

from django.conf import settings

from MobSF.utils import (
    PrintException
)


# def strings(app_file, app_dir, tools_dir):
#     """Extract the strings from an app."""
#     try:
#         print "[INFO] Extracting Strings from APK"
#         strings_jar = tools_dir + 'strings_from_apk.jar'
#         args = [
#             settings.JAVA_PATH + 'java',
#             '-jar', strings_jar, app_dir + app_file, app_dir
#         ]
#         subprocess.call(args)
#         dat = ''
#         try:
#             with io.open(
#                 app_dir + 'strings.json',
#                 mode='r',
#                 encoding="utf8",
#                 errors="ignore"
#             ) as file_pointer:
#                 dat = file_pointer.read()
#         except:
#             pass
#         dat = dat[1:-1].split(",")
#         dat = ["LALA","DADA"]
#         return dat
#     except:
#         PrintException("[ERROR] Extracting Strings from APK")

def strings(app_file, app_dir, tools_dir):
    """Extract the strings from an app."""
    try:
        print "[INFO] Extracting Strings from APK"
        strings_jar = tools_dir + 'apktool.jar'
        args = [
            settings.JAVA_PATH + 'java',
            '-jar', strings_jar,'d', app_dir + app_file,'-o', app_dir + app_file[:-4]
        ]
        subprocess.call(args)

        tree = etree.parse(app_dir + app_file[:-4]+"/res/values/strings.xml")
        root = tree.getroot()
        list = []
        for article in root:
            name = article.get("name")
            list.append(name)
            list.append(article.text)
        data = {}
        for i in range(len(list) // 2):
            data[list[2 * i]] = list[2 * i + 1]

        json_format = json.dumps(data, ensure_ascii=False, indent=2)
        return json_format[1:-1].split(",")
        # return json_format
    except:
        PrintException("[ERROR] Extracting Strings from APK")
    #     dat = ''
    #     try:
    #         with io.open(
    #             app_dir + 'strings.json',
    #             mode='r',
    #             encoding="utf8",
    #             errors="ignore"
    #         ) as file_pointer:
    #             dat = file_pointer.read()
    #     except:
    #         pass
    #     dat = dat[1:-1].split(",")
    #     dat = ["LALA","DADA"]
    #     return dat
    # except:
    #     PrintException("[ERROR] Extracting Strings from APK")