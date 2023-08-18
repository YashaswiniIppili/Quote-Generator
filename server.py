import socket
import ssl
import threading
import random

class Server:
    def __init__(self):
        self.host = 'localhost'
        self.port = 8080
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        self.ssl_context.load_cert_chain(certfile="cert.pem")

        self.quotes = [
                "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle. - Christian D. Larson",
                "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. - Albert Schweitzer",
                "The best way out is always through. - Robert Frost",
                "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
                "I can't change the direction of the wind, but I can adjust my sails to always reach my destination. - Jimmy Dean",
                "Believe you can and you're halfway there. - Theodore Roosevelt",
                "It does not matter how slowly you go as long as you do not stop. - Confucius",
                "The only way to do great work is to love what you do. - Steve Jobs",
                "Happiness is not something ready made. It comes from your own actions. - Dalai Lama",
                "I have not failed. I've just found 10,000 ways that won't work. - Thomas Edison",
                "If you want to live a happy life, tie it to a goal, not to people or things. - Albert Einstein",
                "What you get by achieving your goals is not as important as what you become by achieving your goals. - Zig Ziglar",
                "The mind is everything. What you think you become. - Buddha",
                "If you haven't found it yet, keep looking. Don't settle. As with all matters of the heart, you'll know when you find it. - Steve Jobs",
                "You must be the change you wish to see in the world. - Mahatma Gandhi",
                "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
                "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. - Oprah Winfrey",
                "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
                "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
                "I've failed over and over and over again in my life. And that is why I succeed. - Michael Jordan",
                "If you can't explain it simply, you don't understand it well enough. - Albert Einstein",
                "Education is the most powerful weapon which you can use to change the world. - Nelson Mandela",
                "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
                "Don't watch the clock; do what it does. Keep going. - Sam Levenson",
                "It is not in the stars to hold our destiny but in ourselves. - William Shakespeare",
                "The only way to have a good day is to start it with a positive attitude. - Unknown",
                "Your time is limited, don't waste it living someone else's life. - Steve Jobs",
                "If you want to achieve greatness, stop asking for permission. - Unknown",
                "The only true wisdom is in knowing you know nothing. - Socrates",
                "Don't let yesterday take up too much of today. - Will Rogers",
                "Believe you can and you're halfway there. - Theodore Roosevelt",
                "The best way to predict the future is to create it. - Peter Drucker",
                "If you want something you've never had, you must be willing to do something you've never done. - Thomas Jefferson",
                "The only source of knowledge is experience. - Albert Einstein",
                "Success is stumbling from failure to failure with no loss of enthusiasm. - Winston Churchill",
                "Your work is going to fill a large part of your life, and the only way to be truly satisfied is to do what you believe is great work. - Steve Jobs",
                "The difference between ordinary and extraordinary is that little extra. - Jimmy Johnson",
                "In the midst of winter, I found there was, within me, an invincible summer. - Albert Camus",
                "Do not wait to strike till the iron is hot; but make it hot by striking. - William Butler Yeats",
                "The man who has confidence in himself gains the confidence of others. - Hasidic Proverb",
                "Believe in yourself, take on your challenges, dig deep within yourself to conquer fears. Never let anyone bring you down. - Chantal Sutherland",
                "A goal without a plan is just a wish. - Antoine de Saint-Exupéry",
                "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
                "The only thing necessary for the triumph of evil is for good men to do nothing. - Edmund Burke",
                "It's not the load that breaks you down, it's the way you carry it. - Lou Holtz",
                "It's not what happens to you, but how you react to it that matters. - Epictetus",
                "Nothing is impossible, the word itself says 'I'm possible'! - Audrey Hepburn",
                "I have a dream that one day this nation will rise up and live out the true meaning of its creed: 'We hold these truths to be self-evident, that all men are created equal.' - Martin Luther King Jr.",
                "A successful man is one who can lay a firm foundation with the bricks others have thrown at him. - David Brinkley",
                "If you don't stand for something you will fall for anything. - Malcolm X",
                "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
                "Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time. - Thomas A. Edison",
                "The only person you are destined to become is the person you decide to be. - Ralph Waldo Emerson",
                "I can't change the direction of the wind, but I can adjust my sails to always reach my destination. - Jimmy Dean"
            ]

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server started on {self.host}:{self.port}")
        while True:
            client_socket, client_address = self.server_socket.accept()
            client_socket = self.ssl_context.wrap_socket(client_socket, server_side=True)
            print(f"New client connected: {client_address}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received message from client: {data.decode()}")
                if data == b"generate":
                    quote = random.choice(self.quotes)
                    client_socket.sendall(quote.encode())
                else:
                    client_socket.sendall(b"Invalid command")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            client_socket.close()


if __name__ == '__main__':
    server = Server()
    server.start_server()
