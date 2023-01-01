# SlidExt
 
A Command Line tool to generate a presentation from tutorial videos where the instructor uses slides to explain the topic.
___
## Pre-requisites
1. Python 3.6 or above

## Installation
```bash
git clone https://github.com/suvanbalu/slidext.git
cd slidext
pip install -r requirements.txt
```
## Usage
```bash
python slidext.py <Sub Modules> <Arguments>
```

## Arguments
1. **Sub Module** - Video Downloader
```bash
python slidext.py vd <Arguments>
```
| Argument | Description | Default |
| --- | --- | --- |
| -l,--link | Link of the video | None |
| -s,--save | Path of Output Directory | Current Directory |
  
  
2. **Sub Module** - Slide Extractor
```bash
python slidext.py se <Arguments>
```
| Argument | Description | Default |
| --- | --- | --- |
| -o,--open | Path of Video | None |
| -f,--file | File of links | None |
| -l,--link | Link(s) of video | None |
| -s,--save | Destination Path of the extracted images  | None |
| -t | Set threshold | 520000 |
| -ti | Time interval of frames in second | 2 |
| -nc | No Carousel | 1 |
| -pt | Print Thresholds | 0 | 


3. **Sub Module** - PDF converter
```bash
python slidext.py pdf <Arguments>
```
| Argument | Description | Default |
| --- | --- | --- |
| -fo,--folder | Path of folder | None |
| -o,--open | Path of Video | None |
| -f,--file | File of links | None |
| -l,--link | Link(s) of video | None |
| -s,--save | Destination Path of the extracted images  | None |
| -n,--name | Name of folder | None |


4. **Sub Module** - PPT converter
```bash
python slidext.py ppt <Arguments>
```
| Argument | Description | Default |
| --- | --- | --- |
| -fo,--folder | Path of folder | None |
| -o,--open | Path of Video | None |
| -f,--file | File of links | None |
| -l,--link | Link(s) of video | None |
| -s,--save | Destination Path of the extracted images  | None |
| -n,--name | Name of folder | None |
| -res | Set resolution | 300 |
| -start | Starting page of ppt | 0 |
| -count | Page count | None |
| -quiet | Dont display progress bar | True |


5. **Sub Module** - CAROUSEL to PDF converter
```bash
python slidext.py car <Arguments>
```
| Argument | Description | Default |
| --- | --- | --- |
| -fo,--folder | Path of folder | None |
| -o,--open | Path of Video | None |
| -f,--file | File of links | None |
| -l,--link | Link(s) of video | None |
| -s,--save | Destination Path of the extracted images  | None |
| -n,--name | Name of folder | None |


## Team Members
| Name | Email | Social |
| --- | --- | --- |
| Suvan Sathyendira B | suvanbalu@gmail.com | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/suvanbalu) [![](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/suvanbalu/)
| Ashwin V | ashwinvelu2003@gmail.com | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/asxwin) [![](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ashwin-v-108068219/)
| Nashita V | nv.nashita@gmail.com | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/NashitaV) [![](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nashita-v-972563219/)
| Shivani Sri S | shivanii.srii@gmail.com | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/shxvani) [![](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shivani-s-b640241b2/)
| Nishanth G Palanisamy | nishanthmail | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/nishanth-g-palanisamy) [![](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/nishanth-g-palanisamy-430933206/)
| Sivesh Kannan | siveshkannan8@gmail.com | [![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)](https://github.com/siveshk) [![](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sivesh-kannan-455811252/)
