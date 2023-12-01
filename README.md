# Market-Basket-Analysis

# 1. Introduction
---
### Overview
---
Market basket analysis is a data mining method that enables retailers or shopping stores to improve their sales by understanding their customers' transaction patterns. All the customers’ daily transaction histories are recorded to create the dataset which is critically analysed to reveal product grouping and products that a likely to be bought together in one transaction. By identifying which products tend to be bought together, the company can make informed decisions to improve sales and customer satisfaction. For more information see [here](https://www.techtarget.com/searchcustomerexperience/definition/market-basket-analysis).



## 1.1 About the Dataset
---

The Market basket dataset contains over 38,000 transactions made by customers shopping for groceries. The dataset timeline spans between 2014 and 2015. Below is a brief description of the dataset features: 

> Member_number:  Integer, contains the customers’ ID or number

> Date: Object, recorded date of each transaction

> ItemDescription: Object, the product purchased by the customer.




   ## 1.2 Methodology
   ---
   ### (a) Objective of the Project
 The goal of this work is to perform market basket analysis to uncover patterns in customer purchasing behavior. To achieve this goal, we commenced with the following objectives:
      
   **(1.) Explore the dataset to understand some preliminary patterns such as:**
   
           (a) Mostly purchased items
           (b) Monthly and yearly sales pattern
         
   **(2.) Perform market basket analysis to uncover products that a likely bought together.** 
   
   **(3) Make recommendations based on our results.**

   
   ### (b) Method and Approach
   
We begin by performing the wrangling process on the dataset to familiarize and clean up the dataset. Next, we carried out the exploratory data analysis and highlighted some useful insights from the data. We further carried out data processing to prepare the data for the market basket analysis. We performed the market basket analysis and visualized our results.
   
   
   ### (c) Tools used
     (i) We used the TransactionEncoder to transform the dataset into a form understandable to the apriori algorithm.
    (ii) Next, we used the Apriori algorithm to identify frequent items in the dataset which was then used to implement the association rule. We chose the Apriori algorithm because of its simplicity, ease of
    implementation, and interpretability. 
    
    (iii) We created our rule table by implementing association. 
    
    (iii) We visualized the results obtained to gain insights and make recommendations
     
    

   ## 1.3 Key insights
   ---
   > 1. In our exploration, the most frequently bought item was `whole milk` followed by `vegetables `and `buns`. The highest sales by the company happened in August 2015. We also noticed that the company made more transactions in 2015 compared to 2014.

 
 > 2. Our market basket analysis showed that `yogurt`, `whole milk`, and `sausage` are most likely to be bought together.





