# ELCON- Smart Energy Conservation
![Logo](https://github.com/apurbashakya/SmartGrid/blob/main/SmartGrid/smart-grid/src/img/logodark.jpeg)

We aim to use **predictive analytics** to output expected electricity usage and with the help of **smart home integration**, the resources using maximum amount of energy, which helps in saving a lot of electricity and power consumption. 


## Screenshots

![Logo](https://github.com/apurbashakya/SmartGrid/blob/main/SmartGrid/smart-grid/src/img/pre1.png)




## Description

We’ll develop a **real-time automatic notification alert web based system**  for saving electricity.Along with a daily, monthly and yearly analysis of data about electricity usage. We aim to use predictive analytics to output expected electricity usage and with the help of smart home integration, the resources using maximum amount of energy. This system can also interpret whether the house is empty with the number of mobile devices connected to the home wifi and accordingly minimize the use of non essential appliances.The adaption is supported by **enabling regional languages over standardized english** to increase adoption and using pictorial representation for easier understanding of collected data. The flagship feature enables electricity cost estimation for the current cycle and **minimizing phantom electricity** use, **saving costs by around 6 %.**

Steps involved:
*Cleaning : 
  Datetime index created after converting the data to a day-by-day conigeration.
  Homogenized the features for minimizing bias between features.
  Filled missing entries that may have been caused due to transmission or storage losses or due to error in sensors by filling with data from T-1 day.
  Created an extra feature called sub-metering that processes left out energy usage as a separate category.
Train/test split: 
  Split the data into a 3+1 configuration after a split into standard weeks.
  Applied walk-forward algorithm for validation where each new week predicted is inculcated into the data for prediction of next week and so on and on.
 Pipelined normalization: 
  Created a standardized pipeline including normalization, standardization and modelling over different ML models for convenient and efficient operation.
Training: 
  Used various different models included in but not limited to scikit-learn using the standardized pipeline to access the models based on their RSME score.
 Selecting a model: 
    SGD model produced the lowest error with additional benefits including:
    Reduced redundancy arising from retraining model.
    Maximum/Minimum segmentation for iterations
Hyperparameter tuning: 
  For the final model selected, the hyper-parameters were further enhanced on the detailed dataset acquired to provide hyper-localized results for the required         purpose.


## Tech Stack

**Frontend:** HTML, CSS, JavaScript, React-Bootstrap

**Backend:** Python, Node, Scikit-learn


## Installation
To Run this project on your local system clone the main directory

```bash
  git clone https://github.com/apurbashakya/SmartGrid.git
```

change directory to the smart-grid
```bash
  cd SmartGrid/SmartGrid/smart-grid
```

Install my-project with npm

```bash
  npm install
```
    
## Deployment

Run npm start command

```bash
  npm start
```


## Features

-  Automatic notification alert to reduce wastage of power
- Expected electricity usage using smart home integration
- Special regional languages support 
-  Minimizing phantom electricity use and saving costs by around 6 %


## Roadmap

- Additional browser support

- Add home integrations
- Further optimizing machine learning model


## 🚀 About us
- Jaskaran singh jaggi



## 🔗 Links
- Jaskaran Singh Jaggi

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jaskaran-s-a137aa104/)
[![twitter](https://img.shields.io/badge/twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/in/jaskaran-s-a137aa104)




## Support

For support, join our discord channel or reddit page.

- [@Discord](https://discord.gg/ZuF9Q9Kb)
- [@Reddit](https://reddit.com/elcon_energy)
