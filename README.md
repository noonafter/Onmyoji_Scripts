# Onmyoji_Scripts
 
The initial purpose of the project is to learn pywin32 packages. The project plays Onmyoji（阴阳师） automatically by pywin32 of python on Windows platform. With the help of the scripts, you can liberate yourself from the endless loop of brushing instance zones and other meaningless labor. All the scripts are for communication only, not for commercial use!
 
## Getting Started
 
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.
 
### Prerequisites
 
What things you need to install the software and how to install them
 
```
Python 3.8.x
Pywin32
Pyautogui
```
 
### Installing
 
```
pip install -r requirements.text
```
## Instruction

### Yuhun instance zones
To brush "hun10/11" instance zones as a member of others' team, run hun11_single.py on the team stage. Or to limit the PVE process within certain seconds, run hun11_single_125.py file(1000 strength or 125 rounds by default). 

With the help of v5cxdkq.zip, multi-clients can be open at the same time. If you want brush "hun10/11" instance zones on your own two accounts(one as captain, the other as member), you ought to run the hun11_two.py file. Similarily, PVE within a certain period, hun11_two_30.py(30 rounds for daily tasks by default)

Before run all the scripts, you should edit the "time_round" term at config.ini to your own time of one hun10/11 round. Other parameters can also be edited to your preference. However, check weather you understand the meaning of it before you make a change.

When you run the script, perhaps, some of the window title will change into "不可最小化&右下角不能遮挡", because getpixel function can not get the color of a hidden or minimized window.(Although there is [solution for the problem](https://www.xszz.org/faq-1/question-201808315704.html) online of C++ version, I am of no capbility to access the python version. Welcome to contact me, if you get the solution of python version)
 
## A few notes：
 
The scripts works well on the resolution of 1920x1080. If your screen is of different resolution, you might need to change some color points of certain scripts.
 
 
## Contributing
 
Any issue or bug feedback is welcomed.For such issues, please email lichuan0987@qq.com - note that you must read the instructions carefully first. More functions will be added to the project, like auto-pumping cards and feed N dog-food. Please contact me if you have more ideas about the improvement or suggestion.
 
## Versioning
 
We use [Github](https://github.com/) for versioning. 
 
## Authors
 
* **noonafter** - *Initial work* - [noonafter](https://github.com/noonafter)
 
 
## License
 
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
 
## Acknowledgments
 
* Hat tip to anyone whose code was used
* Inspiration

