[app]
title = Super Secret Group
package.name = supersgroup
package.domain = org.supersecret

source.dir = .
source.include_exts = py

version = 1.0
requirements = python3,kivy

[buildozer]
log_level = 1

[android]
api = 33
minapi = 21
android.allow_backup = false
android.accept_sdk_license = true

[app:source.exclude_patterns]
license,images,doc,tests
