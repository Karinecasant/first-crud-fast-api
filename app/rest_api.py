from fastapi import FastAPI

class RestAPI:
    @property
    def post_business(self):
        return self.__post_business

    @property
    def comment_business(self):
        return self.__comment_business

    @property
    def server(self):
        return self.__server

    @property
    def comment_repository(self):
        return self.__comment_repository

    @property
    def post_repository(self):
        return self.__post_repository

    def __initialize_database(self):
        self.__database = {
            'posts': [],
            'comments': []
        }

    def __initialize_repositories(self):
        from .repositories import CommentRepository, PostRepository

        self.__post_repository = PostRepository(self.__database['posts'])
        self.__comment_repository = CommentRepository(self.__database['comments'])

    def __initialize_business(self):
        from .business import CommentBusiness, PostBusiness

        self.__post_business = PostBusiness(self.__post_repository)
        self.__comment_business = CommentBusiness(self.__comment_repository, self.__post_repository)

    def __initialize_rest_server(self):
        from .rests import routers

        self.__server = FastAPI()

        for router in routers:
            self.__server.include_router(router)

    def initialize(self):
        self.__initialize_database()
        self.__initialize_repositories()
        self.__initialize_business()
        self.__initialize_rest_server()

        
rest_api = RestAPI()

