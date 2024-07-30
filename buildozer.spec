[app]
title = CameraApp
package.name = cameraapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,opencv
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1
build_dir = ./.buildozer
bin_dir = ./bin

# Android specific
fullscreen = 0
android.permissions = android.permission.CAMERA,android.permission.INTERNET
android.api = 31
android.minapi = 21
android.sdk = 31
android.ndk = 25b
android.ndk_api = 21
android.private_storage = True
android.entrypoint = org.kivy.android.PythonActivity
android.service_class_name = org.kivy.android.PythonService
android.gradle_dependencies =
android.enable_androidx = True
android.add_compile_options = "sourceCompatibility = 1.8", "targetCompatibility = 1.8"
android.add_gradle_repositories =
android.add_packaging_options =
android.add_activities =
android.ouya.category = GAME
android.ouya.icon.filename = %(source.dir)s/data/ouya_icon.png
android.custom_manifest =
android.gradle_build_file =
android.aab = False
