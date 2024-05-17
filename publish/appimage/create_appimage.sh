
export TARGET_APPDIR=`readlink --canonicalize AppDir`

appimage-builder --recipe AppImageBuilder.yml
