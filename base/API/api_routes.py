class APIRoutes:
    base_url: str = 'https://jsonplaceholder.typicode.com'

    POSTS: str = '/posts/'
    COMMENTS: str = '/comments/'
    ALBUMS: str = '/albums/'
    PHOTOS: str = '/photos/'
    TODOS: str = '/todos/'
    USERS: str = '/users/'

    posts_url = base_url + POSTS
    users_url = base_url + USERS
    todos_url = base_url + TODOS
    photos_url = base_url + PHOTOS
    albums_url = base_url + ALBUMS
    comments_url = base_url + COMMENTS
