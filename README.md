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
