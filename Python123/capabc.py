#!/usr/bin/python
# -*-coding:utf8-*-
import unittest

class Stuu(unittest.TestCase):
    def setUp(self):
        print('qwe22')

    def tearDown(self):
        print('asd33')
    @unittest.skip

    def test0(self):
        print('我执行了test0')

    def test1(self):
        print('我执行了test1')


if __name__=='__main__':
    unittest.main()