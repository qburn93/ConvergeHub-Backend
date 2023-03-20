# ConvergeHub-Backend

## Deployment

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on
our GitHub account to view and/or make changes without affecting the original
repository by using the following steps...

1. Log in to GitHub and locate the [GitHub
   Repository](https://github.com/qburn93/converhub-backend)
1. At the top of the Repository (not top of page) just above the "Settings"
   Button on the menu, locate the "Fork" Button.
1. Click the button (not the number to the right) and you should now have a copy
   of the original repository in your GitHub account.

### Making a Local Clone

**NOTE**: It is a requirement of the project that you have Python version 3.8 or higher installed locally.

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/qburn93/converhub-backend).
1. Under the repository name, click "Code".
1. To clone the repository using HTTPS, under "HTTPS", copy the link.
1. Open your local terminal with git installed
1. Change the current working directory to the location where you want the cloned directory to be created.
1. Type `git clone`, and then paste the URL you copied in Step 3.

    ```console
    ~$ git clone https://github.com/qburn93/converhub-backend.git
    ```

1. Press Enter. Your local clone will be created.

    ```console
    $ git clone https://github.com/qburn93/converhub-backend.git
    > Cloning into `test-dir`...
    > remote: Counting objects: 10, done.
    > remote: Compressing objects: 100% (8/8), done.
    > remove: Total 10 (delta 1), reused 10 (delta 1)
    > Unpacking objects: 100% (10/10), done.
    ```

    [Click here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) for a more detailed explanation of the process above with pictures.

1. Change the current working directory to the cloned project folder (this will be a child directory in the location you cloned the project).

