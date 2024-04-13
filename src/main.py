from textnode import TextNode

def main():
    node = TextNode('text node','bold' ,'https://test.com')
    print('here:', node.__repr__())

main()