import unittest, time
import app
class Test(unittest.TestCase):#Test_1
  pass
class Test2(unittest.TestCase):#Test_2
  pass
class Test3(unittest.TestCase):#Test_3
  pass

class Test4(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_ids_after_delete(self):
        self.app.delete("/delete/?id=547")
        time.sleep(2)
        response = query_index_by_text('docs', 'святой')
        assert response == [871, 872]

if __name__ == '__main__':
    unittest.main()

