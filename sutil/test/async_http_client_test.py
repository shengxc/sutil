FAKE_SERVER_PATH = "sutil/test/fake_server.py"
if __name__ == "__main__":
    import sys
    sys.path.append("../../")
    FAKE_SERVER_PATH = "fake_server.py"
import unittest
import asyncio
import subprocess
import json
import time
from sutil.async_http_client import AsyncHttpClient
from sutil.test.fake_server import GET_RESPONSE, GET_RESPONSE_STR, TIMEOUT, PORT


class AsyncHttpClientTest(unittest.TestCase):

    def setUp(self):
        self.server = subprocess.Popen(["python", FAKE_SERVER_PATH])
        time.sleep(1)
        print("setup server success")

    def tearDown(self):
        self.server.kill()
        print("kill server success")

    def test_get(self):
        asyncio.run(self.do_test_get())

    async def do_test_get(self):
        async_http_client = AsyncHttpClient()
        url = f"http://localhost:{PORT}/test?timeout=0"
        resp = await async_http_client.get(url)
        self.assertEqual(GET_RESPONSE, resp)
        resp = await async_http_client.get(url, decode_json=False)
        self.assertEqual(GET_RESPONSE_STR, resp)
        url = f"http://localhost:{PORT}/test?timeout=1"
        start = time.time()
        self.assertEqual(None, await async_http_client.get(url, timeout=0.5, timeout_retry=3))
        self.assertGreaterEqual(time.time() - start, 0.5 * 3)
        await async_http_client.destroy()

    def test_post(self):
        asyncio.run(self.do_test_post())

    async def do_test_post(self):
        async_http_client = AsyncHttpClient()
        url = f"http://localhost:{PORT}/test?timeout=0"
        data = {"a": 1}
        resp = await async_http_client.post(url, data)
        self.assertEqual(data, resp)
        resp = await async_http_client.post(url, data, decode_json=False)
        self.assertEqual(json.dumps(data), resp)
        url = f"http://localhost:{PORT}/test?timeout=1"
        start = time.time()
        self.assertEqual(None, await async_http_client.post(url, data, timeout=0.5, timeout_retry=3))
        self.assertGreaterEqual(time.time() - start, 0.5 * 3)
        await async_http_client.destroy()

    def test_post_form(self):
        asyncio.run(self.do_test_post_form())

    async def do_test_post_form(self):
        async_http_client = AsyncHttpClient()
        url = f"http://localhost:{PORT}/test?timeout=0"
        resp = await async_http_client.post_form(url, None, {"a": ["a.txt", b'xyz', "application/octet-stream"]})
        self.assertEqual({"a": [{"filename": "a.txt", "body": "xyz", "content_type": "application/octet-stream"}]}, resp)
        await async_http_client.destroy()

    def test_with(self):
        asyncio.run(self.do_test_with())

    async def do_test_with(self):
        async with AsyncHttpClient() as async_http_client:
            url = f"http://localhost:{PORT}/test?timeout=0"
            resp = await async_http_client.get(url)
            self.assertEqual(GET_RESPONSE, resp)




if __name__ == "__main__":
    unittest.main()

