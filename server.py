import http.server

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cross-Origin-Opener-Policy', 'same-origin')
        self.send_header('Cross-Origin-Embedder-Policy', 'require-corp')
        return super().end_headers()

if __name__ == '__main__':
    http.server.test(HandlerClass=HTTPRequestHandler)