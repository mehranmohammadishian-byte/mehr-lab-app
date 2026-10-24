[app]
# (str) Title of your application
title = Mehr Lab

# (str) Package name
package.name = mehrlab

# (str) Package domain (needed for android/ios packaging)
package.domain = org.mehr

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy,kivymd,reportlab,androidstorage4kivy,pyjnius,arabic-reshaper,python-bidi,waxt

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# --- این دو خط مشکل لایسنس و خطای 403 گوگل را حل می‌کنند ---
# پذیرش خودکار لایسنس‌های اندروید
android.accept_sdk_license = True
# استفاده از NDK از پیش نصب شده روی سرور گیت‌هاب (جلوگیری از خطای دانلود)
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724
# -----------------------------------------------------------

# (str) Android entry point, default is ok for Kivy-based app
#android.entrypoint = org.kivy.android.PythonActivity

# (list) Pattern to whitelist for the compilation of the application
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (list) List of Java .jar files to add to the libs so that pyjnius can access
#android.add_jars = foo.jar,bar.jar,path/to/more/*.jar

# (list) List of Java files to add to the android project (can be java or a
# directory containing the files)
#android.add_src =

# (list) Android AAR archives to add
#android.add_aars =

# (list) Put these files or directories in the apk res directory.
#android.add_resources =

# (list) Gradle dependencies to add
#android.gradle_dependencies =

# (bool) Enable AndroidX support. Enable when 'android.gradle_dependencies'
#android.enable_androidx = True

# (list) add java compile options
#android.add_compile_options =

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a, armeabi-v7a

# (str) The SDK dir
#android.sdk_path =

# (str) Log level, one of 0 (quiet), 1 (default), 2 (debug)
log_level = 2
