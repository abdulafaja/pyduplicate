import argparse


class ArgumentParser(argparse.ArgumentParser):
    """
    Argument parser class. Provide program description and define arguments
    """
    def __init__(self):
        description = ('Organize your files by filtering duplicates and move them into another directory.'
                       ' Also it move your unique files into specified directory and organize them by year and month'
                       ' of last modification')
        super(ArgumentParser, self).__init__(self, description)
        self.add_argument('-s', '--source', help='Path to files which should be organized (default: ".")', default='.')
        self.add_argument('-d', '--destination', help='Path where directories with both unique and duplicate files are '
                                                      'going to be copied (default: ".")', default='.')
