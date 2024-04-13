import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode('text node','bold' ,'https://test.com')
        node2 = TextNode('text node','bold' ,'https://test.com')
        self.assertEqual(node, node2)

    def test_text_not_eq(self):
        node = TextNode('text node','bold' ,'https://test.com')
        node2 = TextNode('text node two','bold' ,'https://test.com')
        self.assertNotEqual(node, node2)

    def test_text_type_not_eq(self):
        node = TextNode('text node','bold' ,'https://test.com')
        node2 = TextNode('text node','italic' ,'https://test.com')
        self.assertNotEqual(node, node2)

    def test_url_not_eq(self):
        node = TextNode('text node','bold' ,'https://test.com')
        node2 = TextNode('text node','bold' ,'https://test2.com')
        self.assertNotEqual(node, node2)

    def test_no_url(self):
        node = TextNode('text node','bold')
        self.assertEqual(node.url, None)

    def test_repr(self):
        node = TextNode('text node','bold' ,'https://test.com')
        self.assertEqual(node.__repr__(), "TextNode(text node, bold, https://test.com)")

if __name__ == "__main__":
    unittest.main()