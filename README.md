# ConvergeHub-Backend

## Track Manual testing of the api

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

# Detailed class  and api explanation bellow
<details>

# Models

### The Post class is a Django model representing a post in the application. It has the following fields:

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