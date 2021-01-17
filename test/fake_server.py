import json
import time
import tornado.ioloop
import tornado.web


GET_RESPONSE = {"a": 1}
GET_RESPONSE_STR = json.dumps(GET_RESPONSE)
TIMEOUT = "timeout"
PORT = 8888


class TestHandler(tornado.web.RequestHandler):
    def get(self):
        timeout = float(self.get_query_argument(TIMEOUT))
        if timeout > 0:
            time.sleep(timeout)
        self.write(GET_RESPONSE_STR)

    def post(self):
        timeout = float(self.get_query_argument(TIMEOUT))
        if timeout > 0:
            time.sleep(timeout)
        for k, v in self.request.files.items():
            for f in v:
                f["body"] = f["body"].decode("utf8")
        if self.request.files:
            self.write(self.request.files)
        else:
            self.write(self.request.body)


if __name__ == '__main__':
    app = tornado.web.Application([(r'/test', TestHandler)])
    app.listen(PORT)
    tornado.ioloop.IOLoop.instance().start()
