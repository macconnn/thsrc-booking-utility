# THSRC-booking-utility

## 聲明
該工具僅提供python爬蟲學習使用，一般使用並不會對網站造成損害，另請勿使用該工具惡意攻擊網站或非法用途，若使用該工具大量購票而觸及中華民國法律，後果請自負。


## Description
This utility helps automate THSRC ticket bookings. Users can choose the specific date and start/end stations of their choice
but the smallest time unit available is half an hour

## Dependencies 
* Python3
* requests
* BeautifulSoup4
* lxml
* Pillow

## Getting started

### Config
The first thing is to fill out the config file in /resources/config.
Please follow the rules below
```
{
	"station_start" : "1",
	"station_end" : "12",
	"date" : "2023/10/05",
	"times" : "1230P"
}
```
### Parameters
#### station
The following are the station name of the code
```
Nangang 	= 1
Taipei 		= 2
Banqiao 	= 3
Taoyuan 	= 4
Hsinchu 	= 5
Miaoli 		= 6
Taichung 	= 7
Changhua 	= 8
Yunlin 		= 9
Chiayi 		= 10
Tainan 		= 11
Zuouing 	= 12
```
#### date
The date format should be `yyyy/mm/dd` like `2023/01/01`

#### time
The time needs to have `A(AM)` or `P(PM)` appended after the time
for example :  
`9:00 AM` should be `900A`  
`11:30 PM` should be `1130P`  

## Launch py
Open the terminal, navigate to your project directory, and execute the following command
```
python main.py
```

## References
https://github.com/maxmilian/thsrc_captcha  
https://irs.thsrc.com.tw/IMINT/
