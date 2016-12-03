# health-project
IPPP Final Project

We decide to focus our project on infant mortality around the world. Our question was how big is the gap between developed and undeveloped regions when they fight against particular diseases that attack children. 

For this purpose the webpage http://www.healthdata.org/ collects a lot of data that could give us insights on the question that we want to answer. Healthdata.org is a webpage owned by the Institute for Health Metrics and Evaluation (IHME). The IHME is an independent global health research center based at the University of Washington. 

The IHME has built a data visualization website where the user can interact with variables by country/region, age group, year (1990-2015), and disease. Their visualization includes geographic maps and charts like treemaps and heat maps that help the user to understand the information in an easier way. After looking at the IHME website our goal was to create a similar webpage where the user could interact.

The website allows the user to download data manually or using APIs. Since we wanted to download csv for different regions (according to the World Bank classification), using APIs would be helpful to save us time. We use json codes (see health1.py file) but they were ineffective because they downloaded different datasets from the ones that we wanted. Since we could not manage to use the APIs code in an efficient way we had to download the csv manually. 

Once we had downloaded the data, we thought about a plotting a bars graph that showed the level of mortality of each disease by region. The code for the graph can be seen in the jupyter file (plot infant mortality diseases).

The next step was to create an attractive and friendly website. In order to do it, we downloaded djangos and created a new project there. We achieved to upload our project to the local server. Afterwards, we started to create the design of the webpage. Our webpage has three different htmls: webhealth, Measurements and Other studies. 

In webhealth (home) we include Our mission and the top 5 causes of the death worldwide. We also include buttons with which we attempt to create tables and plots on the fly. Our atom files contain the views, urls, models, and form for the table; however, we did not achieve to visualize it in our webpage. 

The plots that we intended to include in our page can be seen in the Jupyter file. By playing with the different diseases, we can observe how in underdeveloped regions, diseases like diarrhea still represent a serious threat for infant mortality. We hope that policy makers and people that work on international development can use these data as insights to improve health services in underserved regions of the world. 

++ How to run it ++
The files used to visualize the webpage require django. All the modules that have to be imported are specified in the atom files. The jupyter file requires also the data.csv file in order to show the graphs. 


