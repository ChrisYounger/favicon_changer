# Browser Icon Changer (favicon)

A simple app to change the Splunk browser icon. When you have many tabs open, spread across to different Splunk environments (e.g. Prod vs non-Prod), this makes it easier to differentiate what each tab is for. You may also want to differentiate dedicated Splunk management instances (e.g. monitoring console or cluster master) from your main search head/s.

![screenshot](https://raw.githubusercontent.com/ChrisYounger/favicon_changer/master/static/browser.png)


WARNING: Changing the browser icon will cause Splunk to periodically show a "File integrity" messages to all Administrators. These messages can be safely ignored for `favicon.ico`. For this reason, changing the browser icon is not recommended for production environments.

* Splunk upgrades will restore the original icon.
* Compatible with search head clusters.
* This app is only visible to Administrators and the rest API requires `admin_all_objects` capability.


Copyright (C) 2019 Chris Younger I am a Splunk Professional Services consultant working for JDS Australia, in Brisbane Australia.

[Source code](https://github.com/ChrisYounger/favicon_changer) | [Splunkbase](https://splunkbase.splunk.com/app/XXXX/) | [Questions, Bugs or Suggestions](https://answers.splunk.com/app/questions/XXXX.html) | [My Splunk apps](https://splunkbase.splunk.com/apps/#/author/chrisyoungerjds)




## Usage

Install the app using the Splunk normal app install method.

As a admin user, navigate to the app and click the desired icon.

To see the new icon hit CTRL-F5 to reload the page and clear the browser cache.

Other Splunk users will also need to clear their cache (`CTRL-F5`) to see the icon.

When you need  upgrade Splunk, repeat the above process.



## Third party software

The following third-party software is used by this app. Thank you!

* jQuery - MIT - https://jquery.com/
* Font Awesome - Creative Commons Attribution-ShareAlike 4.0 License - https://fontawesome.com/
