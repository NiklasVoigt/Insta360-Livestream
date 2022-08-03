# Insta360-Livestream
Since insta360 doesn't offer the possibility to get the livestream with a computer without a cell phone in between I reverse engineered the apk (v1.18.2), found the port 6666, then analyzed a tcpdump of my cell phone and the camera and rebuilt the tcp communication to get the livestream of the camera.

You can connect via WLAN with 88888888. 

The livestream is <b>HEVC/H.265</b> encoded, has a resolution of <b>1440x720 pixels</b>  at <b>30 FPS</b> and is in <b>dual fisheye</b> format. 
 
![Vlcsnap-2022-07-25-09h34m59s583](https://user-images.githubusercontent.com/18678779/182454958-9ef98665-897a-4f98-9c56-166fb64f7025.png)


## Tested cameras
<table>
<tr>
    <th>Name</th>
   <th>Model</th>
    <th>Status</th>
    <th>Firmware</th>
</tr>
<tr>
 <td>BetaFPV SMO 360</td>
 <td>Insta360 OneR</td>
 <td>✓</td>
  <td>v10.1.25</td>
</tr>
<tr>
 <td>Insta 360 One R</td>
 <td>-</td>
 <td>✓</td>
 <td>-</td>
 </tr>
</table>
