FAKE_SERVER_PATH = "test/fake_server.py"
if __name__ == "__main__":
    import sys
    import common
    sys.path.append(common.ROOT_DIR)
    FAKE_SERVER_PATH = "fake_server.py"
import unittest
import subprocess
import json
import time
from sutil.http_client import HttpClient
from test.fake_server import GET_RESPONSE, GET_RESPONSE_STR, TIMEOUT, PORT


class HttpClientTest(unittest.TestCase):

    def setUp(self):
        self.server = subprocess.Popen(["python", FAKE_SERVER_PATH])
        time.sleep(1)
        print("setup server success")

    def tearDown(self):
        self.server.kill()
        print("kill server success")

    def test_get(self):
        http_client = HttpClient()
        url = f"http://localhost:{PORT}/test?timeout=0"
        resp = http_client.get(url)
        self.assertEqual(GET_RESPONSE, resp)
        resp = http_client.get(url, decode_json=False)
        self.assertEqual(GET_RESPONSE_STR, resp)
        url = f"http://localhost:{PORT}/test?timeout=1"
        start = time.time()
        self.assertEqual(None, http_client.get(url, timeout=0.5, timeout_retry=3))
        self.assertGreaterEqual(time.time() - start, 0.5 * 3)

    def test_post(self):
        http_client = HttpClient()
        url = f"http://localhost:{PORT}/test?timeout=0"
        data = {"a": 1}
        resp = http_client.post(url, data)
        self.assertEqual(data, resp)
        resp = http_client.post(url, data, decode_json=False)
        self.assertEqual(json.dumps(data), resp)
        url = f"http://localhost:{PORT}/test?timeout=1"
        start = time.time()
        self.assertEqual(None, http_client.post(url, data, timeout=0.5, timeout_retry=3))
        self.assertGreaterEqual(time.time() - start, 0.5 * 3)

    def test_post_form(self):
        http_client = HttpClient()
        url = f"http://localhost:{PORT}/test?timeout=0"
        resp = http_client.post_form(url, None, {"a": ["a.txt", b'xyz', "application/octet-stream"]})
        self.assertEqual({"a": [{"filename": "a.txt", "body": "xyz", "content_type": "application/octet-stream"}]}, resp)




if __name__ == "__main__":
    unittest.main()
