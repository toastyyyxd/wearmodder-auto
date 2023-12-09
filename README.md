# WearModder Auto - Automatically scalling sideloaded apps for WearOS
While WearModder has made it easy to scale other Android apps for WearOS, this should only require basic knowledge to use.

## Installation
You need Java and Python 3 to use this.\
All java executables are included and there are no extra python dependencies.

## Usage
Clone this repo or download as a zip then open it inside a command line.
```
python main.py [ORIGINAL-APK]
```
Outputs `[NAME]-w.apk`

## Description
This script essentially automates the proccess required to make an apk usable on WearOS.
1. Decompile with apktool
2. Process with py-WearModder
3. Build with apktool
4. Sign with uber-apk-signer

Note that this doesn't include the "manual adjustments" as mentioned in the original XDA thread,
the original thread didn't specify what adjustments should've been made and probably varied with different apps,
tested on Spotify Lite and it should work fine without them.

## Credits
[Original WearModder](https://github.com/moneytoo/WearModder) made by [moneytoo](https://github.com/moneytoo), also on [XDA](https://xdaforums.com/t/app-mod-spotify-lite-scaled-for-standalone-use-on-wear-os.3815680/)\
[Python WearModder](https://github.com/wolfinabox/py-wearmodder) ported by [wolfinabox](https://github.com/wolfinabox)\
[Apktool](https://github.com/iBotPeaches/Apktool) made by [iBotPeaches](https://github.com/iBotPeaches/Apktool), this uses [v2.9.1](https://github.com/iBotPeaches/Apktool/releases/tag/v2.9.1)\
[uber-apk-signer](https://github.com/patrickfav/uber-apk-signer) made by [patrickfav](https://github.com/patrickfav/uber-apk-signer), this uses [v1.3.0](https://github.com/patrickfav/uber-apk-signer/releases/tag/v1.3.0)
