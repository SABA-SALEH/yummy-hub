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

- As a user, I want to search for recipes based on keywords, so I can easily find recipes that match my preferences.

- As a user, I want to rate recipes and add comments, so I can share my feedback and experiences with other users.

- As a user, I want to view statistics and insights about my recipe usage, so I can track my activity and engagement on the platform.

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

- Users can search for recipes using keywords, which returns relevant results matching the search query.
- Search results are displayed in a user-friendly format, allowing users to quickly find recipes of interest.

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