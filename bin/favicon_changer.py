# Copyright (C) 2019 Chris Younger

# https://192.168.1.11:8489/services/favicon_changer?icon=red
# | rest splunk_server=local /services/favicon_changer icon=orange

import splunk, sys, os, shutil

class req(splunk.rest.BaseRestHandler):
    def handle_GET(self):
        output = ""
        try:
            if "query" in self.request and "icon" in self.request['query'] and not self.request['query']['icon'] is None:
                action = self.request['query']['icon'].replace("?output_mode=json","")
                src_folder = os.path.join(os.path.dirname( __file__ ), "..", "appserver", "static")
                dest_folder = os.path.join(os.environ['SPLUNK_HOME'], 'share','splunk', 'search_mrsparkle', 'exposed', 'img')
                output += "Setting browser icon to: " + action + "\n"
                if action == "original":
                    if not os.path.exists(os.path.join(dest_folder, 'favicon.ico.orig')):
                        output += "ERROR: Cannot restore original icon becuase backup file is missing. Restore the file from original installation package.\n"
                    else:
                        shutil.copyfile(os.path.join(dest_folder, 'favicon.ico.orig'), os.path.join(dest_folder, 'favicon.ico'))
                        output += "SUCCESS: Restored original file. Hit CTRL-F5 to clear your browser cache and observe the change.\n"
                else: 
                    # if backup file does not already exist
                    if not os.path.exists(os.path.join(dest_folder, 'favicon.ico.orig')):
                        shutil.copyfile(os.path.join(dest_folder, 'favicon.ico'), os.path.join(dest_folder, 'favicon.ico.orig'))
                    if os.path.exists(os.path.join(src_folder, action + '.ico')):
                        os.chmod(os.path.join(dest_folder, 'favicon.ico'), 0644)
                        shutil.copyfile(os.path.join(src_folder, action + '.ico'), os.path.join(dest_folder, 'favicon.ico'))
                        output += "SUCCESS: Changed icon. Hit CTRL-F5 to clear your browser cache and observe the change.\n"
                    else:
                        output += "ERROR: Cannot find icon for this color.\n"
            else:
                output += "ERROR: You must supply the 'icon' argument specifying which favicon to set"
        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            error_stack = template.format(type(ex).__name__, ex.args)
            output += error_stack
        self.response.setHeader('content-type', 'text/plain')
        self.response.write(output)
