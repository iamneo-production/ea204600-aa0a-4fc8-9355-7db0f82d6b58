
### Telangana Academic Grand Challenge on Climate Change
This repository is for the project for the Academic Grand Challenge on Climate Change Hackathon conducted by Nasscom in Collaboration with the Telangana Government and Capgemini
## Table of Contents
- [Getting Started](#getting-started)
- [Problem Statment](#problem-statement)
- [About the Problem](#about-the-problem)
- [Our Understanding](#our-understanding)
- [Prototype](#prototype)
    - [AQI Prediction](#aqi-prediction)
    - [Heatwave Prediction](#heatwave-prediction)
    - [Mobile Application](#mobile-application)
- [Flow Diagram](#flow-diagram)
- [Submissions](#submissions)
- [Authors](#authors)

## Problem Statement
 - Building an AI/ML model that predicts the occurrences of heat waves and the Air Quality Index (AQI) for Adilabad, Nizamabad, Warangal, Karimnagar, and Khammam.

## About the Problem
- The goal of the challenge is to predict heatwave occurrence and AQI trends in tier 2 cities of Telangana. 
- The data provided includes Weather, AQI, Energy Consumption and Vehicle sales in various cities of the state on a monthly basis.

## Our Understanding
- We aim to solve this problem by dividing it into 2 parts:
  - Regression:  the variables like the AQI, Energy Consumption, etc, are continuous in nature, so we could build a possible estimate to these values, based on a linear
  combination of the input variables. With this, we plan to estimate the AQI, temperature and other parameters.
  - Classification: with the AQI, temperature and the other parameters predicted, we create a classifier to categorize whether given a set of weather parameters, contribute a heatwave or not. This model also takes into consideration, a parameter tolerance (), which can be set/used by the users/governing bodies to set the threshold, for determining if the weather parameters is a heatwave or not.

## Prototype
 - It is divided into three modules

   - AQI Prediction
   - Heatwave Prediction
   - Mobile Application

https://sonarcloud.io/summary/overall?id=examly-test_ea204600-aa0a-4fc8-9355-7db0f82d6b58
