# Copyright (C) 2019 Chris Younger

import splunk, sys, os, json, shutil

class req(splunk.rest.BaseRestHandler):
    def handle_GET(self):
        # sessionKey = self.sessionKey
            
        # 	server_response, server_content = splunk.rest.simpleRequest('/services/authentication/current-context?output_mode=json', sessionKey=sessionKey, raiseAllErrors=True)
        # 	transforms_content = json.loads(server_content)
        # 	user = transforms_content['entry'][0]['content']['username']
        # 	capabilities = transforms_content['entry'][0]['content']['capabilities']
        # 	# we need to prevent even read access to admins so that people don't call our api and read the .secrets file
        # 	elif not "admin_all_objects" in capabilities:
        # 		status = "missing_perm_read"
        output = ""
        try:
            action = "green" #self.request['form']['color']
            src_folder = os.path.dirname( __file__ )
            dest_folder = os.path.join(os.environ['SPLUNK_HOME'], 'share','splunk', 'search_mrsparkle', 'exposed', 'img')
            output += "Browser icon to be set: " + action + "\n"
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
                    shutil.copyfile(os.path.join(src_folder, action + '.ico'), os.path.join(dest_folder, 'favicon.ico'))
                    output += "SUCCESS: Changed icon. Hit CTRL-F5 to clear your browser cache and observe the change.\n"
                else:
                    output += "ERROR: Cannot file icon for this color.\n"

        except Exception as ex:
            template = "An exception of type {0} occurred. Arguments:\n{1!r}"
            error_stack = template.format(type(ex).__name__, ex.args)
            output += error_stack

        self.response.setHeader('content-type', 'application/json')
        self.response.write(json.dumps({'output': output}, ensure_ascii=False))
