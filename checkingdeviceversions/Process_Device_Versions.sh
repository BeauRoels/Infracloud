echo "START DEVICE IOS VERSION CHECK"
REQUIRED_IOS='Cisco IOS XE Software; Version 16.09.05'
VERSION_SEARCH_TEXT='Cisco IOS XE Software, Version'
echo $REQUIRED_IOS

echo $(date +"%F")
echo $(date +"%T")
echo
for f in device_versions/*
do
echo "BEGIN -- Proceesing file $f"
cat $f | grep uptime #hostname
IOS_VERSION=$(cat $f | grep "$VERSION_SEARCH_TEXT" | cut -d' ' -f6)
echo Current IOS Version: $IOS_VERSION
if [ "$REQUIRED_IOS" != "$IOS_VERSION" ]
then
echo Upgrade ios version to: $REQUIRED_IOS
else
echo No upgrade needed
fi
echo "END -- PROCESSING FILE $f"
echo
done
echo "END DEVICE IOS VERSION CHECK"