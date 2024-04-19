# Yummy Hub Recipe Manager

Welcome to Yummy Hub Recipe Manager! This is a web application designed to help you organize and discover delicious recipes from around the world.

## Table of Contents
1. [Introduction](#introduction)
2. [UX and UI](#ux-and-ui)
3. [Features](#features)
4. [Future Features](#future-features)
5. [Information Structure](#information-structure)
6. [Presentation](#presentation)
7. [Look and Feel](#look-and-feel)
8. [Technologies Used](#technologies-used)


## Introduction
Yummy Hub Recipe Manager is a convenient tool for storing, managing, and exploring recipes. Whether you're a cooking enthusiast, a professional chef, or someone looking to try out new dishes, this platform has got you covered.

## UX and UI
### Project and Customer Goals:
- **Project Goal:** Develop a web application named "Yummy Hub Recipe Manager" to help users organize, discover, and share recipes.

- **Customer Goal:** Provide users with a user-friendly platform where they can easily manage their recipe collections, explore new recipes, and engage with other users.

### Business Goal:
The business goal of Yummy Hub Recipe Manager is to attract and retain users by offering a comprehensive and intuitive recipe management solution. By providing valuable features such as recipe management, categorization, search functionality, user accounts, recipe sharing, rate recipe and a responsive design, the platform aims to enhance user satisfaction and engagement.

### User Stories:
- As a user, I want to register an account, so I can save my favorite recipes and interact with the community.

- As a user, I want to add, edit, and delete recipes, so I can manage my recipe collection according to my preferences.

- As a user, I want to search for recipes using keywords and advanced search criteria, such as category, ingredients, and cooking time, enabling me to quickly discover recipes that align with my preferences.

- As a user, I want to rate recipes and add comments, so I can share my feedback and experiences with other users.

- As a user, I want to view statistics and insights about my recipe usage, so I can track my activity and engagement on the platform.

-  As a user, I want to print recipes so I can easily refer to them while cooking.

### Features

**User Authentication:**

- Users can register accounts with unique usernames and email addresses.
- Existing users can log in securely using their credentials.
- Sessions are managed to keep users authenticated across different pages.

**Recipe Management:**

- Users can add new recipes with titles, descriptions, instructions, images, preparation time, and cooking time.
- Recipes can be edited or deleted by the user who created them.
- Ingredients can be added to recipes, including names and quantities.

**Recipe Viewing and Browsing:**

- Recipes are displayed on the home page for users to browse.
- Users can view detailed information about each recipe, including ingredients, instructions, and images.
- Recipes can be categorized into predefined categories for easier browsing.

**Search Functionality:**

- Users can search for recipes using keywords and advanced search criteria, such as category, ingredients, and cooking time, enabling them to quickly discover recipes that match their preferences.
- Search results are displayed in a user-friendly format, allowing users to easily navigate through the list of relevant recipes and find those of interest.

**User Interaction:**

- Users can rate recipes to provide feedback on their experiences.
- Comments can be added to recipes, allowing users to share tips, modifications, and reviews.
- Comments are associated with user accounts and displayed alongside recipes.

**User Dashboard:**

- Users have access to a personalized dashboard where they can view statistics and insights about their recipe usage.
- Statistics may include total recipes, total comments, average rating, most commented recipe, etc.

**User Profile:**

- Users can view and edit their profile information, including username and email address.
- Profile information is stored securely and can be updated as needed.


**Print Recipe Functionality:**

- Users can print recipes directly from the web application, allowing them to access recipes offline or share them with others.
- Printed recipes are formatted in a user-friendly layout, ensuring clear and concise presentation of ingredients, instructions, and other details.
- This functionality provides users with the flexibility to conveniently reference recipes without requiring access to the online platform.

**Session Management:**

- Sessions are managed securely to ensure user data privacy and prevent unauthorized access.
- Users are redirected to appropriate pages based on their authentication status and actions performed.

**Error Handling:**

- Error handling is implemented to provide users with clear and informative error messages in case of invalid inputs or other issues.
- Flash messages are used to display notifications, such as successful actions or errors, to users.

**Responsive Design:**

- The web application is designed with a responsive layout, ensuring optimal viewing and interaction experiences across various devices and screen sizes.

These features collectively contribute to the functionality and usability of the Yummy Hub Recipe Manager web application, providing users with a seamless experience for managing, exploring, and sharing recipes.

### Future Features:
- **Social Sharing:** Integrate social media sharing functionality to allow users to share their favorite recipes with their friends and followers.

- **Recipe Recommendations:** Implement recommendation algorithms to suggest recipes based on user behavior, preferences, and ratings.

- **Advanced Search Filters:** Enhance the search functionality with advanced filters such as dietary restrictions, cooking techniques, and recipe ratings.

- **Collaborative Features:** Introduce collaborative features such as recipe collections, group meal planning, and community forums to foster interaction and collaboration among users.

- **Enhanced User Profiles:** Expand profiles with more details and customization.

- **Notification System:** Alert users about comments, recommendations, and updates.

### Information Structure:
The application is structured around the following key components:

- **Users:** Users can register, log in, and manage their accounts to access personalized features and interact with the platform.

- **Recipes:** Recipes serve as the core content of the application, allowing users to add, edit, delete, rate, and comment on recipes.

- **Categories:** Recipes are organized into categories such as "Around the World," "Quick & Easy," "Healthy Food," and "Sweet Treats" to facilitate browsing and discovery.

- **Comments:** Users can add comments to recipes to share their thoughts, tips, and modifications with other users.

- **Search:** The search functionality enables users to search for recipes based on keywords,to find recipes that match their preferences.

### Presentation:
The application is presented through a web interface with a clean and modern design. Users can navigate through different pages, view recipes, add comments, and interact with various features through intuitive user interfaces and interactive components.

### Look and Feel:
The application features a visually appealing design with a clean layout, modern typography, and vibrant colors. The user interface is designed to be user-friendly and accessible, with clear navigation, intuitive controls, and consistent visual elements throughout the application.

### Technologies Used:
The application is developed using the following technologies and frameworks:

- **Python Flask:** Flask is utilized as the web framework for constructing the backend server and handling HTTP requests.

- **SQLAlchemy:** SQLAlchemy serves as the Object-Relational Mapping (ORM) tool for interacting with the database and managing data models.

- **HTML/CSS:** HTML and CSS are employed for structuring and styling the web pages to create the user interface.

- **JavaScript:** JavaScript is integrated to add interactivity and dynamic behavior to the web pages, including form validation and asynchronous requests.

- **Jinja2:** Jinja2 is the template engine used for generating dynamic HTML content with data from the backend.

- **PostgreSQL** (ElephantSQL): ElephantSQL provides a PostgreSQL database for storing user accounts, recipes, comments, and other application data. It enhances scalability and performance compared to SQLite, facilitating seamless application operation.

- **Heroku:** Heroku is utilized as the deployment platform, enabling easy deployment and scaling of the Flask application. It also hosts the PostgreSQL database add-on provided by ElephantSQL, ensuring robustness and reliability of the application's data storage.

### Wireframe
My initial ideas, after conducting research, were sketched out using Balsamiq. This method proved effective as it allowed me to gather my thoughts and assess which ideas worked best. However, during the project's completion, I found myself not entirely satisfied with my initial proposals and opted for different ideas. Nonetheless, the overall structure of the wireframes remained consistent and was reflected in the final design.

## Database Structure:
The database consists of the following tables:

### users:

| Column        | Data Type                    | Constraints                  |
|---------------|------------------------------|------------------------------|
| id            | Integer                      | Primary Key, Autoincrement   |
| username      | String(50)                   | Unique, Not Null             |
| email         | String(100)                  | Unique, Not Null             |
| password      | String(100)                  | Not Null                     |
| created_at    | Timestamp                    | Default: Current Timestamp   |

### recipes:

| Column             | Data Type                    | Constraints                                          |
|--------------------|------------------------------|------------------------------------------------------|
| id                 | Integer                      | Primary Key                                          |
| title              | String(100)                  | Not Null                                             |
| description        | Text                         |                                                      |
| instructions       | Text                         |                                                      |
| user_id            | Integer                      | Foreign Key to users.id                              |
| category_name      | String(50)                   |                                                      |
| image_url          | String(255)                  |                                                      |
| preparation_time   | Integer                      |                                                      |
| cook_time          | Integer                      |                                                      |
| created_at         | Timestamp                    | Default: Current Timestamp                           |
| ingredients        | JSON                         |                                                      |
| unique_identifier  | String(36)                   | Unique, Not Null, Default: UUID                      |

### ratings:

| Column      | Data Type                    | Constraints                                          |
|-------------|------------------------------|------------------------------------------------------|
| id          | Integer                      | Primary Key                                          |
| rating      | Integer                      |                                                      |
| user_id     | Integer                      | Foreign Key to users.id                              |
| recipe_id   | Integer                      | Foreign Key to recipes.id                            |
| created_at  | Timestamp                    | Default: Current Timestamp                           |

### comments:

| Column      | Data Type                    | Constraints                                          |
|-------------|------------------------------|------------------------------------------------------|
| id          | Integer                      | Primary Key                                          |
| content     | Text                         | Not Null                                             |
| created_at  | Timestamp                    | Default: Current Timestamp                           |
| user_id     | Integer                      | Foreign Key to users.id                              |
| recipe_id   | Integer                      | Foreign Key to recipes.id                            |
| name        | String(100)                  |                                                      |
| email       | String(255)                  |                                                      |


## Getting Started

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation
1. Clone the repository to local machine:
   ```sh
   git clone https://github.com/SABA-SALEH/yummy-hub.git
   ```

2. Navigate to the project directory:
   ```sh
   cd yummy-hub
   ```

3. Install the required dependencies:
    ```sh
   pip install -r requirements.txt
   ```

### Setting Up the Database
1. Create a PostgreSQL database either locally or using a cloud service like ElephantSQL.
2. Update the database connection URI in the __init__.py file:
SQLALCHEMY_DATABASE_URI = 'postgresql://'

### Running the Application
1. Start the Flask development server:
   ```sh
   python run.py
2. Open a web browser and navigate to http://localhost:5000 to access the application.

## Deployment

To deploy Yummy Hub Recipe Manager web application to Heroku, follow these steps:

1. Sign up for Heroku:

    - Navigate to Heroku.com in web browser.
    - Click on "Sign Up" and create a new account.
    - Fill out the registration form with  details and verify the account through the confirmation 
    email sent by Heroku.

2. Create a new app on Heroku:

    - Once logged in, click on the "New" button on the dashboard.
    - Choose a unique name for app (e.g., yummy-hub).
    - Select region preference.
    - Click on "Create App" to create app on Heroku.

3. Link  local Git repository to Heroku:

    - In terminal, navigate to project directory.
    - Add a new remote for Heroku by running the command:
    ```csharp
    git remote add heroku <heroku-git-url>
    ```
    - Verify that the remote has been added by running:
    ```csharp
    git remote -v
    ```

4. Create a requirements.txt file:

    - In terminal, run the command:
    ```csharp
    pip freeze > requirements.txt
    ```
    -This command will generate a requirements.txt file listing all Python dependencies used in project.

5. Create a Procfile:

    - In terminal, run the command:
    ```bash
    echo "web: python run.py" > Procfile
    ```

6. Commit changes and push to Heroku:

    - Add the requirements.txt and Procfile to Git repository:
    ```csharp
    git add requirements.txt Procfile
    ```
    - Commit the changes:
    ```sql
    git commit -m "Add requirements.txt and Procfile"
    ```
    - Push code to Heroku:
    ```perl
    git push -u heroku main
    ```

7. Set up environment variables on Heroku:

    - Go to Heroku dashboard and navigate to app's settings.
    - Click on "Reveal Config Vars".
    - Add any necessary environment variables, such as SECRET_KEY, IP, and PORT, and their respective values.

8. Check logs and troubleshoot if necessary:

    - Monitor the build process and check for any errors by viewing the logs on Heroku.
    - You can access logs through the Heroku dashboard or via the command line using:
    ```css
    heroku logs --tail --app yummy-hub
    ```
9. Test deployed app:

    - Once deployment is successful, visit app's URL provided by Heroku to ensure that it is working as expected.

   (Optional) Set up automatic deployment from GitHub:

    - In Heroku app's dashboard, navigate to the "Deploy" tab.
    - Connect GitHub repository to Heroku app.
    - Enable automatic deployments from chosen branch (e.g., main).

## Testing
### Manual Testing
#### User Authentication:
1.	User Registration:
	- Test registering with unique usernames and email addresses.
    - Ensure successful registration redirects users appropriately.


2.	User Login:
	- Test logging in with valid credentials.
	- Ensure login fails with incorrect credentials.
	- Verify that users are redirected to the appropriate pages after login.

#### Recipe Management:
3.	Adding Recipes:
	- Add new recipes with all required fields.
	- Verify that all recipe details are correctly saved in the database.

4.	Editing Recipes:
	- Edit existing recipes and ensure changes are updated correctly.
	- Test updating recipe details such as ingredients, instructions, and images.

5.	Deleting Recipes:
	- Delete recipes and confirm they are removed from the database.

#### Recipe Viewing and Browsing:
6.	Home Page Display:
	- Check if recipes are displayed on the home page.

7.	Recipe Details:
	- View detailed information about each recipe.
	- Test navigation to individual recipe pages.

8.	Category Browsing:
	- Browse recipes by categories and verify correct filtering.

#### Search Functionality:
9.	Keyword Search:
	- Test searching for recipes using various keywords.
	- Confirm that search results are relevant and accurate.

#### User Interaction:
10.	Rating Recipes:
	- Rate recipes and verify that ratings are saved and displayed correctly.

11.	Adding Comments:
	- Add comments to recipes and ensure they are associated 
    - Test displaying comments alongside recipes.

#### User Dashboard:
12.	Viewing Statistics:
    - Check if users can view statistics and insights about their recipe usage.
	- Verify that statistics such as total recipes, total comments, and average rating are accurate.

13.	User Profile:
	- Edit user profile information such as username and email address.
	- Ensure changes are saved correctly.

14. Change Password:
    - Test changing the password from the user dashboard.
    - Verify that users can update their passwords successfully.
    - Confirm that users receive appropriate feedback messages after changing their passwords.

#### Comments Management:
15. Adding Comments:
    - Add comments to recipes and ensure they are associated correctly.
    - Verify that comments are displayed alongside recipes.

16. Editing Comments:
    - Edit existing comments and ensure changes are updated correctly.
    - Test updating comment content.

17. Deleting Comments:
    - Delete comments and confirm they are removed from the database.
    - Verify that associated recipes are updated accordingly.

#### Error Handling:
18.	Invalid Inputs:
	- Test submitting forms with invalid data and verify appropriate error messages.

19.	Flash Messages:
	- Confirm that flash messages are displayed for successful actions and errors.

#### Responsive Design:
16.	Desktop and Mobile Devices:
	- Test the application on different screen sizes to ensure responsiveness.
	- Verify that all features and functionalities work well on both desktop and mobile devices.

### Automated Testing
#### Code Validation:
1.	HTML Validator:
	- Validate HTML code for all pages to ensure compliance with standards.

2.	CSS Validator:
	- Check stylesheets for compliance with CSS standards and fix any issues.

3.	JS Validator:
	- Validate JavaScript code syntax and maintain code quality.

#### Lighthouse Audit:
1.  Assess performance, accessibility, and best practices using Lighthouse.
2.  Optimize performance and address any identified issues.

### Client Stories Testing
#### Client Story 1:
1. Registration and Account Management:
    - Test user registration process.
	- Verify that users can manage their accounts effectively.

#### Client Story 2:
1. Recipe Management:
	- Test adding, editing, and deleting recipes.
	- Confirm that users can manage their recipe collections efficiently.

#### Client Story 3:
1. Search and Browsing:
	- Test search functionality and category browsing.
	- Ensure users can find recipes easily based on their preferences.

#### Client Story 4:
1. Interaction and Engagement:
	- Test rating recipes and adding comments.
	- Verify that users can interact with recipes and engage with the community.

#### Client Story 5:
1.	Personalization and Insights:
	- Check if users can view statistics and insights about their recipe usage.
	- Ensure personalized experience based on user activity.

#### Client Story 6:
1. Error Handling and User Experience:
	- Test error handling and user feedback mechanisms.
	- Verify that users receive clear and informative messages.

### Compatibility and Responsive Testing
#### Browser Testing:
1.	Google Chrome:
	- Test the application thoroughly on Google Chrome to ensure compatibility and functionality.

2.	Mozilla Firefox:
	- Verify compatibility and functionality on Mozilla Firefox.

3.	Microsoft Edge:
	- Test on Microsoft Edge to ensure seamless user experience.
    
#### Mobile Testing:
1.	iPhone and Android Devices:
	- Test the application on various mobile devices to ensure compatibility and responsiveness.
	- Verify that all features work well on mobile browsers such as Chrome and Safari.


       

















