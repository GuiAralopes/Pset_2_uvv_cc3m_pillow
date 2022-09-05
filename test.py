#!/usr/bin/env python3

import os
import pset2
import unittest

TEST_DIRECTORY = os.path.dirname(__file__)

class TestImage(unittest.TestCase):
    def test_load(self):
        result = pset2.Image.load('test_images/centered_pixel.png')
        expected = pset2.Image(11, 11,
                             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 255, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                              0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(result, expected)


class TestInverted(unittest.TestCase):
    def test_inverted_1(self):
        im = pset2.Image.load('test_images/centered_pixel.png')
        result = im.inverted()
        expected = pset2.Image(11, 11,
                             [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                              255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                              255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                              255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                              255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                              255, 255, 255, 255, 255, 0, 255, 255, 255, 255, 255,
                              255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                              255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                              255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                              255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255,
                              255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255])
        self.assertEqual(result,  expected)

    def test_inverted_2(self):
        im =  pset2.Image.new (4,1)
        im.pixels = [29, 89, 136, 200]
        im.save("test_images/meu_teste/tester.png")
        result = im.inverted( )
        result.save("test_images/meu_teste/inverter_teste.png")
        self.assertTrue(im.inverted() == result)
        
    def test_inverted_3(self):
        im =  pset2.Image.load('test_images/bluegill.png')
        im.save('test_images/meu_teste/bluegill.png')
        result = im.inverted( )
        result.save('test_images/meu_teste/inverter_fish.png')
        self.assertTrue(im.inverted() == result)

    def test_inverted_4(self):
        im =  pset2.Image.load('test_images/cat.png')
        im.save('test_images/meu_teste/cat.png')
        result = im.inverted( )
        result.save('test_images/meu_teste/inverter_cat.png')
        self.assertTrue(im.inverted() == result)

    def test_inverted_images(self):
        for fname in ('mushroom', 'twocats', 'chess'):
            with self.subTest(f=fname):
                inpfile = os.path.join(TEST_DIRECTORY, 'test_images', '%s.png' % fname)
                expfile = os.path.join(TEST_DIRECTORY, 'test_results', '%s_invert.png' % fname)
                result = pset2.Image.load(inpfile).inverted()
                expected = pset2.Image.load(expfile)
                self.assertEqual(result,  expected)


class TestFilters(unittest.TestCase):

    def test_correlate(self): 
        
        im = pset2.Image.load('test_images/chess.png')
        im.save('test_images/meu_teste/chess.png')
        
        kernel = [[ 0.00, -0.07,  0.00],
                        [-0.45,  1.20, -0.25],
                        [ 0.00, -0.12,  0.00]]
        
        result = im.correlate(kernel) 
        result.save('test_images/meu_teste/chess_correlate.png')
        
        self.assertTrue(im.correlate(kernel) == result )

    def test_correlate_pig(self):
        im = pset2.Image.load('test_images/pigbird.png')
        im.save('test_images/meu_teste/pig.png')
        
        kernel=[[0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        result = im.correlate(kernel)
        result.save('test_images/meu_teste/pig_correlate.png')
        self.assertIsNot(im, result)

    def test_blurred(self):
        for kernsize in (1, 3, 7):
            for fname in ('mushroom', 'twocats', 'chess'):
                with self.subTest(k=kernsize, f=fname):
                    inpfile = os.path.join(TEST_DIRECTORY, 'test_images', '%s.png' % fname)
                    expfile = os.path.join(TEST_DIRECTORY, 'test_results', '%s_blur_%02d.png' % (fname, kernsize))
                    input_img = pset2.Image.load(inpfile)
                    input_img_copy = pset2.Image(input_img.width, input_img.height, input_img.pixels)
                    result = input_img.blurred(kernsize)
                    expected = pset2.Image.load(expfile)
                    self.assertEqual(input_img, input_img_copy, "Be careful not to modify the original image!")
                    self.assertEqual(result,  expected)

    def test_blurred_1(self):
        im = pset2.Image.load('test_images/cat.png')
        im.save('test_images/meu_teste/cat.png')
        result = im.blurred(5)
        result.save('test_images/meu_teste/cat_borrado.png')
        self.assertNotEqual(result, im)
        

    def test_sharpen(self):
        for kernsize in (1, 3, 9):
            for fname in ('mushroom', 'twocats', 'chess'):
                with self.subTest(k=kernsize, f=fname):
                    inpfile = os.path.join(TEST_DIRECTORY, 'test_images', '%s.png' % fname)
                    expfile = os.path.join(TEST_DIRECTORY, 'test_results', '%s_sharp_%02d.png' % (fname, kernsize))
                    input_img = pset2.Image.load(inpfile)
                    input_img_copy = pset2.Image(input_img.width, input_img.height, input_img.pixels)
                    result = input_img.sharpened(kernsize)
                    expected = pset2.Image.load(expfile)
                    self.assertEqual(input_img, input_img_copy, "Be careful not to modify the original image!")
                    self.assertEqual(result,  expected)

    def test_sharpened_python(self):
        im = pset2.Image.load('test_images/python.png')
        im.save('test_images/meu_teste/python.png')
                
        result = im.sharpened(11)
        result.save('test_images/meu_teste/python_sharpened.png')
        self.assertNotEqual(result, im)

    def test_edges(self):
        for fname in ('mushroom', 'twocats', 'chess'):
            with self.subTest(f=fname):
                inpfile = os.path.join(TEST_DIRECTORY, 'test_images', '%s.png' % fname)
                expfile = os.path.join(TEST_DIRECTORY, 'test_results', '%s_edges.png' % fname)
                input_img = pset2.Image.load(inpfile)
                input_img_copy = pset2.Image(input_img.width, input_img.height, input_img.pixels)
                result = input_img.edges()
                expected = pset2.Image.load(expfile)
                self.assertEqual(input_img, input_img_copy, "Be careful not to modify the original image!")
                self.assertEqual(result,  expected)

    def test_edges_obras(self):
        img=pset2.Image.load('test_images/construct.png')
        img.save("test_images/meu_teste/construct.png")
        result = img.edges()
        result.save("test_images/meu_teste/construct_edge.png")


if __name__ == '__main__':
    res = unittest.main(verbosity=3, exit=False)
