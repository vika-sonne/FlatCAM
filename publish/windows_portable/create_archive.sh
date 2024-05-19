
VERSION="2024_4"
BUILD_PATH="_build"
ARCHIVE_FILE_PATH="$BUILD_PATH/FlatCAM_${VERSION}_windows_portable.7z"

BOLD="\033[1m"
CLEAR="\033[0m"

echo -e "Create windows portable archive: ${BOLD}${ARCHIVE_FILE_PATH}${CLEAR}"

echo "Remove existing archive:"
rm -rfv "$ARCHIVE_FILE_PATH"

7z a -mx9 "$ARCHIVE_FILE_PATH" Python310 FlatCAM*
