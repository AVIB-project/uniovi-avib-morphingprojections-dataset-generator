"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following lines in the
``[options.entry_points]`` section in ``setup.cfg``::

    console_scripts =
         fibonacci = morphingprojections_dataset_generator.skeleton:run

Then run ``pip install .`` (or ``pip install -e .`` for editable mode)
which will install the command ``fibonacci`` inside your current environment.

Besides console scripts, the header (i.e. until ``_logger``...) of this file can
also be used as template for Python modules.

Note:
    This file can be renamed depending on your needs or safely removed if not needed.

References:
    - https://setuptools.pypa.io/en/latest/userguide/entry_point.html
    - https://pip.pypa.io/en/stable/reference/pip_install
"""

import argparse
import logging
import sys
import random

import pandas as pd

from morphingprojections_dataset_generator import __version__

__author__ = "Miguel Salinas Gancedo"
__copyright__ = "Miguel Salinas Gancedo"
__license__ = "MIT"

_logger = logging.getLogger(__name__)


# ---- Python API ----
def generator(num_samples, num_attributes, num_sample_annotations, num_attribute_annotations):
    _logger.info(num_samples)
    _logger.info(num_attributes)

    # Generate random datamatrix dataframe
    attributes = []    
    for attribute_index in range(1, num_attributes + 1):  
        attributes.append("A" + str(attribute_index))

    samples = []
    datamatrix_list = []    
    for sample_index in range(1, num_samples + 1): 
        samples.append("S" + str(sample_index)) 
        sample_values = []
        for attribute_index in range(num_attributes):
            sample_values.append(random.random())

        datamatrix_list.append(tuple(sample_values))

    datamatrix = pd.DataFrame(datamatrix_list, index = samples, columns = attributes)

    print(datamatrix)  

    datamatrix.to_csv('./export/datamatrix.csv', sep=',', index=True, encoding='utf-8')

    # Generate random sample annotion dataframe
    sample_annotations = []   
    for sample_annotation_index in range(1, num_sample_annotations + 1): 
        sample_annotations.append("SA" + str(sample_annotation_index)) 
    
    sample_annotations_list = [] 
    for sample_index in range(1, num_samples + 1):
        sample_annotation_values = []
        for sample_annotation_index in range(1, num_sample_annotations + 1): 
            sample_annotation_values.append(random.random())
        
        sample_annotations_list.append(tuple(sample_annotation_values))

    sample_annotations = pd.DataFrame(sample_annotations_list, index = range(len(sample_annotations_list)), columns = sample_annotations)

    print(sample_annotations)  

    sample_annotations.to_csv('./export/sample_annotations.csv', sep=',', index=False, encoding='utf-8')

    # Generate random attribute annotion dataframe
    attribute_annotations = []   
    for attribute_annotation_index in range(1, num_attribute_annotations + 1): 
        attribute_annotations.append("AA" + str(attribute_annotation_index)) 
    
    attribute_annotations_list = [] 
    for attribute_index in range(1, num_attributes + 1):
        attribute_annotation_values = []
        for attribute_annotation_index in range(1, num_attribute_annotations + 1): 
            attribute_annotation_values.append(random.random())
        
        attribute_annotations_list.append(tuple(attribute_annotation_values))

    attribute_annotations = pd.DataFrame(attribute_annotations_list, index = range(len(attribute_annotations_list)), columns = attribute_annotations)

    print(attribute_annotations)

    attribute_annotations.to_csv('./export/attribute_annotations.csv', sep=',', index=False, encoding='utf-8')
  
# ---- CLI ----
# The functions defined in this section are wrappers around the main Python
# API allowing them to be called directly from the terminal as a CLI
# executable/script.


def parse_args(args):
    """Parse command line parameters

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--help"]``).

    Returns:
      :obj:`argparse.Namespace`: command line parameters namespace
    """
    parser = argparse.ArgumentParser(description="Dataset Generator")
    parser.add_argument(
        "--version",
        action="version",
        version=f"uniovi-avib-morphingprojections-dataset-generator {__version__}",
    )
    parser.add_argument(
        "--num_samples",
        dest="num_samples",
        default=100,
        help="Number of samples",
        type=int,
        metavar="INT"
    )
    parser.add_argument(
        "--num_attributes",
        dest="num_attributes",
        default=5,
        help="Number of attribute per sample",
        type=int,
        metavar="INT"
    )
    parser.add_argument(
        "--num_sample_annotations",
        dest="num_sample_annotations",
        help="Number sample annotations",
        default=0,
        type=int,
        metavar="INT"
    )
    parser.add_argument(
        "--num_attribute_annotations",
        dest="num_attribute_annotations",
        help="Number attribute annotations",
        default=0,
        type=int,
        metavar="INT"
    )       
    parser.add_argument(
        "-v",
        "--verbose",
        dest="loglevel",
        help="set loglevel to INFO",
        action="store_const",
        const=logging.INFO,
    )
    parser.add_argument(
        "-vv",
        "--very-verbose",
        dest="loglevel",
        help="set loglevel to DEBUG",
        action="store_const",
        const=logging.DEBUG,
    )
    return parser.parse_args(args)


def setup_logging(loglevel):
    """Setup basic logging

    Args:
      loglevel (int): minimum loglevel for emitting messages
    """
    logformat = "[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
    logging.basicConfig(
        level=loglevel, stream=sys.stdout, format=logformat, datefmt="%Y-%m-%d %H:%M:%S"
    )


def main(args):
    """Wrapper allowing :func:`fib` to be called with string arguments in a CLI fashion

    Instead of returning the value from :func:`fib`, it prints the result to the
    ``stdout`` in a nicely formatted message.

    Args:
      args (List[str]): command line parameters as list of strings
          (for example  ``["--verbose", "42"]``).
    """
    args = parse_args(args)
    setup_logging(args.loglevel)

    _logger.debug("Starting calculations...")
    generator(args.num_samples, args.num_attributes, args.num_sample_annotations, args.num_attribute_annotations)    
    _logger.info("Script ends here")


def run():
    """Calls :func:`main` passing the CLI arguments extracted from :obj:`sys.argv`

    This function can be used as entry point to create console scripts with setuptools.
    """
    main(sys.argv[1:])


if __name__ == "__main__":
    # ^  This is a guard statement that will prevent the following code from
    #    being executed in the case someone imports this file instead of
    #    executing it as a script.
    #    https://docs.python.org/3/library/__main__.html

    # After installing your project with pip, users can also run your Python
    # modules as scripts via the ``-m`` flag, as defined in PEP 338::
    #
    #     python -m morphingprojections_dataset_generator.skeleton 42
    #
    run()
