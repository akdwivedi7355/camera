[app]
# (list) List of inclusions using pattern matching
# e.g. include extesions like '.py', '.png' and '.kv' files
source.include_exts = py,png,jpg,kv,atlas

# (string) Title of your application
title = CameraApp

# (string) Package name
package.name = cameraapp

# (string) Package domain (unique identifier, usually in reverse domain format)
package.domain = org.example

# (string) Application versioning (numeric version string)
version = 1.0

# (list) Application requirements
# e.g. 'kivy', 'opencv-python', etc.
requirements = python3,kivy,opencv-python

# (string) Supported orientations (portrait or landscape)
orientation = portrait

[buildozer]
# (int) Log level
# 0 = default
# 1 = debug
# 2 = verbose
log_level = 2

# (bool) Whether to use a specific SDK version
# Use '1' to accept SDK licenses if needed
app_android_accept_sdk_license = 1

# (bool) Whether to warn when running as root
warn_on_root = 1

[android]
# (int) Minimum API level required
android.minapi = 21

# (int) Target API level
android.api = 31

# (int) Android SDK version
android.sdk = 30

# (string) Android NDK version
android.ndk = 23b

# (bool) Whether to use a custom gradle.properties file
# Use 'true' if you have a custom gradle.properties file
use_custom_gradle_properties = false

# (string) Custom gradle.properties file
gradle_properties_file = 

# (bool) Whether to include the SDL2 bootstrap
# Use 'true' if you need it
include_sdl2_bootstrap = true

# (bool) Whether to include the SDL2-image library
# Use 'true' if you need it
include_sdl2_image = true

# (bool) Whether to include the SDL2-mixer library
# Use 'true' if you need it
include_sdl2_mixer = true

# (bool) Whether to include the SDL2-ttf library
# Use 'true' if you need it
include_sdl2_ttf = true

# (bool) Whether to include the android support libraries
# Use 'true' if you need it
include_android_support = true

[buildozer]
# (string) Directory to store build artifacts
build_dir = ./.buildozer

# (string) Path to the buildozer binary
buildozer_bin = ./bin

# (string) Path to the android platform
android_platform = ./platform

# (string) Path to the android toolchain
android_toolchain = ./toolchain
