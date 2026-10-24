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

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# --- تنظیمات حیاتی برای گیت‌هاب اکشنز ---
# این خط مجوزهای اندروید را خودکار قبول می‌کند
android.accept_sdk_license = True

# این خط به Buildozer می‌گوید NDK را دانلود نکن و از نسخه نصب شده روی سرور استفاده کن (حل مشکل 403)
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724
# ----------------------------------------

[buildozer]

# (int) Log level (0 = quiet, 1 = default, 2 = debug)
log_level = 2

# (int) Warn on root
warn_on_root = 1
