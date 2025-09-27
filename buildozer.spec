[app]
title = MrAnatas9 Secret System
package.name = mranatas9app
package.domain = org.mranatas9

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

version = 1.0
requirements = python3,kivy

[buildozer]
log_level = 1

[android]
api = 33
minapi = 21
android.accept_sdk_license = True

[app:source.exclude_patterns]
license,images,doc,tests
