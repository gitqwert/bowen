#!/usr/bin/python
# -*-coding:utf8-*-
import unittest
class Stt(unittest.TestCase):
    def setUp(self):
        print('qwdc1')

    def tearDown(self):
        print('mnbvl2')
    @unittest.skip

    def test1(self):
        print('我执行了test1')

    def test2(self):
        print('我执行了test2')


if __name__=='__main__':
    unittest.main()


