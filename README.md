# Insta360-Livestream
Since insta360 doesn't offer the possibility to get the livestream with a computer without a cell phone in between I reverse engineered the apk (v1.18.2), found the port 6666, then analyzed a tcpdump of my cell phone and the camera and rebuilt the tcp communication to get the livestream of the camera.

Search for a Wi-Fi station with the name of “ONE R XXXXX”, and connect to the Wi-Fi with the password of 88888888. 
App version 1.7.1 offers the possibility to set the language to Indonesia and thus limit the wifi to 2.4GHz

The livestream is <b>HEVC/H.265</b> encoded, has a resolution of <b>1440x720 pixels</b>  at <b>30 FPS</b> and is in <b>dual fisheye</b> format. 
 
![Vlcsnap-2022-07-25-09h34m59s583](https://user-images.githubusercontent.com/18678779/182454958-9ef98665-897a-4f98-9c56-166fb64f7025.png)


## Tested cameras
<table>
<tr>
    <th>Model</th>
    <th>Status</th>
    <th>Firmware</th>
</tr>
<tr>
 <td>BetaFPV SMO 360</td>
 <td>✓</td>
  <td>v10.1.25, <a href="Insta360OneRFW.bin">v10.1.26</a></td>
</tr>
<tr>
 <td>Insta 360 One R</td>
 <td>✓ but lost some frames</td>
 <td>-</td>
 </tr>
 <tr>
 <td>Insta360 X3</td>
 <td>✘ camera display flickers, rx no usable video data</td>
 <td>v1.0.04</td>
 </tr>
</table>


## Basic commands

```
#start script:
$ python3 insta360hevc.py

#play written data:
$ ffplay data.bin

#or convert to mp4
$ ffmpeg -i data.bin data.mp4
```
