# Prediction_Thin_Sections_Perm_Por

## Objective
The objective for this particular Data Science Project 3 is to generate a representative thin section from the client’s input of Porosity and Permeability using the Core Analysis and Petrographic data as our training set. We have written our own Python script for the Machine Learning (ML) that are available on GitHub.  

In this project we are using a form of Map Inversion to generate the representative thin section images based on the core reference data and the location of these data in poro-perm space. We are using the Core Porosity vs. Core Permeability Cross Plot as our roadmap for this map inversion process. We use the inverse distance of the client’s input of Porosity and Permeability vs. the reference core-based Porosity and Permeability to determine the most likely and representative thin section from the available calibration data. 

The figure below shows the traditional Porosity vs. Permeability Cross Plot on the left with most of the available Thin Sections on the right over the same Cross Plot.  

<img src="https://github.com/Preston5789/Prediction_Thin_Sections_Perm_Por/blob/master/Readme_imgs/Pic1.png" width="500" height="400">

From a view of most of the Thin Section images above, the Core Analysis database for this well appears to be reasonable representing most/many of the Rock Types that we might expect from our subject well.  What is particularly appreciated is that there are a large number of corresponding thin sections for most core analysis samples. Even though the thin sections are relatively qualitative, they do provide for a visualization as to the texture of the rock.  From the above figure it is apparent from an examination of all the thin sections that the rock texture varies across poro-perm space. It appears reasonable that we could generate a representative thin section from a user defined Porosity and Permeability just based on the location of that combination in poro-perm space. For this project we select only the most likely Thin Section from our map inversion process. 

It should be stated that this technique is very formation and field specific. The following examples are based solely on a particular reference core data set. It would not be advisable to use these data on any other fields or reservoir. This technique requires core calibration for each reservoir. 

For all of the examples below, the user is asked to input Porosity and Permeability. The program then uses the inverse distance of the user’s input Porosity and Permeability vs. the core reference Porosity and Permeability to select the most representative Thin Section from all the core sample using the closest core reference sample in poro-perm space. 

## Example 1:

In this first instance we are entering a high Porosity (0.25) and Permeability (400 mD), and the program estimates a Thin Section representing a high quality rock sample as shown below. Our estimate appears very reasonable. 

<img src="https://github.com/Preston5789/Prediction_Thin_Sections_Perm_Por/blob/master/Readme_imgs/Pic2.png" width="500" height="400">
<img src="https://github.com/Preston5789/Prediction_Thin_Sections_Perm_Por/blob/master/Readme_imgs/Pic3.png" width="500" height="400">

## Continuous Image Data

As shown in the image below we can also concatenate all the estimated images from each depth level being studies to create a continuous image along the wellbore. Our continuous porosity used for this estimation is from the CMR Effective Porosity. We could use a core calibrated NMR Permeability for a continuous permeability; however, we have employed our Map Inversion results using the CMR Effective Porosity and Free Fluid to estimate a continuous core calibrated that is being used in this example. 

The first figure below is a Depth plot at scale of 20:1 showing a continuous image of representative Thin Sections for each depth level. The second figure below is a Depth plot at a scale of 240:1. 

Thin Section images are not quantitative estimations, but they do indicate something about the texture of the rock and how that texture changes with depth. Also, the representative thin sections do match what we would expect from the CMR data shown on the same Depth plots. 

<img src="https://github.com/Preston5789/Prediction_Thin_Sections_Perm_Por/blob/master/Readme_imgs/Pic4.png" width="500" height="400">
## Authors

* **Preston Phillips** - *Initial work* - [Preston5789](https://github.com/Preston5789)
