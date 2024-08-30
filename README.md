
# Mildew Detection Project

## Live Link - https://mildewdetectionhg-d519acc0f8b3.herokuapp.com/

## Dataset Content

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
- The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## Business Requirements

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Hypothesis and how to validate?

- As the leaves of cherry trees can be manually differentiated by the visible presence of powdery mildew, it is believed that a classification machine learning model can expedite this process by instantly discerning if mildew is present on a leaf. This would be achieved through an average image study, with the accuracy of the model informing the validity of the hypothesis. 

## The rationale to map the business requirements to the Data Visualisations and ML tasks

### Business Requirement 1: Data Visualisation
- Display the mean and standard deviation images for mildew-infected and uninfected cherry leaves.
- Display the difference between average mildew-infected and uninfected leaves.
- Display an image montage for either mildew-infected or uninfected leaves.
### Business Requirement 2: Classification and Prediction
- Build an ML model and use it to perform predictions based on whether leaves are infected or not, with an accuracy rating of at least 97%.

## ML Business Case

- We are seeking to create a supervised, 2-class image classification model in order to achieve the above tasks.
- The goal of this will be to allow the client to quickly and accurtely differentiate healthy and non-healthy cherry leaves. It has been agreed with the client that the model must have an accuracy rating of at least 97%.
- An API dashboard will be needed to display the results and outputs of the model.
- The benefits of a successfull prediction model will be that the client is able to more reliably supply a quality product. The client will also be able to use the model as a basis for potentially carrying out similar classification tasks with other crops.
- The data was provided by the client under an NDA (non-disclosure agreement), therefore the data should not be share with those not officially involved in the project. There are no additional ethical concerns surrounding the data used.

## Dashboard Design

### Page 1 - G


- List all dashboard pages and their content, either blocks of information or widgets, like buttons, checkboxes, images, or any other items, that your dashboard library supports.
- Finally, during the project development, you may revisit your dashboard plan to update a given feature (for example, at the beginning of the project, you were confident you would use a given plot to display an insight, but later, you chose another plot type).

## Unfixed Bugs

- No unfixed bugs were detected 

## Deployment

### Heroku

- The App live link is: `https://mildewdetectionhg-d519acc0f8b3.herokuapp.com/`
- Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
- The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.

Additional steps for using heroku-20 stack(needed to support python 3.8.18):
1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Go to heroku, manage account, applications -> create authorisation
5. Enter the following into your IDE and use your authorisation code for the password: **heroku login -i** 
6. Enter the following into your IDE: **curl https://cli-assets.heroku.com/install.sh | sh**
7. Initialise with git in your IDE: **git init**
8. Enter the following into your IDE to confirm your app is there: **heroku apps**
9. Add your app remotely: **heroku git:remote -a your_app_name**
10. Set stack to heroku-20: **heroku stack:set heroku-20**
11. 4. Select the branch you want to deploy, then click Deploy Branch.

N/B - If the slug size is too large, then add large files not required for the app to the .slugignore file.

## Credits

- Using base64 to convert images in prediction dashboard page - Streamlit forum - https://discuss.streamlit.io/t/cannot-display-imagecolumns-with-streamlit/50957/2

### CodeInstitute 
- Repo template and raw image data from Handbook: Mildew Detection in Cherry Leaves
- Data cleaning and set splitting code from the 'data collection' and 'data preperation' sections of the malaria detection walkthrough project
- Code for displaying graph of number of images in sets from the 'image augmentation' section of the malaria detection walkthrough project
- Code for ML performance dashboard page repurposed from ML performance page from the malaria detection walkthrough project
  
### Data
- Data taken from the Code Institute Kaggle cherry leaves database - https://www.kaggle.com/codeinstitute/cherry-leaves

### Favicon
- Deciduous tree - Emojis By Twitter's Twemoji, Licensed Under CC-BY 4.0