1. It is recommended to use a virtual environment during development ([learn more about virtual environments](https://realpython.com/python-virtual-environments-a-primer/)). If you would prefer not to use one please skip the following steps:
    1. Create a virtual environment in the projects working directory by entering the following command in the same terminal window used for the steps above `python3 -m venv .venv`.
    1. Before use, the virtual environment will need to be activated using the command `source .venv/bin/activate` in the same terminal window used previously.
1. Packages required by the project can now using the command `pip install -r requirements.txt`
1. In the cloned directory, rename the file `.env-example` to `.env` and populate it with the information required.
1. Make Django migrations using the command `./manage.py migrate`.

### Deploying with Heroku

**NOTE**: It is a prerequisite of deployment to Heroku that you already have access to the following:

- A Cloudinary account, create one for free at [https://cloudinary.com](https://cloudinary.com).

**NOTE**: It is assumed you have followed all deployment instructions listed in this readme starting with the section titled 'Forking the GitHub Repository'.

1. Log in to [Heroku](https://www.heroku.com/) and if not taken there automatically, navigate to your personal app dashboard.
1. At the top of the page locate the 'New' drop down, click it and then select 'Create new app'.
1. Give your application a unique name, select a region appropriate to your location and click the 'Create app' button.
1. Your app should now be created, so from the menu towards the top of the page select the 'Resources' section.
1. Search for 'Heroku Postgres' under the Add-ons section and add it.
1. From the menu towards the top of the page select the 'Settings' section and lick 'Reveal Config Vars' in the Config vars section. Enter the following key / value pairings:
    1. Key as `ALLOWED_HOSTS` and the value as the name of you project with '.herokuapp.com' appended to the end e.g.  `example-app.herokuapp.com`. Click the Add button.
    1. Key as `CLOUDINARY_URL` and the value as your cloudinary API Environment variable e.g. `cloudinary://**************:**************@*********`. Click the Add button.
    1. Key as `SECRET_KEY` and the value as a complex string which will be used to provide cryptographic signing. The use of a secret key generator is recommended such as [https://djecrety.ir](https://djecrety.ir/). Click the Add button.
    1. Ensure the key `DATABASE_URL` is already populated. This should have been created automatically by Heroku.
    1. The `DATABASE_URL` should be copied into your local `.env`, created during the cloning process.
    1. To make authenticated requests to this API (e.g. from a fontend application) you are required to add the key `CLIENT_ORIGIN` with the value set as the URL you will be sending the authentication request from.
    1. Additionally, a `CLIENT_ORIGIN_DEV` key can be set with the value of a development server (IP or URL) for use during local development.
1. Open the `.env` file in the project directory and delete the key / value pair `DEV_ENVIRONMENT_DATABASE = True` before saving the file. This can be added back after the next step to ensure local development changes will not alter the remote database.
1. Navigate to the 'Deploy' page using the menu towards the top of the page.
1. Select 'GitHub' from the 'Deployment method' section and you will be prompted to 'Connect to GitHub'.
1. Once connected to your GitHub account you will be able to search for your repository which contains the forked 'convergehub-backend' repository.
1. Once the repository is found click 'Connect'.
1. At the bottom of the page find the section named 'Manual deploy', select the 'main' branch in the drop down and click the 'Deploy' button.
1. Once deployment is complete, click the 'View' button to load the URL of the deployed application.


## Technologies Used

### Languages and Frameworks Used

- Python
- [Django](https://pypi.org/project/Django/3.2.14/) - High-level Python Web framework used to develop the project.
- [djangorestframework](https://pypi.org/project/djangorestframework/3.14.0/) - Toolkit for building web API's with Django.

### Python Modules Used

- Built-in Packages/Modules
  - [math](https://docs.python.org/3/library/math.html) - The trigonometric functions acos, cos and sin and the constant pi from the math module were used in longitude and latitude calculations.
  - [pathlib](https://docs.python.org/3/library/pathlib.html) - Used to work with filepaths.
  - [os](https://docs.python.org/3/library/os.html) - This module provides a portable way of using operating system dependent functionality.

### Packages Used

- External Python Packages
  - [cloudinary](https://pypi.org/project/cloudinary/1.30.0/) - Cloudinary intergration.
  - [django-cloudinary-storage](https://pypi.org/project/django-cloudinary-storage/0.3.0/) - Cloudinary intergration.
  - [dj-database-url](https://pypi.org/project/dj-database-url/0.5.0/) - Allows the use of 'DATABASE_URL' environmental variable in the Django project settings file to connect to a PostgreSQL database.
  - [django-allauth](https://pypi.org/project/django-allauth/0.51.0/) - Set of Django application used for account registration, management and authentication.
  - [dj-rest-auth](https://pypi.org/project/dj-rest-auth/2.2.5/) - API endpoints for handling authentication in Django Rest Framework.
  - [django-filter](https://pypi.org/project/django-filter/22.1/) - Application that allows dynamic QuerySet filtering from URL parameters.
  - [djangorestframework-simplejwt](https://pypi.org/project/djangorestframework-simplejwt/5.2.1/) - JSON Web Token authentication backend for the Django REST Framework.
  - [django-cors-headers](https://pypi.org/project/django-cors-headers/3.13.0/) - Django App that adds CORS headers to responses.
  - [gunicorn](https://pypi.org/project/gunicorn/20.1.0/) - Python WSGI HTTP Server.
  - [Pillow](https://pypi.org/project/Pillow/9.2.0/) - Fork of PIL, the Python Imaging Library which provides image processing capabilities.
  - [psycopg2](https://pypi.org/project/psycopg2/2.9.3/) - Python PostgreSQL database adapter.
  - [python-dotenv](https://pypi.org/project/python-dotenv/0.21.0/) - Set key-value pairs from `.env` file as environmental variables.

## Testing
### Track Manual testing of the api


| Feature                | Action                                                            | Expected Result                                  | Actual Result   |
|------------------------|-------------------------------------------------------------------|--------------------------------------------------|-----------------|
| List Posts             | Perform GET request to /api/posts/                                | Retrieve a list of all posts                     | Pass               |
| Create Post            | Perform POST request to /api/posts/ with title and content       | Create a new post and return the created post    | Pass               |
| Retrieve Post          | Perform GET request to /api/posts/:id/                            | Retrieve a specific post by its ID                | Pass               |
| Update Post            | Perform PUT request to /api/posts/:id/ with updated data          | Update a specific post by its ID                  | Pass               |
| Delete Post            | Perform DELETE request to /api/posts/:id/                         | Delete a specific post by its ID                  | Pass               |
| List Profiles          | Perform GET request to /api/profiles/                             | Retrieve a list of all user profiles              | Pass               |
| Retrieve Profile       | Perform GET request to /api/profiles/:id/                         | Retrieve a specific profile by its ID             | Pass               |
| Update Profile         | Perform PUT request to /api/profiles/:id/ with updated data       | Update a specific profile by its ID               | Pass               |
| List Comments          | Perform GET request to /api/comments/                             | List all comments                                 | Pass               |
| Create Comment         | Perform POST request to /api/comments/ with content and post ID   | Create a new comment and return the created comment | Pass             |
| Retrieve Comment       | Perform GET request to /api/comments/:id/                         | Retrieve a specific comment by its ID             | Pass               |
| Update Comment         | Perform PUT request to /api/comments/:id/ with updated data       | Update a specific comment by its ID               | Pass               |
| Delete Comment         | Perform DELETE request to /api/comments/:id/                      | Delete a specific comment by its ID               | Pass               |

<br>

# Detailed class  and api explanation bellow
<details>

# Models

## The Post class is a Django model representing a post in the application. It has the following fields:

## Post
- owner: ForeignKey relation to the User model (author of the post).
- created_at: DateTime field indicating when the post was created.
- updated_at: DateTime field indicating the last time the post was updated.
- title: CharField for the post's title.
- content: TextField for the post's content (optional).
- image: ImageField for the post's image (optional).
- image_filter: CharField for the image filter to be applied (default is 'normal').

## Profile
- owner: OneToOneField relation to the User model.
- created_at: DateTime field indicating when the profile was created.
- updated_at: DateTime field indicating the last time the profile was updated.
- name: CharField for the user's display name (optional).
- content: TextField for the user's profile content (optional).
- image: ImageField for the user's profile image.

## Comment
- owner: ForeignKey relation to the User model (author of the comment).
- post: ForeignKey relation to the Post model (the post the comment is related to).
- created_at: DateTime field indicating when the comment was created.
- updated_at: DateTime field indicating the last time the comment was updated.
- content: TextField for the comment's content.

## Like
The Like model represents a like on a post. It has the following fields:

- owner: A foreign key reference to the user who liked the post.
- post: A foreign key reference to the post that has been liked.
- created_at: The timestamp when the like was created.
- updated_at: The timestamp when the like was last updated.
- content: The text content of the like (not required in this case, can be removed).
The Meta class orders the Like model by the created_at timestamp in descending order and ensures that a user can like a post only once.

## Follower
The Follower model represents the relationship between two users where one user follows another user. It has the following fields:

- owner: A foreign key reference to the user who follows another user.
- followed: A foreign key reference to the user who is being followed.
- created_at: The timestamp when the follow action was created.
The Meta class orders the Follower model by the created_at timestamp in descending order and ensures that a user can follow another user only once.

# Serializers
## Post serializer :
#### PostSerializer Class
- Serializes the Post model.
- Includes extra fields: owner (username), is_owner, profile_id, and profile_image.
- Validates image size, height, and width.

## Profile serializer :
#### ProfileSerializer Class
- Serializes the Profile model.
- Includes extra fields: owner (username) and is_owner

## Comments serializer :
#### CommentSerializer Class
- Serializes the Comment model.
- Includes extra fields: owner (username), is_owner, profile_id, and profile_image.
#### CommentDetailSerializer Class
- Inherits from CommentSerializer.
- Adds the post field (ID of the related post).

### LikeSerializer
#### The LikeSerializer is a serializer for the Like model. It has the following fields:

- owner: The username of the user who liked the post (read-only).
- id, created_at, and post: Fields from the Like model.
### FollowerSerializer
#### The FollowerSerializer is a serializer for the Follower model. It has the following fields:

- owner: The username of the user who follows another user (read-only).
- followed_name: The username of the user being followed (read-only).
- id, created_at, and followed: Fields from the Follower model.
The create method handles the creation of a new follower relationship and raises a validation error if there is a duplicate relationship.

# Views
## Posts views :
#### PostList Class (APIView)
- Handles the listing of all posts and the creation of new posts.
- Serializer class: PostSerializer
- Permission classes: IsAuthenticatedOrReadOnly
#### PostDetail Class (APIView)
- Handles the retrieval, updating, and deletion of a single post by its ID.
- Serializer class: PostSerializer
- Permission classes: IsOwnerOrReadOnly
## Profiles App views :
#### ProfileList Class (APIView)
- Handles the listing of all user profiles.
- No post method provided, as profile creation is handled by Django signals.
#### ProfileDetail Class (APIView)
- Handles the retrieval and updating of a single user profile by its ID.
- Serializer class: ProfileSerializer
- Permission classes: IsOwnerOrReadOnly
## Comments views :
#### CommentList Class (ListCreateAPIView)
- Handles the listing of all comments and the creation of new comments.
- Serializer class: CommentSerializer
- Permission classes: IsAuthenticatedOrReadOnly
#### CommentDetail Class (RetrieveUpdateDestroyAPIView)
- Handles the retrieval, updating, and deletion of a single comment by its ID.
- Serializer class: CommentDetailSerializer
- Permission classes: IsOwnerOrReadOnly

## LikeList and LikeDetail
#### The LikeList view allows users to list all likes or create a like if they are authenticated. The LikeDetail view allows users to retrieve or delete a like if they are the owner.

## FollowerList and FollowerDetail
#### The FollowerList view allows users to list all followers or create a follower (follow a user) if they are authenticated if they are authenticated. The FollowerDetail view allows users to retrieve or delete a follower (unfollow a user) if they are the owner.


# API Endpoints details bellow


# API Endpoints
Below is the documentation for each app's API endpoints.

## Posts App
### GET /api/posts/
- Description: List all posts.
- Authentication: None (public access).
- Method: GET
- Response: List of serialized Post instances.
### POST /api/posts/
- Description: Create a new post.
- Authentication: Token authentication required.
- Method: POST
- Payload: JSON object with title, content, image, and image_filter.
- Response: Serialized Post instance of the created post.
### GET /api/posts/:id/
- Description: Retrieve a specific post by its ID.
- Authentication: None (public access).
- Method: GET
- Response: Serialized Post instance.
### PUT /api/posts/:id/
- Description: Update a specific post by its ID.
- Authentication: Token authentication required, and the user must be the owner of the post.
- Method: PUT
- Payload: JSON object with the fields to update.
- Response: Serialized Post instance of the updated post.
### DELETE /api/posts/:id/
- Description: Delete a specific post by its ID.
- Authentication: Token authentication required, and the user must be the owner of the post.
- Method: DELETE
- Response: HTTP status code 204 (No Content).
# Profiles App
### GET /api/profiles/
- Description: List all user profiles.
- Authentication: None (public access).
- Method: GET
- Response: List of serialized Profile instances.
### GET /api/profiles/:id/
- Description: Retrieve a specific user profile by its ID.
- Authentication: None (public access).
- Method: GET
- Response: Serialized Profile instance.
### PUT /api/profiles/:id/
- Description: Update a specific user profile by its ID.
- Authentication: Token authentication required, and the user must be the owner of the profile.
- Method: PUT
- Payload: JSON object with the fields to update.
- Response: Serialized Profile instance of the updated profile.
# Comments App
### GET /api/comments/
- Description: List all comments.
- Authentication: None (public access).
- Method: GET
- Response: List of serialized Comment instances.
### POST /api/comments/
- Description: Create a new comment.
- Authentication: Token authentication required.
- Method: POST
- Payload: JSON object with post (ID of the related post) and content.
- Response: Serialized Comment instance of the created comment.
### GET /api/comments/:id/
- Description: Retrieve a specific comment by its ID.
- Authentication: None (public access).
- Method: GET
- Response: Serialized Comment instance.
### PUT /api/comments/:id/
- Description: Update a specific comment by its ID.
- Authentication: Token authentication required, and the user must be the owner of the comment.
- Method: PUT
- Payload: JSON object with the fields to update.
- Response: Serialized Comment instance of the updated comment.
### DELETE /api/comments/:id/
- Description: Delete a specific comment by its ID.
- Authentication: Token authentication required, and the user must be the owner of the comment.
- Method: DELETE
- Response: HTTP status code 204 (No Content).
