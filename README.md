# Book Exchange API

This is a RESTful API for a book exchange site built using Python, Django, and Django REST Framework.

The site allows users to register, add books they have (i.e. books they can lend), and books they need to borrow. Users can then send requests to exchange books with other users.

The API includes a powerful filter that allows users to find other users who have books they need and who need books they have.


## Technologies Used

- Python
- Django
- Django REST Framework

## Installation and Setup

1. Clone the repository to your local machine.
2. Create and activate a virtual environment.
3. Install the dependencies using the command: `pip install -r requirements.txt`.
4. Create a .env file using the .env.example file and provide your own environment variables.
5. Run the server using the command: `python manage.py runserver`.

## API Authentication

Token authentication is used for user authentication. Users can obtain their token by making a `POST` request to `/users/login/` with their `username` and `password`. The token should be included in the `Authorization` header of subsequent requests.

## Contributing

Contributions to this project are welcome. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch.
3. Make your changes and commit them with clear commit messages.
4. Push your changes to your fork.
5. Submit a pull request with a detailed description of your changes.


