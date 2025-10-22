[app]

# (str) Title of your application
title = TerraForge Studio

# (str) Package name
package.name = terraforgestudio

# (str) Package domain (needed for android/ios packaging)
package.domain = com.terraforge

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,md,json

# (list) List of inclusions using pattern matching
source.include_patterns = frontend-new/dist/*,realworldmapgen/*,desktop/icon.png

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec,pyc,pyo

# (list) List of directory to exclude (let empty to not exclude anything)
source.exclude_dirs = tests,bin,venv,env,.git,build,dist,desktop/dist,desktop/build

# (str) Application versioning (method 1)
version = 1.0.2

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy==2.3.0,android,pyjnius,pillow,requests,fastapi,uvicorn,starlette,pydantic,h11,httptools,websockets,watchfiles,python-multipart,anyio,sniffio,click,numpy,shapely,geopandas,rasterio,pyproj

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# requirements.source.kivy = ../../kivy

# (str) Presplash of the application
presplash.filename = desktop/icon.png

# (str) Icon of the application
icon.filename = desktop/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for android toolchain)
android.presplash_color = #667EEA

# (string) Presplash animation using Lottie format.
# android.presplash_lottie = "path/to/lottie/file.json"

# (list) Permissions
android.permissions = INTERNET,ACCESS_NETWORK_STATE,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,CAMERA

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android logcat filters to use
android.logcat_filters = *:S python:D

# (bool) Android logcat only display log for activity's pid
android.logcat_pid_only = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.archs = arm64-v8a,armeabi-v7a

# (bool) enables Android auto backup feature (Android API >=23)
android.allow_backup = True

# (str) The format used to package the app for release mode (aab or apk).
android.release_artifact = apk

# (bool) Skip byte compile for .py files
android.no-byte-compile-python = False

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer

# (str) Path to build output (i.e. .apk, .ipa) storage
bin_dir = ./bin
