from controllers.userController import userController

def init_app(server):
    #handle routes for Api
    server.include_router(userController)

    @server.get('/')
    def main():
        return 'Hello word'
    
    